from django.shortcuts import render, get_object_or_404
from gallery.models import Photograph

def index(request):
    
    photographs = Photograph.objects.order_by("-photograph_date").filter(published=True) # apenas adicionar um - ao argumento passado em "order_by" para apresentar em ordem decrescente

    return render(request, 'gallery/index.html', {"cards": photographs})

def image(request, photo_id):
    photograph = get_object_or_404(Photograph, pk=photo_id)
    return render(request, 'gallery/image.html', {"photograph": photograph})

def search(request):
    photographs = Photograph.objects.order_by("-photograph_date").filter(published=True)

    if 'search' in request.GET: # vê se tem a palavra na url
        searched_name = request.GET['search']
        if searched_name:
            photographs = photographs.filter(name__icontains=searched_name) # diferencia acento. Portanto não retorna quando diferente

    return render(request, 'gallery/search.html', {"cards": photographs})