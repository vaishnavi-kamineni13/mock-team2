from django.urls import path
from .import views

urlpatterns=[
path('', views.index,name="index"),
path('register',views.register,name="register"),
path('login',views.login,name="login"),
path('requests',views.requests,name="requests"),
path('donate',views.donate,name="donate"),
path('about',views.about,name="about"),
path('logout',views.logout,name="logout"),
]