from django.shortcuts import render
from django.http import HttpResponse
from .models import News
import feedparser

def NewsHome(request):
    objs = News.objects.all()
    return render(request, 'news.html', context={'name':'Google News','data':objs}) 

def UpdateDatabase(request):
    google_news_feed_url = 'https://news.google.com/rss/search?pz=1&cf=all&q=nse$&hl=en-IN&gl=IN&ceid=IN:en'
    news_feed = feedparser.parse(google_news_feed_url)
    for feed in news_feed.entries:
        title = feed.title.encode("utf-8")
        link = feed.link.encode("utf-8")
        guid = feed.guid
        source_title = feed.source["title"]
        source_link = feed.source["href"]
        description = feed.description.encode("utf-8")
        if News.objects.filter(guid = guid).count() == 0:
            n = News(title=title.decode('utf-8'),
            link=link.decode('utf-8'),
            guid=guid,
            source_title=source_title,
            source_link=source_link,
            description=description)
            n.save()
    objs = News.objects.all()
    return render(request, 'news.html', context={'name':'Google News','data':objs})