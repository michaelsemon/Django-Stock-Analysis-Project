#New File (routing from urls.py from stockanalysis)

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
]
