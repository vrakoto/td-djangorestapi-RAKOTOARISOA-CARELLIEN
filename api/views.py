from django.shortcuts import render

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
