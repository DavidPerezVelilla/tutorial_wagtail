# Generated by Django 3.2.11 on 2022-02-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250, verbose_name='titulo')),
                ('contenido', models.CharField(max_length=1000, verbose_name='contenido')),
            ],
        ),
    ]