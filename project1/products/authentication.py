from rest_framework.authentication import (BaseAuthentication)
from rest_framework_simplejwt.tokens import (AccessToken,RefreshToken)
from django.contrib.auth import (get_user_model)

User = get_user_model()


class CookieJWTAuthentication(BaseAuthentication):
    def authenticate(self,request):
        access_token = (request.COOKIES.get("access_token"))
        refresh_token = (request.COOKIES.get("refresh_token"))

        print("ALL COOKIES:",request.COOKIES)
        print("ACCESS TOKEN:",access_token)
        print("REFRESH TOKEN:",refresh_token)

        # no cookies -> anonymous user
        if (not access_token and not refresh_token):
            return None

        try:
            validated_token = (AccessToken(access_token))
        except Exception:
            # no refresh token
            if not refresh_token:
                return None

            try:
                refresh = RefreshToken(refresh_token)

                new_access_token = str(refresh.access_token)
                validated_token = (AccessToken(new_access_token))

                request.new_access_token = (new_access_token)
            except Exception:
                return None

        print(validated_token.payload)

        user_id = (validated_token.get("user_id"))

        if not user_id:
            return None
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

        print("USER:", user)

        return (user,validated_token)