import do
import actions
from exceptions import *


def go(config):
    """
    Base method for starting coastguard
    :param config: dict. Configuration object
    :return:
    """
    _DOChecks = do.DOChecks(config['DO_TOKEN'])
    try:
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
    except CoastguardSendEmailError:
        print "unable to send mail"
    except:
        raise CoastguardException
