from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions, HTTP_HEADER_ENCODING
from django.contrib.auth.hashers import check_password
from django.utils.six import text_type

from models import Device
import pprint


def get_authorization_header(request):
    """
    Return request's 'Authorization:' header, as a bytestring.
    """

    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, text_type):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


class DeviceAuthenticationBackend(authentication.TokenAuthentication):
    keyword = 'api_key'

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        try:
            device = Device.objects.get(api_key=key)
            device.is_authenticated = True
            return (device, None)
        except Device.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')
