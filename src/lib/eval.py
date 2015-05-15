class CheckBase(object):
    def __init__(self):
        raise NotImplementedError

    def check_uptime(self, max_uptime):
        raise NotImplementedError
