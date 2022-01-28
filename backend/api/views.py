from rest_framework import generics, serializers
from .models import Todo
from .serializers import TodoSerilizer

class TodoGetCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerilizer

class TodoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerilizer



# 127.0.0.1 
# 10.0.2.2:8000 