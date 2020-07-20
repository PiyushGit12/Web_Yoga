from django.shortcuts import render, redirect
from .forms import Blog_post_form, LoginForm, UserSiginform
from .models import  Blog_post


# Create your views here.
def login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('post_create')
    else:
        form = LoginForm()
        return render(request, 'mysite_post/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserSiginform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserSiginform()
    return render(request, 'mysite_post/signup.html', {'form': form} )


def blog_post_ui(request):
    blog_list = Blog_post.objects.all()
    count = Blog_post.objects.count()
    print('This is our Blog post count', count)

    last_video = Blog_post.objects.all().last()
    print('This is our  Last video from Db', last_video)
    lastobjdb = last_video.File_f.url
    context = {'file_url': lastobjdb,
               'blog_list': blog_list
               }
    return render(request, 'mysite_post/post_create.html', context)

