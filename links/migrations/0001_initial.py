# Generated by Django 3.2.3 on 2021-05-19 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistema', models.CharField(max_length=200, verbose_name='Sistema')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Título')),
                ('enlace', models.URLField(verbose_name='Enlace a acortar')),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='links.sistema', verbose_name='Sistema')),
            ],
        ),
    ]
