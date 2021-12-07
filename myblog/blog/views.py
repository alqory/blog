from django.shortcuts import render, redirect
from .models import blog
from .forms import *
from .decorators import *
import requests
import math
from django.urls.base import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


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



# Refactory code

class BlogIndex(ListView):
    model               = blog
    context_object_name ='artikel_list'
    template_name       = 'blog/index.html'
    ordering            = ['-create']

    def get_queryset(self):
        return blog.objects.all()[3:]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategori'] = kategori.objects.all()
        context['banner'] = blog.objects.all()[0]
        context['banner2'] = blog.objects.all()[1:3]
        context['data'] = self.get_data()
        return context 
  
    def get_data(self):
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
        return pypload

class BlogDetail(DetailView):
    model = blog
    template_name='blog/detail.html'
    context_object_name = 'post'
    form = commentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = blog.objects.get(slug=self.kwargs.get('slug'))
        context['listComments'] = commentSession.objects.filter(blogs=slug).order_by('time')
        context['terkait'] = blog.objects.all().order_by('-create').exclude(slug=self.object.slug)[1:6]
        context['comment'] = self.form

        return context
    
    def post(self,  *args, **kwargs):
        formComment = commentForm(self.request.POST)
        if formComment.is_valid():
            # Create Comment object but don't save to database yet  
            new_comment = formComment.save(commit=False)
            #  # Assign the current post to the comment
            new_comment.blogs = blog.objects.get(slug=self.kwargs.get('slug'))
            # # Save the comment to the database
            new_comment.save()

            return redirect('blog:detail',self.kwargs.get('slug'))


class BlogKategori(ListView):
    template_name = 'blog/kategori.html'
    context_object_name = 'kat'
    
    def get_queryset(self):
        return blog.objects.filter(category=self.kwargs.get('category_id'))

    def get_context_data(self, **kwargs):
        print(self.kwargs.get('category_id'))
        context = super().get_context_data(**kwargs)
        print(self.kwargs.get('category_id'))
        context['title'] = kategori.objects.filter(id=self.kwargs.get('category_id'))
        return context

class BlogManage(ListView):
    template_name = 'blog/manage.html'
    context_object_name = 'manage_list'

    def get_queryset(self):
        return blog.objects.all()

class BlogCreate(CreateView):
    model = blog
    form_class = blogForm
    template_name = 'blog/create.html'

class BlogUpdate(UpdateView):
    model = blog
    form_class = blogForm
    template_name = 'blog/create.html'

class BlogDelete(DeleteView):
    model = blog
    form_class = blogForm
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:manage')