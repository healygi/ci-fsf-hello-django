"""django_todo  Configuration

The `patterns` list routes s to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/s/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a  to patterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a  to patterns:  path('', Home.as_view(), name='home')
Including another conf
    1. Import the include() function: from django.s import include, path
    2. Add a  to patterns:  path('blog/', include('blog.s'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_todo_list, name='get_todo_list'),
    path('add', views.add_item, name='add'),
    path('edit/<item_id>', views.edit_item, name='edit'),
    path('toggle/<item_id>', views.toggle_item, name='toggle'),
    path('delete/<item_id>', views.delete_item, name='delete'),
]
