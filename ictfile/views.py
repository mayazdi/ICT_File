from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm


def handle_uploaded_file(f):
    print(f.path)
    with open('files/name.mp4', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# Create your views here.
def default(request):
    return render(request, 'index.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def success(request):
    return render(request, 'success.html')
