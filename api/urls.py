from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chercheurs/', views.chercheurs, name='chercheurs'),
    path('projets/', views.projets, name='projets'),
    path('publications/', views.publications, name='publications'),
    path('login/', views.login, name='login')
]