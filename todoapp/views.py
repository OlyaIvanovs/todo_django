# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TodoSerializer
from .models import Todo

# List all todos or create a new one 
# todoslist/
class TodoList(APIView):

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True);
        return Response(serializer.data)

    def post(self):
        pass



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

        todo = Todo(title=title, text=text)
        todo.save()
        return redirect('/todoapp')
    else:
        return render(request, 'add_todo.html')

def delete_todo(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect('/todoapp')

def edit_todo(request, todo_id):
    if(request.method == 'POST'):
        title =request.POST['title']
        text =request.POST['text']
        todo = Todo.objects.get(id=todo_id)
        todo.text = text
        todo.title = title
        todo.save()
        return redirect('/todoapp')
    else:
        todo = Todo.objects.get(id=todo_id)
        context = {
            'todo': todo
        }
        return render(request, 'edit_todo.html', context); 
    
