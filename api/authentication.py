from django.utils.timezone import now
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from djangoProject.settings import TOKEN_EXPIRE_SECONDS


class TokenAuthenticationExpired(TokenAuthentication):
    """
    A custom TokenAuthenticationExpired exception will be raised if the token is expired.
    created for user safety
    """

    def authenticate(self, request) -> object:
        result = super().authenticate(request)
        if result is None:  # if token not found, returning none
            return None

        user, token = result
        if (
                now() - token.created).total_seconds() > TOKEN_EXPIRE_SECONDS:  # if token time has expired, telling
            # this our user
            token.delete()
            raise AuthenticationFailed('Token is expired, please request a new one')

        return user, token
