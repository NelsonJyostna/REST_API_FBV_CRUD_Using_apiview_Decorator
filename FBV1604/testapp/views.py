from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

# Create your views here.
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    print('tasklist', tasks)
    serializer = TaskSerializer(tasks, many=True)
    print('taskList', serializer)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    print('taskDetail', tasks)
    serializer = TaskSerializer(tasks, many=False)
    print('taskDetail', serializer)
    return Response(serializer.data)

@api_view(['POST'])        
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    print('taskCreate', serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id=pk)
    print(tasks)
    serializer = TaskSerializer(instance=tasks, data=request.data)
    print('taskUpdate', serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = Task.objects.get(id=pk)
    print('taskDelete', tasks)
    tasks.delete()
    return Response('Delete Successfully')               