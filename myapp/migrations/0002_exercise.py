# Generated by Django 5.0.1 on 2024-02-02 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_media', models.FileField(upload_to='photos')),
                ('e_name', models.CharField(max_length=30)),
                ('e_reps', models.TextField(default='')),
                ('e_sets', models.TextField(default='')),
                ('de_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.deficiency')),
            ],
        ),
    ]
