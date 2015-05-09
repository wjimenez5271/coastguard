from datetime import datetime, timedelta

class CheckBase(object):
    def __init__(self):
        pass

    def check_uptime(self, max_uptime):
        raise NotImplementedError
