from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def user_auth(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect ('blog:index')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def allowed_users(allowed_role=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None

            if request.user.groups.exists():
                print(request.user.groups)
                group = request.user.groups.all()[0].name
            
            if group in allowed_role:
                return view_func(request, *args, **kwargs)

            else:
                return render(request,'permissions.html')
        return wrapper_func
    return decorators

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'visistors':
            return redirect('blog:index')
        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function