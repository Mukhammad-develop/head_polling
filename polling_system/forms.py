from django import forms
from .models import *


class PoliticalPartyForm(forms.ModelForm):
    class Meta:
        model = PoliticalParty
        fields = '__all__'


class UserCustomForm(forms.ModelForm):
    class Meta:
        model = UserCustom
        fields = '__all__'


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = '__all__'


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'
