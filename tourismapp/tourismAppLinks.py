from .views import homepage
from django.urls import path
from .views import loginpage
from .views import signuppage

urlpatterns = [
    path("homepage/", homepage, name="homepage") ,
    path("loginpage/", loginpage, name="loginpage" ) ,
    path("signuppage/", signuppage, name="signuppage" )
]