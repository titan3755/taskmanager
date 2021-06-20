from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginform, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('task/', views.taskedit, name='taskedit'),
    path('edit/', views.task_mod, name='edit'),
    path('delete/', views.delete, name='delete'),
    path('item/<str:key>/', views.taskitem, name='item'),
    path('finditem/', views.finditem, name='finditem'),
]