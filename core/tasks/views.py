from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task, Priority
from .serializers import TaskSerializer, TaskListSerializer
# Create your views here. 

@api_view(['GET'])
def getTasks(request):
    task = Task.objects.all()
    serializer = TaskListSerializer(task, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
    data = request.data
    priority = Priority.objects.get(pk=data['priority'])
    task = Task.objects.create(
        title = data['title'],
        description = data['description'],
        is_completed = data['is_completed'],
        priority = priority
    )
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateTask(request, pk):
    data = request.data
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    data = {
        "message": "Task has been deleted succesfully"
    }
    return Response(data)

