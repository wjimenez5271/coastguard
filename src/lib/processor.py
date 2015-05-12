import do
import actions


def go(config):
    _DOChecks = do.DOChecks()
    for host in _DOChecks.check_uptime(config['uptime_threshold']):
        if config['email_alert']:
            message = host+" has been running for too long"
            actions.NotificationActions.alert(
                config['subject'],
                message,
                config['mail_sender'],
                config['mail_recipient'],
                config['mail_server'],
            )
