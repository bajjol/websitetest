from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse 
from django.shortcuts import render, redirect
from .forms import *

def merchandise(request):
	"""The merchandise page"""
	return render(request, 'merchandise.html')
	

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'merchandise.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'merchandise.html')

