from traitlets import Unicode

from tornado.concurrent import run_on_executor
from jupyterhub.auth import PAMAuthenticator


class PassThroughAuthenticator(PAMAuthenticator):
    guest_user = Unicode(
        "guest",
        help="""
        Guest account to use when logging in to jupyterhub. This account will not require any authentication
        hence use it wisely. All the terminal access and directory will be used for the specified machine user
        and the account must be present beforehand.
        """,
        config=True
    )

    @run_on_executor
    def authenticate(self, handler, data):
        if data is None:
            return self.guest_user
        else:
            return super(PAMAuthenticator, self).authenticate(handler, data)
