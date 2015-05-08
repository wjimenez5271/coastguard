import digitalocean

DO_TOKEN = ''
uptime_threshold = ''


class DO(object):
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