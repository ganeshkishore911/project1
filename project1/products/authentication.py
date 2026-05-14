
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User

class CookieJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        access_token = request.COOKIES.get("access_token")
        
        # print("ALL COOKIES:", request.COOKIES)     
        # print("ACCESS TOKEN:", access_token)          

        if not access_token:
            return None
        try:
            validated_token = AccessToken(access_token)
            user_id = validated_token["user_id"]
            user = User.objects.get(id=user_id)
            # print("USER FOUND:", user)               
            return (user, validated_token)
        except Exception as e:
            print("AUTH ERROR:", e)                   
            raise AuthenticationFailed("Invalid or expired token")