from django.contrib import admin
from .models import PoliticalParty, UserCustom, Candidate

admin.site.register(PoliticalParty)

admin.site.register(UserCustom)

admin.site.register(Candidate)
