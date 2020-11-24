from django.shortcuts import render
from .models import Card

# Create your views here.
def main(request):

    cards = Card.objects.all()

    return render(request, 'index.html', {'cards': cards})
