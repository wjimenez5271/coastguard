import digitalocean
from eval import *
from util import *
import dateutil.parser
import dateutil.relativedelta
from datetime import *
from dateutil.relativedelta import *
import logging
from actions import *

log = logging.getLogger('coastguard')


class CG_DigitalOcean(object):
    """
    This class encompasses everything relating to the DO API
    """
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
    """
    Implementation of the CheckBase object for Digital Ocean
    """
    def __init__(self, hostFilter, DO_TOKEN):
        super(DOChecks, self).__init__(hostFilter)
        if DO_TOKEN is None:
            raise MissingAuthException
        self.c = digitalocean.Manager(token=DO_TOKEN)

    def eval_delta(self, date1, date2, max_uptime):
        """
        Compare the date/time stamps and determine if the instance has violated threshold. Expects like TZ
        :param date1: datetime obj. first date/time to compare
        :param date2: datetime obj. second date/time to compare
        :param max_uptime: int. max uptime in hours
        :return: bool. True if it has violated, False if not.
        """
        diff = relativedelta(date1, date2)
        age_in_hours = abs((diff.days * 24) + diff.hours)
        if not age_in_hours <= max_uptime:
            log.debug('instance has been online for {0} hours. threshold {1} hours'.format(
                age_in_hours, max_uptime))
            return True
        else:
            return False

    def check_uptime(self, max_uptime):
        """
        Evaluate the uptime of a digital ocean instance
        :param max_uptime: int. Uptime threshold in hours
        :return: lst. hosts violating `max_uptime`.
        """
        hosts_violated = []
        droplets = self.hostFilter.filter(self.c.get_all_droplets(), 'name')
        for i in droplets:
            log.debug('checking uptime of instance {0}'.format(i))
            # ts format from digital ocean api: 2015-05-07T22:27:38Z
            created_at = i.created_at
            log.debug('instance {0} was created at {1}'.format(i, created_at))
            # slice off last char of time stamp to make it timezone unaware.
            created_at = dateutil.parser.parse(created_at[:-1])
            if self.eval_delta(created_at,datetime.utcnow(), max_uptime):
                hosts_violated.append(i)
        return hosts_violated

class DOActions(Actions):
    def __init__(self, DO_TOKEN):
        if DO_TOKEN is None:
            raise MissingAuthException
        self.c = CG_DigitalOcean(DO_TOKEN)

    def terminate_instance(self, droplet_id):
        d = self.c.get_droplet(droplet_id)
        d.shutdown()
