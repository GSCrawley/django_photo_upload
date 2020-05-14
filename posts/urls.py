from django.urls import path, include
from .views import HomePageView, CreatePostView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'), # new
    path('accounts/', include('django.contrib.auth.urls')),
    # path('admin_page/', views.admin_page, name='admin_page'),
]