from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.


def home(request):
    return render(request, 'Home.html')

def form(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'fileform.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'fileform.html')


