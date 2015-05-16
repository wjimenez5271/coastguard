import ConfigParser
import os

def load_config(configfile):
    """
    Load config from ini formatted text file
    :param configfile: str. path to file
    :return: dict. configuration attributes
    """
    parser = ConfigParser.SafeConfigParser()
    parser.read(configfile)
    config = {}
    config['mail_server'] = parser.get('settings', 'mail_server')
    config['mail_recipient'] = parser.get('settings', 'mail_recipient')
    config['mail_sender'] = parser.get('settings', 'mail_sender')
    config['subject'] = parser.get('settings', 'subject')
    config['mail_alert_address'] = parser.get('settings', 'mail_alert_address')
    config['email_alert'] = parser.get('settings', 'email_alert')
    config['uptime_threshold'] = parser.get('settings', 'uptime_threshold')
    config['terminate_long_running'] = parser.get('settings', 'terminate_long_running')
    if config['terminate_long_running'].lower == "false":
        config['terminate_long_running'] = False
    elif config['terminate_long_running'].lower == "true":
        config['terminate_long_running'] = True
    else:
        config['terminate_long_running'] = None
    # One-liner because Daniel's fancy that way.
    config['DO_TOKEN'] = os.environ.get('DO_TOKEN', None) or parser.get('DigitalOcean', 'DO_TOKEN')
    return config

