class CheckBase(object):
    def __init__(self, hostFilter):
        self.hostFilter = hostFilter

    def check_uptime(self, max_uptime):
        raise NotImplementedError
