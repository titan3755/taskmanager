"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('avatar/', include('avatar.urls')),
    path('', include('mainapp.urls')),
    path('signup/', include('mainapp.urls')),
    path('login/', include('mainapp.urls')),
    path('dashboard/', include('mainapp.urls')),
    path('logout/', include('mainapp.urls')),
    path('editprofile/', include('mainapp.urls')),
    path('task/', include('mainapp.urls')),
    path('edit/', include('mainapp.urls')),
    path('delete/', include('mainapp.urls')),
    path('item/<str:key>/', include('mainapp.urls')),
    path('finditem/', include('mainapp.urls')),
]
