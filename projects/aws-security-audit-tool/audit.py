"""
AWS Security Audit Tool
-----------------------
Checks your AWS account for common security misconfigurations.

Checks performed:
  1.  Root account MFA enabled
  2.  IAM password policy strength
  3.  No active root access keys
  4.  CloudTrail enabled and logging
  5.  Public S3 buckets (Block Public Access)
  6.  Security groups open to 0.0.0.0/0 on SSH (22) or RDP (3389)
  7.  GuardDuty enabled
  8.  AWS Config enabled
  9.  Default VPC exists (flags as a risk reminder)
  10. IAM users with console access but no MFA

Usage:
  pip install -r requirements.txt
  python audit.py                      # uses default AWS profile
  python audit.py --profile my-profile # uses a named AWS profile
  python audit.py --region us-east-1   # specify region (default: us-east-1)
  python audit.py --output report.txt  # save report to file
"""

import argparse
import sys
import datetime
import boto3
from botocore.exceptions import ClientError, NoCredentialsError, EndpointConnectionError

# ── Formatting helpers ────────────────────────────────────────────────────────

GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

def passed(msg):  return f"  {GREEN}[PASS]{RESET} {msg}"
def failed(msg):  return f"  {RED}[FAIL]{RESET} {msg}"
def warning(msg): return f"  {YELLOW}[WARN]{RESET} {msg}"
def info(msg):    return f"  {BLUE}[INFO]{RESET} {msg}"

def section(title):
    bar = "─" * 60
    return f"\n{BOLD}{bar}\n  {title}\n{bar}{RESET}"

# ── Individual checks ─────────────────────────────────────────────────────────

def check_root_mfa(iam):
    lines = []
    try:
        summary = iam.get_account_summary()["SummaryMap"]
        if summary.get("AccountMFAEnabled", 0) == 1:
            lines.append(passed("Root account MFA is enabled"))
        else:
            lines.append(failed("Root account MFA is NOT enabled — enable it immediately"))
    except ClientError as e:
        lines.append(warning(f"Could not check root MFA: {e.response['Error']['Code']}"))
    return lines


def check_root_access_keys(iam):
    lines = []
    try:
        summary = iam.get_account_summary()["SummaryMap"]
        key_count = summary.get("AccountAccessKeysPresent", 0)
        if key_count == 0:
            lines.append(passed("No active root account access keys"))
        else:
            lines.append(failed(f"Root account has {key_count} active access key(s) — delete them"))
    except ClientError as e:
        lines.append(warning(f"Could not check root access keys: {e.response['Error']['Code']}"))
    return lines


def check_password_policy(iam):
    lines = []
    try:
        policy = iam.get_account_password_policy()["PasswordPolicy"]
        issues = []
        if policy.get("MinimumPasswordLength", 0) < 14:
            issues.append(f"minimum length is {policy.get('MinimumPasswordLength')} (recommend ≥14)")
        if not policy.get("RequireUppercaseCharacters"):
            issues.append("uppercase characters not required")
        if not policy.get("RequireLowercaseCharacters"):
            issues.append("lowercase characters not required")
        if not policy.get("RequireNumbers"):
            issues.append("numbers not required")
        if not policy.get("RequireSymbols"):
            issues.append("symbols not required")
        if not policy.get("MaxPasswordAge"):
            issues.append("no password expiry set")

        if issues:
            lines.append(failed("IAM password policy is weak:"))
            for i in issues:
                lines.append(f"      • {i}")
        else:
            lines.append(passed("IAM password policy meets recommended standards"))
    except iam.exceptions.NoSuchEntityException:
        lines.append(failed("No IAM password policy is set"))
    except ClientError as e:
        lines.append(warning(f"Could not check password policy: {e.response['Error']['Code']}"))
    return lines


def check_cloudtrail(session, region):
    lines = []
    try:
        ct = session.client("cloudtrail", region_name=region)
        trails = ct.describe_trails(includeShadowTrails=False)["trailList"]
        if not trails:
            lines.append(failed(f"No CloudTrail trails found in {region}"))
            return lines

        for trail in trails:
            name = trail["Name"]
            try:
                status = ct.get_trail_status(Name=trail["TrailARN"])
                if status.get("IsLogging"):
                    lines.append(passed(f"CloudTrail '{name}' is active and logging"))
                else:
                    lines.append(failed(f"CloudTrail '{name}' exists but logging is DISABLED"))
            except ClientError:
                lines.append(warning(f"Could not get status for trail '{name}'"))
    except ClientError as e:
        lines.append(warning(f"Could not check CloudTrail: {e.response['Error']['Code']}"))
    return lines


def check_s3_public_access(session):
    lines = []
    try:
        s3  = session.client("s3")
        s3c = session.client("s3control")
        sts = session.client("sts")
        account_id = sts.get_caller_identity()["Account"]

        # Account-level block
        try:
            config = s3c.get_public_access_block(AccountId=account_id)["PublicAccessBlockConfiguration"]
            all_blocked = all([
                config.get("BlockPublicAcls"),
                config.get("IgnorePublicAcls"),
                config.get("BlockPublicPolicy"),
                config.get("RestrictPublicBuckets"),
            ])
            if all_blocked:
                lines.append(passed("Account-level S3 Block Public Access is fully enabled"))
            else:
                lines.append(warning("Account-level S3 Block Public Access is partially disabled — check individual settings"))
        except ClientError:
            lines.append(warning("Could not check account-level S3 Block Public Access"))

        # Per-bucket check
        buckets = s3.list_buckets().get("Buckets", [])
        if not buckets:
            lines.append(info("No S3 buckets found in this account"))
            return lines

        public_buckets = []
        for bucket in buckets:
            bname = bucket["Name"]
            try:
                bconfig = s3.get_public_access_block(Bucket=bname)["PublicAccessBlockConfiguration"]
                if not all([
                    bconfig.get("BlockPublicAcls"),
                    bconfig.get("IgnorePublicAcls"),
                    bconfig.get("BlockPublicPolicy"),
                    bconfig.get("RestrictPublicBuckets"),
                ]):
                    public_buckets.append(bname)
            except ClientError as e:
                if e.response["Error"]["Code"] == "NoSuchPublicAccessBlockConfiguration":
                    public_buckets.append(bname)

        if public_buckets:
            lines.append(failed(f"{len(public_buckets)} bucket(s) have public access not fully blocked:"))
            for b in public_buckets:
                lines.append(f"      • {b}")
        else:
            lines.append(passed(f"All {len(buckets)} S3 bucket(s) have Block Public Access enabled"))

    except ClientError as e:
        lines.append(warning(f"Could not check S3: {e.response['Error']['Code']}"))
    return lines


def check_security_groups(session, region):
    lines = []
    risky_ports = {22: "SSH", 3389: "RDP"}
    try:
        ec2 = session.client("ec2", region_name=region)
        sgs = ec2.describe_security_groups()["SecurityGroups"]
        exposed = []

        for sg in sgs:
            for rule in sg.get("IpPermissions", []):
                from_port = rule.get("FromPort", 0)
                to_port   = rule.get("ToPort", 65535)
                for port, service in risky_ports.items():
                    if from_port <= port <= to_port:
                        for cidr in rule.get("IpRanges", []):
                            if cidr.get("CidrIp") in ("0.0.0.0/0",):
                                exposed.append(
                                    f"{sg['GroupId']} ({sg['GroupName']}) — "
                                    f"port {port} ({service}) open to 0.0.0.0/0"
                                )
                        for cidr6 in rule.get("Ipv6Ranges", []):
                            if cidr6.get("CidrIpv6") == "::/0":
                                exposed.append(
                                    f"{sg['GroupId']} ({sg['GroupName']}) — "
                                    f"port {port} ({service}) open to ::/0"
                                )

        if exposed:
            lines.append(failed(f"{len(exposed)} security group rule(s) expose sensitive ports to the internet:"))
            for e in exposed:
                lines.append(f"      • {e}")
        else:
            lines.append(passed(f"No security groups expose SSH/RDP to 0.0.0.0/0 in {region}"))
    except ClientError as e:
        lines.append(warning(f"Could not check security groups: {e.response['Error']['Code']}"))
    return lines


def check_guardduty(session, region):
    lines = []
    try:
        gd = session.client("guardduty", region_name=region)
        detectors = gd.list_detectors()["DetectorIds"]
        if not detectors:
            lines.append(failed(f"GuardDuty is NOT enabled in {region}"))
        else:
            for det_id in detectors:
                detail = gd.get_detector(DetectorId=det_id)
                if detail["Status"] == "ENABLED":
                    lines.append(passed(f"GuardDuty is enabled in {region} (detector: {det_id})"))
                else:
                    lines.append(failed(f"GuardDuty detector {det_id} exists but is DISABLED"))
    except ClientError as e:
        lines.append(warning(f"Could not check GuardDuty: {e.response['Error']['Code']}"))
    return lines


def check_aws_config(session, region):
    lines = []
    try:
        cfg = session.client("config", region_name=region)
        recorders = cfg.describe_configuration_recorders()["ConfigurationRecorders"]
        if not recorders:
            lines.append(failed(f"AWS Config has no recorders configured in {region}"))
            return lines
        statuses = cfg.describe_configuration_recorder_status()["ConfigurationRecordersStatus"]
        for s in statuses:
            if s.get("recording"):
                lines.append(passed(f"AWS Config recorder '{s['name']}' is active in {region}"))
            else:
                lines.append(failed(f"AWS Config recorder '{s['name']}' exists but is NOT recording"))
    except ClientError as e:
        lines.append(warning(f"Could not check AWS Config: {e.response['Error']['Code']}"))
    return lines


def check_default_vpc(session, region):
    lines = []
    try:
        ec2  = session.client("ec2", region_name=region)
        vpcs = ec2.describe_vpcs(Filters=[{"Name": "isDefault", "Values": ["true"]}])["Vpcs"]
        if vpcs:
            lines.append(warning(
                f"Default VPC exists in {region} — "
                "consider deleting it to reduce attack surface if not in use"
            ))
        else:
            lines.append(passed(f"No default VPC in {region}"))
    except ClientError as e:
        lines.append(warning(f"Could not check default VPC: {e.response['Error']['Code']}"))
    return lines


def check_iam_users_mfa(iam):
    lines = []
    try:
        paginator = iam.get_paginator("list_users")
        no_mfa = []

        for page in paginator.paginate():
            for user in page["Users"]:
                uname = user["UserName"]
                try:
                    login_profile = iam.get_login_profile(UserName=uname)
                    # User has console access — check MFA
                    mfa_devices = iam.list_mfa_devices(UserName=uname)["MFADevices"]
                    if not mfa_devices:
                        no_mfa.append(uname)
                except iam.exceptions.NoSuchEntityException:
                    pass  # no console access, skip

        if no_mfa:
            lines.append(failed(f"{len(no_mfa)} IAM user(s) have console access but NO MFA:"))
            for u in no_mfa:
                lines.append(f"      • {u}")
        else:
            lines.append(passed("All IAM users with console access have MFA enabled"))
    except ClientError as e:
        lines.append(warning(f"Could not check IAM user MFA: {e.response['Error']['Code']}"))
    return lines


# ── Main runner ───────────────────────────────────────────────────────────────

def run_audit(profile, region, output_file):
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    report_lines = []

    def log(line=""):
        print(line)
        # Strip ANSI codes for file output
        clean = line
        for code in [GREEN, RED, YELLOW, BLUE, RESET, BOLD]:
            clean = clean.replace(code, "")
        report_lines.append(clean)

    log(f"\n{BOLD}{'='*60}")
    log(f"  AWS SECURITY AUDIT REPORT")
    log(f"  Generated: {timestamp}")
    log(f"  Region:    {region}")
    log(f"  Profile:   {profile or 'default'}")
    log(f"{'='*60}{RESET}")

    try:
        session_kwargs = {"region_name": region}
        if profile:
            session_kwargs["profile_name"] = profile
        session = boto3.Session(**session_kwargs)
        iam = session.client("iam")

        # Confirm identity
        try:
            sts = session.client("sts")
            identity = sts.get_caller_identity()
            log(info(f"Authenticated as: {identity['Arn']}"))
            log(info(f"Account ID:       {identity['Account']}"))
        except Exception:
            log(warning("Could not confirm AWS identity — proceeding anyway"))

    except NoCredentialsError:
        print(f"\n{RED}ERROR: No AWS credentials found.{RESET}")
        print("  Run 'aws configure' or set AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY env vars.")
        sys.exit(1)

    # ── Run all checks ────────────────────────────────────────────────────────

    checks = [
        ("Root Account Security",        [*check_root_mfa(iam), *check_root_access_keys(iam)]),
        ("IAM Password Policy",           check_password_policy(iam)),
        ("IAM User MFA",                  check_iam_users_mfa(iam)),
        ("CloudTrail Logging",            check_cloudtrail(session, region)),
        ("S3 Bucket Public Access",       check_s3_public_access(session)),
        ("Security Group Exposure",       check_security_groups(session, region)),
        ("GuardDuty Threat Detection",    check_guardduty(session, region)),
        ("AWS Config Recording",          check_aws_config(session, region)),
        ("Default VPC",                   check_default_vpc(session, region)),
    ]

    pass_count = fail_count = warn_count = 0

    for title, results in checks:
        log(section(title))
        for line in results:
            log(line)
            if "[PASS]" in line: pass_count += 1
            elif "[FAIL]" in line: fail_count += 1
            elif "[WARN]" in line: warn_count += 1

    # ── Summary ───────────────────────────────────────────────────────────────

    log(f"\n{BOLD}{'='*60}")
    log("  SUMMARY")
    log(f"{'='*60}{RESET}")
    log(passed(f"{pass_count} check(s) passed"))
    log(failed(f"{fail_count} check(s) failed  ← remediate these"))
    log(warning(f"{warn_count} warning(s)"))
    log(f"\n  Score: {pass_count}/{pass_count + fail_count} checks passed\n")

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(report_lines))
        print(info(f"Report saved to: {output_file}"))


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="AWS Security Audit Tool — checks your account for common misconfigurations"
    )
    parser.add_argument("--profile", default=None,      help="AWS CLI profile name (default: default)")
    parser.add_argument("--region",  default="us-east-1", help="AWS region to audit (default: us-east-1)")
    parser.add_argument("--output",  default=None,      help="Save report to a text file")
    args = parser.parse_args()

    run_audit(args.profile, args.region, args.output)
