import digitalocean
from datetime import datetime, timedelta
from eval import *
from exceptions import  *



class DigitalOcean(object):
    def __init__(self, do_token):
        self.do_token = do_token
        self._conn = None

    def conn(self):
        if not self._conn:
            self._conn = digitalocean.Manager(token=self.do_token)
        return self._conn

    def get_droplets(self):
        droplets = []
        for droplet in self.conn.get_all_droplets():
            droplets.append(droplet)
        return droplets

    def get_uptime(self):
        r = []
        for droplet in self.get_droplets():
            r.append({'name': droplet.name(),
                      'created_at': droplet.created_at()})
        return r

    def get_ssh_key_fingerprint(self):
        r = []
        for droplet in self.get_droplets():
            r.append({'name': droplet.name(),
                      'ssh_key_fingerprint': droplet.ssh_keys()})
        return r


class DOChecks(CheckBase):
    def __init__(self, DO_TOKEN):
        self.c = DigitalOcean(DO_TOKEN)

    def check_uptime(self, max_uptime):
        hosts_violated =[]
        try:
            for i in self.c.get_uptime():
                # ts format: 2015-05-07T22:27:38Z
                if (i['created_at'] - datetime.utcnow()) > timedelta(hours=max_uptime):
                    hosts_violated.append(i)
        except:
            raise CoastguardAPIError
        return hosts_violated



