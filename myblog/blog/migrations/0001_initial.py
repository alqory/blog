# Generated by Django 3.2.8 on 2021-10-20 06:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
                ('author', models.CharField(max_length=50)),
                ('describ', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('category', models.CharField(max_length=50)),
                ('is_recomended', models.BooleanField(default=False)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
