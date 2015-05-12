import digitalocean
from datetime import datetime, timedelta
from eval import *

DO_TOKEN = ''


class DigitalOcean(object):
    def __init__(self, do_token):
        self.do_token = do_token
        self._conn = None

    def conn(self):
        if not self._conn:
            self._conn = digitalocean.Manager(token=DO_TOKEN)
        return self._conn

    def get_droplet(self):
        droplets = []
        for droplet in self.conn.get_all_droplets():
            droplets.append(droplet)
        return droplets

    def get_uptime(self):
        r = []
        for droplet in self.get_droplet():
            r.append({'name': droplet.name(),
                      'created_at': droplet.created_at()})
        return r

    def get_ssh_key_fingerprint(self):
        r = []
        for droplet in self.get_droplet():
            r.append({'name': droplet.name(),
                      'ssh_key_fingerprint': droplet.ssh_keys()})
        return r


class DoChecks(CheckBase):
    @staticmethod
    def check_uptime(max_uptime):
        hosts_violated =[]
        c = DigitalOcean(DO_TOKEN)
        for i in c.get_uptime():
            # ts format: 2015-05-07T22:27:38Z
            if (i['created_at'] - datetime.utcnow()) > timedelta(hours=max_uptime):
                hosts_violated.append(i)
        return hosts_violated



