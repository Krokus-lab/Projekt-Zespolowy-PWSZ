# Generated by Django 3.0.5 on 2021-04-13 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attempts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(blank=True)),
                ('numeryZadanZamknietych', models.CharField(max_length=70)),
                ('numeryZadanOtwartych', models.CharField(max_length=70)),
                ('odpowiedzi', models.CharField(max_length=200)),
                ('punkty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('numer_kontaktowy', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('miasto', models.CharField(blank=True, max_length=100)),
                ('szkola', models.CharField(blank=True, max_length=100)),
                ('ranga', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='zadanie_matematyczne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_zadania', models.IntegerField()),
                ('nr_wersji', models.IntegerField()),
                ('rodzaj', models.CharField(max_length=30)),
                ('zestaw', models.CharField(blank=True, max_length=40)),
                ('tresc', models.CharField(max_length=200)),
                ('odp_a', models.CharField(blank=True, max_length=40)),
                ('odp_b', models.CharField(blank=True, max_length=40)),
                ('odp_c', models.CharField(blank=True, max_length=40)),
                ('odp_d', models.CharField(blank=True, max_length=40)),
                ('rozwiazanie', models.CharField(blank=True, max_length=200)),
                ('odpowiedz', models.CharField(max_length=40)),
                ('dzial', models.CharField(blank=True, max_length=30)),
                ('punkty', models.IntegerField()),
                ('url', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Zadanie_otwarte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_zadania', models.IntegerField()),
                ('nr_wersji', models.IntegerField()),
                ('tresc', models.CharField(max_length=200)),
                ('odpowiedz', models.CharField(max_length=30)),
                ('dzial', models.CharField(max_length=30)),
                ('punkty', models.IntegerField()),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zadanie_zamkniete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_zadania', models.IntegerField()),
                ('nr_wersji', models.IntegerField()),
                ('tresc', models.CharField(max_length=200)),
                ('odp_a', models.CharField(max_length=40)),
                ('odp_b', models.CharField(max_length=40)),
                ('odp_c', models.CharField(max_length=40)),
                ('odp_d', models.CharField(max_length=40)),
                ('odpowiedz', models.CharField(max_length=40)),
                ('dzial', models.CharField(max_length=30)),
                ('punkty', models.IntegerField()),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_zad_otwartych', models.CharField(max_length=50)),
                ('tresci_zad_otwartych', models.CharField(max_length=300)),
                ('odp_otwarte', models.CharField(max_length=200)),
                ('id_zad_zamknietych', models.CharField(max_length=50)),
                ('tresci_zad_zamknietych', models.CharField(max_length=400)),
                ('odp_zamkniete', models.CharField(max_length=200)),
                ('punkty', models.IntegerField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.User')),
            ],
        ),
        migrations.CreateModel(
            name='PostM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tresc', models.CharField(max_length=200)),
                ('stan', models.CharField(blank=True, max_length=30)),
                ('zadanie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.zadanie_matematyczne')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=200)),
                ('userP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.User')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('userA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.User')),
                ('zadanie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.PostM')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Post')),
                ('userA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.User')),
            ],
        ),
    ]