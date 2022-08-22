from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Movie
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework import serializers, viewsets

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo")

def about(request):
    return HttpResponse("About")

def movies_index(request):
    movies = Movie.objects.all() #lista de peliculas - select * from api_movies
    return render(request, "movies/index.html/", {'ad':"Hi everyone", 'lista': movies})

def movies_create(request):
    return render(request, "movies/create.html/")

def movies_store(request):
    print(request.POST)
    print(request.FILES)

    if 'image' in request.FILES:

        imagen=request.FILES['image']

        path = default_storage.save("posters/" + imagen.name, ContentFile(imagen.read()))

        print(path)

    #print(request.POST["nombre"])

    #movie = Movie()#guardar el nombre de las peliculas
    #movie.name = request.POST["nombre"]
    #movie.save()

    return HttpResponse("Guardar Película")

def movies_json(request):
    movies = Movie.objects.select_related('gender').all()

    json_movies = []
    for o in movies:
        movie = {
            "id": o.id,
            "title": o.name,
            "gender": o.gender.name if o.gender else '-'
        }
        json_movies.append(movie)

    return JsonResponse(json_movies, safe = False)#envia datos serializados 

class MovieSerializer(serializers.ModelSerializer):
    gender_name = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()

    def get_gender_name(self, obj):
        return obj.gender.name if obj.gender else None

    def get_actors(self, obj):
        return [x.name for x in obj.actor.all()]

    class Meta:
        model = Movie
        fields = ['id','name','poster','gender_name','actors']

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer