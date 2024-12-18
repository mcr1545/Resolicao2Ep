from django.shortcuts import render  # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.views.generic import ListView, CreateView, UpdateView, DeleteView # type: ignore
from .models import Todo

class TodoListView(ListView): # type: ignore
    model = Todo # type: ignore


class TodoCreateView(CreateView): # type: ignore
    model = Todo # type: ignore
    fields = ['title','deadline']
    success_url = reverse_lazy('todo_list') # type: ignore


class TodoUpdateView(UpdateView): # type: ignore
    model = Todo # type: ignore
    fields = ['title','deadline']
    success_url = reverse_lazy('todo_list') # type: ignore


class TodoDeleteView(DeleteView): # type: ignore
    model = Todo # type: ignore
    success_url = reverse_lazy('todo_list') # type: ignore
