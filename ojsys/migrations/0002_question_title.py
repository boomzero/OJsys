# Generated by Django 4.2.5 on 2023-09-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ojsys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
