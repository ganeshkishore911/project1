
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
from django.contrib.auth.models import User

class CookieJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        access_token = request.COOKIES.get("access_token")
        refresh_token=request.COOKIES.get("refresh_token")
        
        print("ALL COOKIES:", request.COOKIES)
        print("ACCESS TOKEN:", access_token)
        print("REFRESH TOKEN:", refresh_token)        
        try:
            validated_token=AccessToken(access_token)
        except Exception:
            if not refresh_token:
                raise AuthenticationFailed("Login again")
            
            try:
                refresh = RefreshToken(refresh_token)
                new_access_token=str(refresh.access_token)
                validated_token=AccessToken(new_access_token)
                request.new_access_token=new_access_token
            except Exception:
                raise AuthenticationFailed("Refresh token expired. Login again")

        user_id = validated_token["user_id"]
        user = User.objects.get(id=user_id)
        print("USER:", user)
        return (user, validated_token)
        