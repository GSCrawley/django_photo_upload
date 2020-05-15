from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# def login(request):
#     if request.user.is_authenticated:
#         return redirect('admin_page')
 
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = auth.authenticate(username=username, password=password)
 
#         if user is not None:
#             # correct username and password login the user
#             auth.login(request, user)
#             return redirect('admin_page')
 
#         else:
#             messages.error(request, 'Error wrong username/password')
 
#     return render(request, '/posts/login.html')
 
 
# def logout(request):
#     auth.logout(request)
#     return render(request,'/posts/logout.html')
 
 
# def admin_page(request):
#     if not request.user.is_authenticated:
#         return redirect('login')
 
#     return render(request, 'posts/admin_page.html')