from django.shortcuts import render, redirect
from backend_app.models import UploadImage
from .forms import UploadImageForm
from Scanner.Segmentor import Segment 

import cv2 as cv

def index(request): 

    if request.method == 'POST': 
        form = UploadImageForm(request.POST, request.FILES) 
        if form.is_valid(): 

            form.save() 
            img = UploadImage.objects.last()
            image = cv.imread('.'+img.image.url, cv.IMREAD_UNCHANGED)
            text = Segment(image)
            return render(request, 'result.html', {'img_url' : img.image.url, 'text' : text} ) 
    else: 
        form = UploadImageForm() 
    return render(request, 'index.html', {'form' : form}) 


def about(request):
    return render(request, 'about.html')

