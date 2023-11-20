from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    political_parties = PoliticalParty.objects.all()
    polls = Poll.objects.all()
    candidates = Candidate.objects.all()
    votes = Vote.objects.all()

    context = {
        'political_parties': political_parties,
        'polls': polls,
        'candidates': candidates,
        'votes': votes,
    }

    return render(request, 'main.html', context)


def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    context = {'poll': poll}
    return render(request, 'poll_detail.html', context)


def poll_list(request):
    polls = Poll.objects.all()

    context = {'polls': polls}
    return render(request, 'poll_list.html', context)


def candidate_list(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}
    return render(request, 'candidate_list.html', context)


def candidate_detail(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    context = {'candidate': candidate}
    return render(request, 'candidate_detail.html', context)
