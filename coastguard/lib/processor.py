import do
import actions
from util import *
import logging
import do

log = logging.getLogger('coastguard')

def go(config):
    """
    Base method for starting coastguard
    :param config: dict. Configuration object
    :return:
    """
    log.info('Starting digital ocean checks')
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
            if config['terminate_long_running']:
                terminate_instance(host, config)
    except CoastguardSendEmailError:
        log.error('unable to send mail')
    except CoastguardAPIError:
        log.error('Exception communicating with infrastructure provider API')
    except Exception as e:
        log.exception(e)
        log.error('Unhandled exception processing digital ocean checks')
        raise CoastguardException


def terminate_instance(host, config):
    log.info('Terminating instance {0}'.format(str(host)))
    d = do.DOActions(config['DO_TOKEN'])
    d.terminate_instance(host)