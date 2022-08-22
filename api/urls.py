from django.urls import path, include
from .views import MovieViewSet,index, about, movies_index, movies_create, movies_json, movies_store
from rest_framework import routers


router = routers.DefaultRouter()
router.register('movies',MovieViewSet)

#http://dominio.com/api/movies -> get -> all
#http://dominio.com/api/movies -> post -> crear
#http://dominio.com/api/movies/1 -> get -> un elemento
#http://dominio.com/api/movies/1 -> put -> actualizar
#http://dominio.com/api/movies/1 -> delete -> eliminar


urlpatterns = [

    path('', include(router.urls)),

    path("hello", index),
    path("about", about),

    #path("movies", movies_index),
    #path("movies/create", movies_create),
    #path("movies/store", movies_store),

    path("json/movies", movies_json),
]