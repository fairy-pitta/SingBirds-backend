# Generated by Django 5.1.2 on 2024-10-16 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singbirds', '0003_bird_hotspots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birddetail',
            name='spectrogram',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]