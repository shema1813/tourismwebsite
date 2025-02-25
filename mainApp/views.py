from django.shortcuts import render
from django.http import HttpResponse
from .models import player
from .models import Movie 
from django.shortcuts import redirect
#H
# Create your views here.
def homepage(request):
    return HttpResponse ("hello from python")

def loginpage(request):
    print("you did a"+request.method)
    if request.method == "POST":
        print(request.POST)
        typedname = request.POST.get("username")
        print("the name you typed is :" + typedname)
        typedpassword =request.POST.get("password")
        print(typedpassword)
        new_player = player(username = typedname,password = typedpassword)
        new_player.save()
    return render(request,"login.html")

def fetch_all_users_page(request):
    all_players = player.objects.all()
    return render(request, "all_players.html", {"all_players" :all_players})
 
def fetch_all_Movie_page(request):
    all_Movie = Movie.objects.all()
    return render(request, "all_Movie.html", {"all_Movie" :all_Movie})

def update_one_movie(request, pk):
    single_movie = Movie.objects.get( pk=pk )
    return render(request,
                  "update_one_movie.html",
                  {"single_movie": single_movie})

from django.shortcuts import redirect
def delete_one_players(request , pk) :
    single_player = player.objects.get(pk=pk)
    single_player.delete()
    return redirect("homepage")