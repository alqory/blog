from django.shortcuts import render, redirect
from .models import blog
from .forms import *
from .decorators import *
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


    if request.method == 'POST':
        kata_kunci = request.POST['cari']

        cari = blog.objects.filter(title__contains = kata_kunci)
        banner = blog.objects.all()[0]
        category = kategori.objects.all()
        paginator = Paginator(cari, 12)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'data':pypload,
            'blog':page_obj,
            'kat':category,
            'banner':banner,
            'Kata' : f'Menampilkan pencarian yang paling relevan " {kata_kunci} " '
        }
    else :

        blogs = blog.objects.all().order_by('-id')[3:]
        banner = blog.objects.all()[0]
        banner2 = blog.objects.all()[1:3]
        category = kategori.objects.all()
        paginator = Paginator(blogs, 8)


        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
        'data':pypload,
        'blog':page_obj,
        'kat':category,
        'banner':banner,
        'banner2':banner2
        }

    print(request.user)
    return render(request,'index.html',context)

@allowed_users(allowed_role=['admin'])
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

@allowed_users(allowed_role=['admin'])
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

@allowed_users(allowed_role=['admin'])
def hapus(request,id):
    data = blog.objects.get(id=id)
    data.delete()
    return redirect('blog:index')


def detail_post(request,slug_input):
    
    blogs = blog.objects.get(slug=slug_input)
    comment = commentSession.objects.filter(blogs=blogs).order_by('time')
    terkait = blog.objects.all().order_by('-create')[1:6]
    # 
    
    if request.method == 'POST':
        new_comment = None
        formComment = commentForm(request.POST or None)
        if formComment.is_valid():
            # Create Comment object but don't save to database yet  
            new_comment = formComment.save(commit=False)
            #  # Assign the current post to the comment
            new_comment.blogs = blogs
            # # Save the comment to the database
            new_comment.save()

            return redirect('blog:detail', slug_input)
    else :
        formComment = commentForm()

    context = {
        'post':blogs,
        'comment':formComment,
        'terkait':terkait,
        'listComments':comment,
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
