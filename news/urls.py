from django.urls import path
from .views import NewsHome,UpdateDatabase

urlpatterns = [
    path('', NewsHome),
    path('update/',UpdateDatabase),
]