from django.urls import path
from . import views


views.index
urlpatterns = [
    path('', views.index)
]

