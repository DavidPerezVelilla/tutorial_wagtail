# Generated by Django 3.2.11 on 2022-02-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20220223_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.URLField(blank=True),
        ),
    ]
