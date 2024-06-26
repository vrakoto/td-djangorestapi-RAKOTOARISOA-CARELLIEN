from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Chercheur, ProjetDeRecherche, Publication
from .serializers import ChercheurSerializer, ProjetDeRechercheSerializer, PublicationSerializer

class ChercheurViewSet(viewsets.ModelViewSet):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer
    permission_classes = [IsAuthenticated]

class ProjetDeRechercheViewSet(viewsets.ModelViewSet):
    queryset = ProjetDeRecherche.objects.all()
    serializer_class = ProjetDeRechercheSerializer
    permission_classes = [IsAuthenticated]

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [IsAuthenticated]
