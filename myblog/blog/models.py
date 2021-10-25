from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from datetime import datetime

# Create your models here.

class blog(models.Model):
    title           = models.CharField(max_length=123)
    author          = models.CharField(max_length=50)
    describ         = RichTextField(blank=True, null=True)
    category        = models.CharField(max_length=50)
    is_recomended   = models.BooleanField(default=False)
    create          = models.DateTimeField(auto_now_add=True)
    update          = models.DateTimeField(auto_now=True)
    slug            = models.SlugField()


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(blog, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {} ".format(self.title,self.author)

class commentSession(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=120)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.blog)