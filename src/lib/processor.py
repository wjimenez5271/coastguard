import do
import actions


def go(config):
    for host in do.DoChecks.check_uptime():
        if config['email_alert']:
            message = host+" has been running for too long"
            actions.NotificationActions.alert(
                config['subject'],
                message,
                config['mail_sender'],
                config['mail_recipient'],
                config['mail_server'],
            )


