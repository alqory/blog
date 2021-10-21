from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):
    
    blogs = blog.objects.all()
    kategori = blog.objects.values('category').distinct()

    context = {
        'blog':blogs,
        'kat':kategori
        }


    return render(request,'index.html',context)


def tambah(request):

    form = blogForm()
    if request.method == 'POST':
        form = blogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    
    context = {
        'forms':form
    }
    return render(request,'tambah.html',context)

def update(request, id):
    data = blog.objects.get(id=id)
    
    form = blogForm(instance=data)

    if request.method == 'POST':
        form = blogForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    
    context = {
        'forms':form
    }
    return render(request,'update.html',context)

def hapus(request,id):
    data = blog.objects.get(id=id)
    data.delete()
    return redirect('blog:index')

def detail_post(request,id_detail):

    blogs = blog.objects.get(id=id_detail)

    context = {
        'post':blogs,
    }

    return render(request,'detail_post.html',context)


def kategori(request, Kategori_input):
       
    kategori = blog.objects.filter(category=Kategori_input)
    blogs = blog.objects.values('category').distinct()

    context = {
        'blog':blogs,
        'kat':kategori
        }


    return render(request,'kategori_post.html',context)
