from django.shortcuts import render
from django.http import HttpResponse
import feedparser

def NewsHome(request):
    try:
        google_news_feed_url = 'https://news.google.com/rss/search?pz=1&cf=all&q=nse$&hl=en-IN&gl=IN&ceid=IN:en'
        news_feed = feedparser.parse(google_news_feed_url)
        for feed in news_feed.entries:
            title = feed.title.encode("utf-8")
            link = feed.link.encode("utf-8")
            guid = feed.guid
            source_title = feed.source["title"]
            source_link = feed.source["href"]
            desc = feed.description.encode("utf-8")
    except Exception as e:
        print(e)
    return HttpResponse("Hello") 
