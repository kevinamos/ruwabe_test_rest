from rest_framework.generics import ListAPIView, CreateAPIView

from ruwabe_app.models import *

from .serializers import  GetUsersSerializer, CreateUserSerializer

class PostListAPIView(ListAPIView):
	queryset=User.objects.all()
	serializer_class=GetUsersSerializer

class CreateUserApiView(CreateAPIView):
    model = User
    
    serializer_class = CreateUserSerializer
