from . import views
from django.urls import path

app_name = 'Randomize'

urlpatterns = [
    path('', views.index, name='index'),
    path('submit', views.submit, name='submit')
]
