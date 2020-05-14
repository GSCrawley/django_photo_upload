from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy 
from .forms import PostForm
from .models import Post
from django.contrib import auth, messages


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')


def login(request):
    if request.user.is_authenticated:
        return redirect('admin_page')
 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
 
        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('admin_page')
 
        else:
            messages.error(request, 'Error wrong username/password')
 
    return render(request, 'posts/login.html')
 
 
def logout(request):
    auth.logout(request)
    return render(request,'posts/logout.html')
 
 
def admin_page(request):
    if not request.user.is_authenticated:
        return redirect('insta_login')
 
    return render(request, 'posts/admin_page.html')