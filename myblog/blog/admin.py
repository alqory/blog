from django.contrib import admin
from .models import *

# Register your models here.



class AdminBlog(admin.ModelAdmin):
    model = blog
    readonly_fields = ['create','update','slug']

class comment(admin.ModelAdmin):
    model = commentSession
    readonly_fields = ['time']

admin.site.register(blog,AdminBlog)
admin.site.register(commentSession, comment)