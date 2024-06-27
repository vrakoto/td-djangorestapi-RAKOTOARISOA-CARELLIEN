from django.shortcuts import render
# import io
# import base64
# import matplotlib.pyplot as plt
# import seaborn as sns
# from django.http import JsonResponse
from rest_framework.decorators import api_view
# from .models import Chercheur, ProjetDeRecherche, Publication

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'api/index.html')

def chercheurs(request):
    return render(request, 'api/chercheurs.html')

def projets(request):
    return render(request, 'api/projets.html')

def publications(request):
    return render(request, 'api/publications.html')


# @api_view(['GET'])
# def generate_graph(request):
#     start_date = request.GET.get('startDate')
#     end_date = request.GET.get('endDate')
#     specialty = request.GET.get('specialty')
#     graph_type = request.GET.get('graphType')

#     # Récupérer les données en fonction des filtres
#     if specialty:
#         chercheurs = Chercheur.objects.filter(specialite=specialty)
#     else:
#         chercheurs = Chercheur.objects.all()

#     if start_date and end_date:
#         projets = ProjetDeRecherche.objects.filter(date_debut__gte=start_date, date_fin_prevue__lte=end_date)
#         publications = Publication.objects.filter(date_publication__gte=start_date, date_publication__lte=end_date)
#     else:
#         projets = ProjetDeRecherche.objects.all()
#         publications = Publication.objects.all()

#     # Générer le graphique en fonction du type spécifié
#     plt.figure(figsize=(8, 6))
#     if graph_type == 'bar':
#         # Générer un graphique à barres
#         data = [len(projets), len(publications)]
#         labels = ['Projets', 'Publications']
#         sns.barplot(x=labels, y=data)
#         plt.title('Nombre de projets et publications')
#     elif graph_type == 'pie':
#         # Générer un graphique en secteurs
#         data = [len(projets), len(publications)]
#         labels = ['Projets', 'Publications']
#         plt.pie(data, labels=labels, autopct='%1.1f%%')
#         plt.title('Répartition des projets et publications')
#     else:
#         # Générer un graphique en courbe par défaut
#         data = {
#             'Projets': [len(ProjetDeRecherche.objects.filter(date_debut__year=year)) for year in range(2010, 2023)],
#             'Publications': [len(Publication.objects.filter(date_publication__year=year)) for year in range(2010, 2023)]
#         }
#         sns.lineplot(data=data)
#         plt.title('Évolution des projets et publications au fil des années')

#     # Convertir le graphique en image base64
#     buffer = io.BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

#     # Retourner les données du graphique en JSON
#     return JsonResponse({'graphData': image_base64})