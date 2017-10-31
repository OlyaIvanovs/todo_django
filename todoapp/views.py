# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context); 

def todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    context = {
        'todo': todo
    }
    return render(request, 'todo.html', context); 


def add_todo(request):
    if(request.method == 'POST'):
        title =request.POST['title']
        text =request.POST['text']
    else:
        return render(request, 'add_todo.html')
    
