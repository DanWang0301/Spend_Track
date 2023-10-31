from django.shortcuts import render
from Track.models import *

# Create your views here.

def display(request):
    Post = TrackRecord.objects.all()
    return render(request, "track_page/track_detail.html", {"post":Post})

def insert(request):
    if request.method == 'POST':
        Track_Type = request.Post['Track_Type']
        Credit_Card = request.Post['Spend_Type']
        Track_Amount = request.Post['Amount']
        Track_Detail = request.Post['Detail']
        Track_Date = request.Post['Date']

def update(request):
    if request.method == 'POST':
        Track_Type = request.Post['Track_Type']
        Credit_Card = request.Post['Spend_Type']
        Track_Amount = request.Post['Amount']
        Track_Detail = request.Post['Detail']
        Track_Date = request.Post['Date']

def select(request):
    pass

def delete(request):
    if request.method == 'POST':
        Track_Type = request.Post['Track_Type']
        Credit_Card = request.Post['Spend_Type']
        Track_Amount = request.Post['Amount']
        Track_Detail = request.Post['Detail']
        Track_Date = request.Post['Date']