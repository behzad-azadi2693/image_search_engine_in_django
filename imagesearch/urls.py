from django.urls import path
from .views import image_search


urlpatterns = [
    path('', image_search),
]