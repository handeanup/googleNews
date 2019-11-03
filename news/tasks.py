from django.template import Template, Context
from news.celery import app
import feedparser
from .models import News

@app.task
def update_news_feed():
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
            if News.objects.filter(guid = guid).count() == 0:
                n = News(title=title,
                link=link,
                guid=guid,
                source_title=source_title,
                source_link=source_link,
                desc=desc)
                n.save()

    except Exception as e:
        print(e)