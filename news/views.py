from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def NewsHome(request):
    objs = News.objects.all()
    return render(request, 'news.html', context={'name':'Google News','data':objs}) 
