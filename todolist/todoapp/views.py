from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework import generics
from .serializers import *
from .models import *
#CRUD Operations
class ListTodo(generics.ListAPIView):      #read to do list
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializer
class UpdateTodo(generics.RetrieveUpdateAPIView):#Update to do list
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializer
class CreateTodo(generics.CreateAPIView):  #create to do list
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializer
class DeleteTodo(generics.DestroyAPIView):   #Delete to do list
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializer
class tagTodo(generics.ListAPIView):
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializer
    def get_queryset(self):
        tag = self.kwargs['tag']
        return ToDo.objects.filter(tag=tag)