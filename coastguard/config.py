import ConfigParser
from lib.hostfilter import HostFilter
import os


def get_boolean(param):
    """
    Convert string to boolean from config file
    :rtype : object
    :param param: str. config parameter
    :return: bool. unless it can't be read, then return None
    """
    if param.lower == "false":
        return False
    elif param.lower == "true":
        return True
    else:
        return None


def load_config(configfile):
    """
    Load config from ini formatted text file
    :rtype : config object
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
    config['terminate_long_running'] = get_boolean(parser.get('settings', 'terminate_long_running'))
    # One-liner because Daniel's fancy that way.
    config['DO_TOKEN'] = os.environ.get('DO_TOKEN', None) or parser.get('DigitalOcean', 'DO_TOKEN')
    config['HostFilter'] = HostFilter.fromConfig(parser)
    return config

