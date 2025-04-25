from allauth.account.adapter import DefaultAccountAdapter
from decouple import config

class CheckSignupsAllowedAccountAdapter(DefaultAccountAdapter):
    """
    Adapter to disable allauth new signups
    Used at equilang/settings.py with key ACCOUNT_ADAPTER

    """
    def is_open_for_signup(self, request):
        """
        Checks whether or not the site is open for signups.
        """
        allow_new_signups = config("ALLOW_NEW_SIGNUPS", default=False, cast=bool)
        return allow_new_signups
