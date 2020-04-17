from rest_framework import generics
from rest_framework.permissions import AllowAny

from todo.auth_.models import MyUser
from todo.auth_.serializers import MyUserSerializer


class CreateUserView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get_queryset(self):
        return MyUser.objects.all()

    def get_serializer_class(self):
        return MyUserSerializer
