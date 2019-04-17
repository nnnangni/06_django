from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

# Create your views here.
def list(request):
    movies = Movie.objects.all()
    return render(request, "movie/list.html",{"movies":movies})
    
def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:list")
        else:
            form = MovieForm()
    else:
        form = MovieForm()
    return render(request, 'movie/form.html', {"form":form})
    
def detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'movie/detail.html', {'movie':movie})

def update(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movies:list")
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie/form.html',{'form':form})
    
def delete(request,id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect("movies:list")