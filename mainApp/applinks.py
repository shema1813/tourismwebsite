from .views import homepage
from django.urls import path
from .views import loginpage
from .views import fetch_all_users_page
from .views import fetch_all_Movie_page
from  .views import update_one_movie
from.views import delet_one_players

urlpatterns = [
    path("homepage/", homepage, name="homepage") ,
    path("loginpage/",loginpage, name="loginpage") ,
    path("allplayerspage/" , fetch_all_users_page, name="allplayerspage") ,
    path("allmoviesspage/" , fetch_all_Movie_page, name="allmoviespage")  ,
     path("updateonemovie/<int:pk>" , update_one_movie, name="update_one_movie page") ,
     path("deleteoneplayer/<int:pk>" , delete_one_players, name="delete_one_players page") 
]


