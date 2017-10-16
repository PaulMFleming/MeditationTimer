# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 21:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useruploads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadAudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myaudio', models.FileField(upload_to='myaudio/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='myimage',
            field=models.ImageField(upload_to='myimages/'),
        ),
    ]
