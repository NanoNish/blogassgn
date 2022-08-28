from django.http import HttpResponse, HttpRequest
from rest_framework import viewsets
from .serializers import UserSerializer, PostSerializer
from blog.models import User, Post
from .permissions import IsAuthenticated

def index(request):
    return HttpResponse("Hello, world. You're being rickrolled in 3..2..1 Gotcha!!!")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated)

def login(request):
    user = request.body['user']
    password = request.body['password']
    userSet = User.objects.filter(user = user)
    if(len(userSet) == 1 and userSet[0].password == password):
        return True
    return False