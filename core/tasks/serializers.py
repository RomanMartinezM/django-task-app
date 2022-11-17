from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskListSerializer(ModelSerializer):
    priority = SerializerMethodField('get_priority')
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_completed', 'priority']

    def get_priority(self, Task):
        return Task.priority.name