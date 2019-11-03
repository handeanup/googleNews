from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def NewsHome(request):
    objs = News.objects.all()
    '''return HttpResponse('hello')'''
    return render(request, 'news.html', context={'name':'Anup','data':objs}) 
