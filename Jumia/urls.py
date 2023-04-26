"""Jumia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home
from about.views import about
from service.views import service
from menu.views import menu
from contact.views import contact
from Registration.views import register, Login
from booking.views import booking
from team.views import team 
from testimonial.views import testimonial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('menu/', menu, name ='menu'),
    path('contact/', contact, name ='contact'),
    path('register/', register, name = 'register'),
    path('login/', Login , name = 'login'),
    path('booking/', booking , name = 'booking'),
    path('team/', team, name = 'team'),
    path('testimonial/', testimonial, name = 'testimonial')
]