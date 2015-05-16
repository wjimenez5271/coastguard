[![Join the chat at https://gitter.im/wjimenez5271/coastguard](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/wjimenez5271/coastguard?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
# Coastguard
Enforce good behavior in DigitalOcean

### Installation
From the repo root
```
python setup.py install
```
This should install the console script `coastguard` into your PATH.

### Usage
```
coastguard --config configfile.ini
```

Requires DO API token. This can either be set in the `.ini` config file or as an environment variable named `DO_TOKEN` (with the evar taking precedence). 

### Ideas
- Warn if resources have been running for too long
- Warn if firewalls are not running
- Warn if deprecated/revoked SSH keys are being used (according to DO API)
- Warn if backups are running/not running (depending on desired state)
- Warn if instance launch rate deviates significantly (detect abuse, program errors)
- Optionally terminate long-running resources, or ones that violate security requirements
- Report stats on life-cycles of resources (longest running, avg running time, churn rate, avg resource sizes, etc)
- Communicate warnings via email, XMPP, and platform specific APIs like hipchat, slack, pagerduty, etc.

Pull requests welcome!
