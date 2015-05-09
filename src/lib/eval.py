import do
from datetime import datetime, timedelta

DO_TOKEN = ''


class CheckBase(object):
    def __init__(self):
        pass

    def check_uptime(self, max_uptime):
        raise NotImplementedError


class DoChecks(CheckBase):
    def check_uptime(self, max_uptime):
        hosts_violated =[]
        c = do.Digtal_Ocean(DO_TOKEN)
        for i in c.get_uptime():
            # ts format: 2015-05-07T22:27:38Z
            if (i['created_at'] - datetime.utcnow()) > timedelta(hours=max_uptime):
                hosts_violated.append(i)
        return hosts_violated