# Generated by Django 3.0.5 on 2021-05-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_kategoria_klasa_podkategoria_poziom_typ_zadanie'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='date',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='answerm',
            name='date',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='attempts',
            name='date',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='postm',
            name='date',
            field=models.CharField(blank=True, max_length=70),
        ),
    ]
