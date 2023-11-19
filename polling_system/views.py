from django.shortcuts import render
from .models import *


def index(request):
    # Fetch data for the index page, such as political parties and polls
    political_parties = PoliticalParty.objects.all()
    polls = Poll.objects.all()

    # Pass the data to the template
    context = {
        'political_parties': political_parties,
        'polls': polls,
    }

    # Render the index page with the provided data
    return render(request, 'main.html', context)
