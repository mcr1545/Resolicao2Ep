"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path  # type: ignore
from todos.views import TodoListView, TodoCreateView, TodoDeleteView, TodoUpdateView



urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'), # type: ignore
    path('create/', TodoCreateView.as_view(), name='todo_create'), # type: ignore
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='todo_update'), # type: ignore
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='todo_delete')] # type: ignore