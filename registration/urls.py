from registration import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]