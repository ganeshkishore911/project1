from django.urls import path
from .views import Signup,Login,Logout,Profile,index

urlpatterns=[
    path("signup/",Signup.as_view(),name="signup"),
    path("login/",Login.as_view(),name="Login"),
    path("logout/",Logout.as_view(),name="Logout"),
    path("profile/",Profile.as_view(),name="Profile"),
    path("",index,name='index')
]