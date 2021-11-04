from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator
import requests
import math
# Create your views here.

def index(request):
    # Cuaca API
    city = 'Pontianak'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ebdd290488e624510dd716d774523aaa'
    data = requests.get(url).json()
    pypload = {
        'kota':data['name'],
        'ikon':data['weather'][0]['icon'],
        'kecepatan_angin':data['wind']['speed'],
        'temperatur': math.ceil(data['main']['temp'] - 273), #Celcius 
        'tekanan_udara':data['main']['pressure'],
        'kondisi':data['weather'][0]['main']
        }
    print(pypload)


    
    blogs = blog.objects.all().order_by('-id')[1:]
    banner = blog.objects.all()[0]
    category = kategori.objects.all()
    paginator = Paginator(blogs, 8)
    

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'data':pypload,
        'blog':page_obj,
        'kat':category,
        'banner':banner,
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

def detail_post(request,slug_input):

    
    blogs = blog.objects.get(slug=slug_input)
    terkait = blog.objects.all().order_by('-create')[1:6]
    # 
    if request.method == 'POST':
        formComment = commentForm(request.POST)
        if formComment.is_valid():
            obj = formComment.save(commit=False)
            obj.blog = blogs
            obj.save()

            return redirect('blog:detail', slug_input)
    else :
        formComment = commentForm()

    context = {
        'post':blogs,
        'comment':formComment,
        'terkait':terkait,
    }

    return render(request,'detail_post.html',context)


def kategories(request,Kategori_input):
       
    q = kategori.objects.filter(id=Kategori_input)
    kategoris = blog.objects.filter(category=Kategori_input)



    context = {
        'kat':kategoris,
        'title':q
        }


    return render(request,'kategori_post.html',context)
