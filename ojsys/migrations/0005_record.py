# Generated by Django 4.2.5 on 2023-09-29 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ojsys', '0004_submission_user_alter_submission_lang'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('time', models.IntegerField(default=0)),
                ('memory', models.IntegerField(default=0)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojsys.dataset')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojsys.submission')),
            ],
        ),
    ]
