from django.urls import path
from .views import *
urlpatterns=[
    path('<int:pk>',UpdateTodo.as_view()),
    path('', ListTodo.as_view()),
    path('create',CreateTodo.as_view()),
    path('delete/<int:pk>/',DeleteTodo.as_view()),
   path('todo/tag/<str:tag>/', tagTodo.as_view(), name='tagTodo'),
]