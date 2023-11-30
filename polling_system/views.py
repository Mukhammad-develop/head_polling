from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import PollForm


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


def party_list(request):
    party = PoliticalParty.objects.all()
    context = {'party': party}
    return render(request, 'party_list.html', context)


def party_detail(request, id):
    party = get_object_or_404(PoliticalParty, pk=id)
    context = {'party': party}
    return render(request, 'party_detail.html', context)


def poll_add(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
        else:
            return render(request, 'poll_add.html', {'form': form})
    else:
        form = PollForm()
        return render(request, 'poll_add.html', {'form': form})
