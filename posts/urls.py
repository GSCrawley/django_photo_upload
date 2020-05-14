from django.urls import path
from .views import HomePageView, CreatePostView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'), # new
    path('login/', views.login, name='insta_login'),
    path('logout/', views.logout, name='insta_logout'),
    path('admin_page/', views.admin_page, name='admin_page'),
]