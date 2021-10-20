from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class blog(models.Model):
    title           = models.CharField(max_length=123)
    author          = models.CharField(max_length=50)
    describ         = RichTextField(blank=True, null=True)
    category        = models.CharField(max_length=50)
    is_recomended   = models.BooleanField(default=False)
    create          = models.DateTimeField(auto_now_add=True)
    update          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} ".format(self.title,self.author)