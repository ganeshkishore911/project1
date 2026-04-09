from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World")
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
        username=request.data.get("username")
        password=request.data.get("password")
        user=authenticate(username=username,password=password)
        if user is None:
            raise AuthenticationFailed("Invaild Credentials")
        refresh=RefreshToken.for_user(user)
        access_token=str(refresh.access_token)
        refresh_token=str(refresh)
        response=Response({
            "message":"Login Successful"
        },status=status.HTTP_200_OK)
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,secure=True,samesite='Strict'
        )
        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,secure=True,samesite="Strict"
        )
        return response
    
class Logout(APIView):
    def post(self,request):
        response=Response({
            "message":"Logout successfully"
        },status=status.HTTP_200_OK)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response
    
class Profile(APIView):
    def get(self,request):

        user=request.user
        return Response({
            "id":user.id,
            "username":user.username,"email":user.email,
        })
    
