from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class Signup(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data,partial=True) #its allow the missing fields like a email
        if serializer.is_valid():
            user=serializer.save()
            refresh=RefreshToken.for_user(user)
            access_token=str(refresh.access_token) # access_token is property to get the access token from refresh token
            refresh_token=str(refresh)
            response = Response({
                "user": serializer.data
            }, status=status.HTTP_201_CREATED)
            # set the access token in cookie  with https for secure
            response.set_cookie(key="access_token",value=access_token,
                                httponly=True,secure=True,samesite='Strict')
            # set the refresh token in cookie 
            response.set_cookie(key="refresh_token",value=refresh_token,httponly=True,secure=True,samesite="Strict")
            return response
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class Login(APIView):
    def post(self,request):
        pass