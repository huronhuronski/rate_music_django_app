# Generated by Django 3.1.6 on 2021-02-09 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate_music_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='labels_past',
            field=models.ManyToManyField(blank=True, related_name='band_past_labels', to='rate_music_app.Label'),
        ),
    ]
