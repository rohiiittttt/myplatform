import jwt
from django.conf import settings
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')

        if not token:
            raise exceptions.AuthenticationFailed('No token provided')

        try:
            token = token.split(' ')[1]  # Get the token part from 'Bearer <token>'
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token')

        user = User.objects.filter(id=payload['user_id']).first()
        if not user:
            raise exceptions.AuthenticationFailed('User not found')

        return (user, token)
