import ConfigParser


def load_config(configfile):
    parser = ConfigParser.SafeConfigParser()
    parser.read(configfile)
    config = {}
    config['mail_server'] = parser.get('settings', 'mail_server')
    config['mail_recipient'] = parser.get('settings', 'mail_recipient')
    config['mail_sender'] = parser.get('settings', 'mail_sender')
    config['subject'] = parser.get('settings', 'subject')
    config['mail_alert_address'] = parser.get('settings', 'mail_alert_address')
    return config

