# Generated by Django 3.2.8 on 2021-11-06 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_remove_commentsession_idblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsession',
            name='idBlog',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog'),
            preserve_default=False,
        ),
    ]
