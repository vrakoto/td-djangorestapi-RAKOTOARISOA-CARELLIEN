from django.urls import path
from . import views
# from .views import generate_graph

urlpatterns = [
    path('', views.index, name='index'),
    path('chercheurs/', views.chercheurs, name='chercheurs'),
    path('projets/', views.projets, name='projets'),
    path('publications/', views.publications, name='publications'),
    path('login/', views.login, name='login'),
    # path('generate-graph/', generate_graph, name='generate_graph'),
]