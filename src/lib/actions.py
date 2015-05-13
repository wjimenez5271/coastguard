from exceptions import *


class Actions(object):
    def terminate_instance(self):
        raise NotImplementedError

    def alert(self, subject, message, mail_sender, mail_recipient, mail_server, timeout=5, start_tls=False):
        raise NotImplementedError


class NotificationActions(Actions):
    def terminate_instance(self):
        raise NotImplementedError

    @staticmethod
    def alert(subject, message, mail_sender, mail_recipient, mail_server, timeout=5, start_tls=False):
        import smtplib
        """
        Alert user via email
        """
        try:
            smtpObj = smtplib.SMTP(mail_server, timeout)
            if start_tls:
                smtpObj.starttls()
            sender = mail_sender
            message = "From: %s \nTo: %s \nSubject: %s\n \n%s" % (sender, mail_recipient, subject, message)
            smtpObj.sendmail(sender, [mail_recipient], message)
        except Exception as e:
            raise CoastguardSendEmailError(e)
