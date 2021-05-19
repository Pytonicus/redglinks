from django.shortcuts import render, HttpResponse, redirect
from .models import Link, Sistema
import hashlib

def links(request):
    """ Devuelve los enlaces ya reducidos """

    if request.user.is_authenticated:
        links = Link.objects.all()
        links_list = []
        for link in links:
            enlace = link.enlace.encode('utf-8')
            enlace = hashlib.md5(enlace)
            links_list.append({
                "nombre": link.nombre,
                "sistema": link.sistema,
                "enlace": enlace.hexdigest()
            })

        return render(request, "links/index.html", {"links":links_list})
    else:
        return HttpResponse("<h1>ERROR 404</h1>")

def link_decript(request, link):
    """ Desencripta y redirige al enlace de descarga """
    enlaces = Link.objects.all()
    for enlace in enlaces:
        hash = enlace.enlace.encode('utf-8')
        hash = hashlib.md5(hash)

        print("HASH:")
        print(hash.hexdigest())
        if hash.hexdigest() == link:
            print("ENLACE ENCONTRADO:")
            print(enlace.enlace)
            url = enlace.enlace


    return redirect(url)