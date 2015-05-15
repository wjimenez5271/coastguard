# coastguard
Enforce good behavior in DigitalOcean

### Ideas
- Warn if resources have been running for too long
- Warn if firewalls are not running
- Warn if deprecated/revoked SSH keys are being used (according to DO API)
- Warn if backups are running/not running (depending on desired state)
- Warn if instance launch rate deviates significantly (detect abuse, program errors)
- Optionally terminate long-running resources, or ones that violate security requirements
- Report stats on life-cycles of resources (longest running, avg running time, churn rate, avg resource sizes, etc)
- Communicate warnings via email, XMPP, and platform specific APIs like hipchat, slack, pagerduty, etc.
