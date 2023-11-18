from django.db import models
from django.contrib.auth.models import AbstractUser


class PoliticalParty(models.Model):
    title = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='media/', null=True, blank=True)
    leader = models.OneToOneField('polling_system.Candidate', on_delete=models.SET_NULL, null=True, blank=True)
    ideology = models.TextField()
    year_founded = models.PositiveIntegerField()
    headquarters_location = models.CharField(max_length=255)
    motto_or_slogan = models.CharField(max_length=255)
    manifesto = models.TextField()
    current_seats_held = models.PositiveIntegerField(default=0)
    historical_performance = models.TextField()
    campaign_focus = models.TextField()
    social_media_links = models.URLField(max_length=255, blank=True, null=True)
    contact_information = models.TextField()
    affiliated_organizations = models.TextField()
    previous_election_results = models.TextField()
    coalition_partners = models.TextField(blank=True, null=True)
    international_affiliations = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class UserCustom(AbstractUser):
    first_name = models.CharField(max_length=75)
    family_name = models.CharField(max_length=75, null=True, blank=True)
    fathers_name = models.CharField(max_length=75, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=15, blank=True)
    is_candidate = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.family_name} {self.fathers_name}'


class Candidate(models.Model):
    user = models.OneToOneField(UserCustom, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to='media/', null=True, blank=True)
    party = models.ForeignKey(PoliticalParty, on_delete=models.SET_NULL, null=True, blank=True)
    biography = models.TextField()
    campaign_promises = models.TextField()
    contact_information = models.TextField()
    education = models.TextField()
    professional_experience = models.TextField()
    public_service_record = models.TextField()
    social_media_links = models.CharField(max_length=255, blank=True, null=True)
    campaign_slogan = models.CharField(max_length=255)
    endorsements = models.TextField()
    campaign_events_schedule = models.TextField()
    previous_voting_record = models.TextField()
    languages_spoken = models.CharField(max_length=255)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user


class Poll(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    candidates = models.ManyToManyField('Candidate', related_name='polls', blank=True)
    voters = models.ManyToManyField(UserCustom, related_name='voted_polls', blank=True)

    def __str__(self):
        return self.title
