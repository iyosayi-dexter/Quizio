import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class EmailActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.id) + six.text_type(user.email_verified) + six.text_type(timestamp))
