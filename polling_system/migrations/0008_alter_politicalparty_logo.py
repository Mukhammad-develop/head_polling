# Generated by Django 4.2.7 on 2023-11-30 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling_system', '0007_alter_candidate_avatar_alter_politicalparty_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politicalparty',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='political-party-images'),
        ),
    ]
