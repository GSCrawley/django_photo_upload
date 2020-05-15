from django.urls import path, include
from .views import HomePageView, CreatePostView
from . import views

# app_name = 'posts'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create/', CreatePostView.as_view(), name='add_post'), # new
    path('accounts/', include('django.contrib.auth.urls')),
    # path('admin_page/', views.admin_page, name='admin_page'),
]