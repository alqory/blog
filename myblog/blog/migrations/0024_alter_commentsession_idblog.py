# Generated by Django 3.2.8 on 2021-11-06 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_commentsession_idblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsession',
            name='idBlog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog'),
        ),
    ]
