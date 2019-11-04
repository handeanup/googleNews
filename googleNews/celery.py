from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from news.models import News
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "googleNews.settings")
 
app = Celery("googleNews")
app.config_from_object("django.conf:settings")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'update-news-feed-every-single-minute': {
        'task': 'googleNews.tasks.update_news_feed',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}