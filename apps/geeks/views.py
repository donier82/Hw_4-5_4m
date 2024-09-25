from django.shortcuts import render

from .models import Settings, News

# Create your views here.
def index(request):
   
    settings = Settings.objects.latest('id')
    news=News.objects.latest('id')
    return render(request, 'index.html', locals())

