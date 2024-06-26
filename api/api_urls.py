from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views_api

router = DefaultRouter()
router.register(r'chercheurs', views_api.ChercheurViewSet)
router.register(r'projets', views_api.ProjetDeRechercheViewSet)
router.register(r'publications', views_api.PublicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]