import json
import os
from django.shortcuts import render
from django.conf import settings

def index(request):
    return render(request, 'templates/index.html' )

def usuario(request):
    return render(request, 'templates/usuario.html')

def libros(request):
    data = {
        "title": "Libros",
        "titulo": "Libros",
        "foto1": "later.jpeg",
        "producto1": "Later",
        "url_1": "later",
        "foto2": "revival.jpeg",
        "producto2": "Revival",
        "url_2": "revival",
        "foto3": "tale.jpeg",
        "producto3": "Fairy Tale",
        "url_3": "fairytale"
    }
    return render(request, 'templates/producto.html', data)


def peliculas(request):
    data = {
        "title": "Peliculas",
        "titulo": "Peliculas",
        "foto1": "theShining.jpeg",
        "producto1": "The Shinning",
        "url_1": "theshinning",
        "foto2": "nop.jpeg",
        "producto2": "¡NOP!",
        "url_2": "nop",
        "foto3": "theWhale.jpeg",
        "producto3": "The Whale",
        "url_3": "thewhale"
    }
    return render(request, 'templates/producto.html', data)

def albums(request):
    data = {
        "title": "Albums",
        "titulo": "Albums Musicales",
        "foto1": "audioslave.jpeg",
        "producto1": "audioslave",
        "url_1": "audioslave",
        "foto2": "mynameisearl.jpeg",
        "producto2": "My Name Is Earl",
        "url_2": "mynameisearl",
        "foto3": "monument.jpeg",
        "producto3": "Monument",
        "url_3": "monument"
    }
    return render(request, 'templates/producto.html', data)



# vista detalle libros
def detalle_libro_1(request):
    data = {
    "title": "Later",
    "titulo": "Later",
    "anio": "Año: 2021",
    "elem_1": "Autor: Stephen King",
    "elem_2": "Puntuación: 4.5/5 (Amazon)",
    "foto1": "later.jpeg",
    "elem_3": "Descripcion: Later es una novela de crimen y horror que sigue a Jamie Conklin, un joven con la habilidad de ver y hablar con los muertos. Su madre, una madre soltera con dificultades, le insta a mantener este don en secreto. Sin embargo, cuando un detective de la NYPD lo involucra en la búsqueda de un asesino que ha amenazado con volver de entre los muertos, Jamie descubre que su habilidad especial viene con un costo."
    }


    return render(request, 'templates/detalle.html', data )


def detalle_libro_2(request):
    data = {
    "title": "Revival",
    "titulo": "Revival",
    "anio": "Año: 2014",
    "elem_1": "Autor: Stephen King",
    "elem_2": "Puntuación: 4.2/5 (Amazon)",
    "foto1": "revival.jpeg",
    "elem_3": "Descripcion: Revival es una novela oscura y electrificante sobre la adicción, el fanatismo y lo que podría existir al otro lado de la vida. La historia se desarrolla en una pequeña ciudad de Nueva Inglaterra, donde un ministro recién llegado causa una impresión indeleble en un joven llamado Jamie Morton. A lo largo de cinco décadas, Jamie y el ministro Charles Jacobs se cruzan en una serie de encuentros que alteran la vida, con resultados aterradores."
    }


    return render(request, 'templates/detalle.html', data )


def detalle_libro_3(request):
    data = {
    "title": "Fairy Tale",
    "titulo": "Fairy Tale",
    "anio": "Año: 2022",
    "elem_1": "Autor: Stephen King",
    "elem_2": "Críticas: 4.13/5 (Goodreads)",
    "foto1": "tale.jpeg",
    "elem_3": "Descripcion: Fairy Tale es una novela de fantasía oscura que sigue a Charlie Reade, un joven de 17 años que hereda llaves a un reino oculto y sobrenatural, y se encuentra liderando la batalla entre las fuerzas del bien y del mal. La historia transcurre en un universo paralelo lleno de princesas y príncipes exiliados, castigos horribles, y una lucha a muerte en juegos mortales para el entretenimiento de la 'Fair One', con un reloj de sol mágico que puede revertir el tiempo como uno de los elementos centrales del relato."
    }

    return render(request, 'templates/detalle.html', data )






# vistas para detalle peliculas

def detalle_pelicula_1(request):
    data = {
        "title": "The Shining",
        "titulo": "The Shining",
        "anio": "Año: 1980",
        "elem_1": "Director: Stanley Kubrick",
        "elem_2": "Puntuacion: 8.4/10 (IMDb)",
        "elem_3": "Descripcion: The Shining es una película de terror psicológico que sigue a Jack Torrance, un escritor en recuperación del alcoholismo, quien acepta un trabajo como cuidador del histórico Hotel Overlook durante el invierno. Sin embargo, pronto es acosado por fuerzas sobrenaturales malignas presentes en el hotel, lo que lo lleva a una espiral descendente hacia la locura y la violencia, mientras su hijo, que tiene habilidades psíquicas, ve visiones horripilantes del pasado y del futuro del hotel",
        "foto1": "theShining.jpeg",
    }
    return render(request, 'templates/detalle.html', data)




def detalle_pelicula_2(request):
    data = {
    "title": "Nope",
    "titulo": "Nope",
    "anio": "Año: 2022",
    "elem_1": "Director: Jordan Peele",
    "elem_2": "Puntuacion: 6.8/10 (IMDb)",
    "elem_3": "Descripcion: Nope es una película de terror neo-occidental y ciencia ficción que sigue a los residentes de un solitario barranco en California, quienes son testigos de un descubrimiento inquietante y escalofriante. La trama se centra en dos hermanos interpretados por Daniel Kaluuya y Keke Palmer, quienes encuentran un OVNI depredador mientras intentan capturarlo. La película también explora la moderna fascinación por el espectáculo y cómo representa los peligros de la fama a través del personaje de Steven Yeun, Jupe.",
    "foto1": "nop.jpeg",
    }   

    return render(request, 'templates/detalle.html', data)

def detalle_pelicula_3(request):
    data = {
    "title": "The Whale",
    "titulo": "The Whale",
    "anio": "Año: 2022",
    "elem_1": "Director: Darren Aronofsky",
    "elem_2": "Puntuacion: 7.7/10 (IMDb)",
    "elem_3": "Descripcion: The Whale es un drama psicológico que sigue a un profesor de inglés recluido con obesidad mórbida que intenta restaurar su relación con su hija adolescente. La película explora temas como el abandono, la pérdida, las familias rotas, la sexualidad y la necesidad de conexión. Esta película fue dirigida por Darren Aronofsky y escrita por Samuel D. Hunter, basada en su obra de teatro de 2012 con el mismo nombre. Brendan Fraser, Sadie Sink, Hong Chau, Ty Simpkins y Samantha Morton son los protagonistas. The Whale se estrenó en el 79° Festival Internacional de Cine de Venecia el 4 de septiembre de 2022, y tuvo un lanzamiento limitado en cines en los Estados Unidos el 9 de diciembre, seguido de un lanzamiento amplio el 21 de diciembre, por A24.",
    "foto1": "theWhale.jpeg",
    }

    return render(request, 'templates/detalle.html', data)





# vistas para albums musicales
def detalle_album_1(request):
    data = {
    "title": "Audioslave",
    "titulo": "Audioslave",
    "anio": "Año: 2002",
    "elem_1": "Banda: Audioslave",
    "elem_2": "Genero: Hard Rock, Alternative Rock, Post-Grunge",
    "elem_3": "Sello Discografico: Epic Records, Interscope Records",
    "foto1": "audioslave.jpeg",
}


    return render(request, 'templates/detalle.html', data)

def detalle_album_2(request):
    data = {
    "title": "My Name Is Earl",
    "titulo": "My Name Is Earl",
    "anio": "Año: 2017",
    "elem_1": "Banda: Earl St. Clair",
    "elem_2": "Genero: R&B/Soul",
    "elem_3": "Sello Discografico: Def Jam Recordings",
    "foto1": "mynameisearl.jpeg",
    }


    return render(request, 'templates/detalle.html', data)

def detalle_album_3(request):
    data = {
    "title": "Monument",
    "titulo": "Monument",
    "anio": "Año: 2021",
    "elem_1": "Banda: Portico Quartet",
    "elem_2": "Genero: Jazz, Electronica",
    "elem_3": "Sello Discografico: Gondwana Records",
    "foto1": "monument.jpeg",
    }

    return render(request, 'templates/detalle.html', data)


def user(request):
    data = {
        "title": "Usuario",
        "titulo": "Usuario",
        "nombre": "Diego Obreque Molina",
        "email": "diego.obreque05@inacapmail.cl",
        "carrera": "Analista Programador",
        "sede": "Temuco",
        "foto1": "user.jpeg"
    }
    return render(request, 'templates/usuario.html', data)