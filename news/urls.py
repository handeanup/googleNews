from django.urls import path
from .views import NewsHome

urlpatterns = [
    path('', NewsHome),
]