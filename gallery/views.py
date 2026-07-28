from django.shortcuts import render, get_object_or_404
from gallery.models import Photograph

def index(request):
    
    photographs = Photograph.objects.order_by("-photograph_date").filter(published=True) # aapenas adicionar um - ao argumento passado em "order_by" para apresentar em ordem decrescente

    return render(request, 'gallery/index.html', {"cards": photographs})

def image(request, photo_id):
    photograph = get_object_or_404(Photograph, pk=photo_id)
    return render(request, 'gallery/image.html', {"photograph": photograph})