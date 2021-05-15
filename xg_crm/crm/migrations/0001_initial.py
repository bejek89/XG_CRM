# Generated by Django 3.2.3 on 2021-05-15 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nazwa', models.CharField(max_length=200)),
                ('NIP', models.IntegerField()),
                ('Osoba_kontatowa', models.CharField(max_length=30)),
                ('Numer_telefonu', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Zadanie', models.CharField(max_length=200)),
                ('task_data', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Nowe', 'Nowe'), ('W trakcie', 'W trakcie'), ('Zakonczone', 'Zakonczone')], max_length=500)),
                ('Postep_zadania', models.TextField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.client')),
            ],
        ),
    ]