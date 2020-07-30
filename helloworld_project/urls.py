"""helloworld_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from hello.views import helloView
from todo.views import todoView, addTodo, deleteTodo
from scheduler.views import schedulerView, getResult
from filterresult.views import resultView
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from register.views import registerView 

urlpatterns = [
    path('home/', helloView),
    # path('', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('todo/', todoView),
    path('scheduler/', schedulerView),
    path('getResult/', getResult),
    path('filterresult/', resultView),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('register/', registerView),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
   
]
