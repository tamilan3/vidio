from django.shortcuts import render
from vidioapp.models import vidiouploader
def index(request):
    vidio=vidiouploader.objects
    return render(request,"vidioapp/1.html",context={"vidio":vidio})
# Create your views here.
