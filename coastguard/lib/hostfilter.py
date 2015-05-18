import re
import logging

log = logging.getLogger('coastguard')


def createRe(l):
    if not l or len(l) == 0:
        return None
    l = [x.strip() for x in l if x] # Remove empty items and whitespace
    reText = "(" + ")|(".join(l) + ")"
    return re.compile(reText, re.I)

'''
Filter hosts given a set of regexes and host names. The filter takes a set of
regexes in a whitelist and another set as a blacklist.

Hostnames are only denied if they match an item in the blacklist and do not match
any items in the whitelist.
'''


class HostFilter(object):
    def __init__(self, whitelist, blacklist):
        self.whitelist = createRe(whitelist)
        self.blacklist = createRe(blacklist)
        self.hostCache = {}

    @staticmethod
    def fromConfig(parser, section="hostfilter"):
        whitelist = None
        blackilst = None
        if parser.has_section(section):
            whitelist = parser.get(section, 'whitelist').splitlines()
            blacklist = parser.get(section, 'blacklist').splitlines()
        return HostFilter(whitelist, blacklist)

    def allowed(self, host, attributeName=None):
        '''Check if a hostname is allowed. Hosts are cached for better performance on
        susequent lookups.'''
        if attributeName:
            host = getattr(host, attributeName)

        if host in self.hostCache:
            return self.hostCache[host]

        value = self._check(host)
        self.hostCache[host] = value
        return value

    def filter(self, hostList, attributeName=None):
        return [host for host in hostList if self.allowed(host, attributeName)]

    def _check(self, hostname):
        '''Check if a hostname is allowed. This internal function does not use the
        cache.'''
        # Matched the whitelist, so it's allowed.
        if self.whitelist and self.whitelist.match(hostname):
            log.debug("hostfilter: %s permitted by whitelist", hostname)
            return True

        # Matched the blacklist and not the whitelist.
        if self.blacklist and self.blacklist.match(hostname):
            log.debug("hostfilter: %s denied by blacklist", hostname)
            return False

        # Matched neither, so it's allowed
        log.debug("hostfilter: %s permitted due to no match", hostname)
        return True
