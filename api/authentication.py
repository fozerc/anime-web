from django.template.defaulttags import now
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from djangoProject.settings import TOKEN_EXPIRE_SECONDS


class TokenAuthenticationExpired(TokenAuthentication):
    def authenticate(self, request):
        try:
            user, token = super().authenticate(request)
        except TypeError:
            return
        if (now() - token.created) > TOKEN_EXPIRE_SECONDS:
            token.delete()
            return AuthenticationFailed('token is expired, please take a new one')
        return user, token
