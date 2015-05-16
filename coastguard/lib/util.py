class CoastguardSendEmailError(Exception):
    """
    Coastguard is unable to send email
    """

class CoastguardAPIError(Exception):
    """
    Generic exception communicating with a 3rd party API
    """

class MissingAuthException(Exception):
    """
    Missing needed authentication token
    """

class CoastguardException(Exception):
    """
    Generic exception
    """
