"""
URL configuration for evaluacion_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from evaluacion_1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('user/', views.user),

    path('libros/', views.libros),
    path('libros/later/', views.detalle_libro_1),
    path('libros/revival/', views.detalle_libro_2),
    path('libros/fairytale/', views.detalle_libro_3),

    path('peliculas/', views.peliculas),
    path('peliculas/theshinning/', views.detalle_pelicula_1),
    path('peliculas/nop/', views.detalle_pelicula_2),
    path('peliculas/thewhale/', views.detalle_pelicula_3),

    path('albums/', views.albums),
    path('albums/audioslave/', views.detalle_album_1),
    path('albums/mynameisearl/', views.detalle_album_2),
    path('albums/monument/', views.detalle_album_3),

    path('usuario/', views.user)

]
