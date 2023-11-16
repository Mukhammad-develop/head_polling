# Generated by Django 4.2.7 on 2023-11-16 12:24

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCustom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=75)),
                ('family_name', models.CharField(max_length=75)),
                ('fathers_name', models.CharField(max_length=75)),
                ('is_candidate', models.BooleanField(default=False)),
                ('is_voter', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('biography', models.TextField()),
                ('campaign_promises', models.TextField()),
                ('contact_information', models.TextField()),
                ('education', models.TextField()),
                ('professional_experience', models.TextField()),
                ('public_service_record', models.TextField()),
                ('social_media_links', models.CharField(blank=True, max_length=255, null=True)),
                ('campaign_slogan', models.CharField(max_length=255)),
                ('endorsements', models.TextField()),
                ('campaign_events_schedule', models.TextField()),
                ('previous_voting_record', models.TextField()),
                ('languages_spoken', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VoterCivilian',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PoliticalParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('ideology', models.TextField()),
                ('year_founded', models.PositiveIntegerField()),
                ('headquarters_location', models.CharField(max_length=255)),
                ('motto_or_slogan', models.CharField(max_length=255)),
                ('manifesto', models.TextField()),
                ('current_seats_held', models.PositiveIntegerField(default=0)),
                ('historical_performance', models.TextField()),
                ('campaign_focus', models.TextField()),
                ('social_media_links', models.URLField(blank=True, max_length=255, null=True)),
                ('contact_information', models.TextField()),
                ('affiliated_organizations', models.TextField()),
                ('previous_election_results', models.TextField()),
                ('coalition_partners', models.TextField(blank=True, null=True)),
                ('international_affiliations', models.TextField(blank=True, null=True)),
                ('leader', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='polling_system.candidate')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='polling_system.politicalparty'),
        ),
    ]
