from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.

class blog(models.Model):
    title           = models.CharField(max_length=200)
    author          = models.CharField(max_length=50)
    describ         = RichTextField(blank=True, null=True)
    images          = models.ImageField(upload_to='cover/',null=True)
    category        = models.CharField(max_length=50)
    is_recomended   = models.BooleanField(default=False)
    create          = models.DateTimeField(auto_now_add=True)
    update          = models.DateTimeField(auto_now=True)
    slug            = models.SlugField()


    def save(self, *args, **kwargs):
        if len(self.title) > 50:
            content = slugify(self.title[:50]) 
        
        self.slug = content
        super(blog, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {} ".format(self.title,self.author)

class commentSession(models.Model):
    blog = models.ForeignKey(blog,related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=120)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.blog)