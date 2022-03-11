# Generated by Django 3.2.11 on 2022-03-11 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_contactpage_formfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Fecha de la noticia'),
        ),
    ]