from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')
class ToDoSerializer(serializers.ModelSerializer):
    tags = serializers.MultipleChoiceField(choices=Tag.objects.all().values_list('id', 'name'), write_only=True)
    class Meta:
        model=ToDo
        fields=('id','Title','Description','Date','completed','due_date','status','tags','created_on')