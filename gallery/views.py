from django.shortcuts import render

def index(request):
    
    data = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "webbtelescope.org / NADA / James Webb"},
        2: {"nome": "Galáxia NGC 1079",
            "legenda": "nasa.org / NASA / Hubble"}
        }

    return render(request, 'gallery/index.html', {"cards": data})

def image(request):
    return render(request, 'gallery/image.html')