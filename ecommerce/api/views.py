from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from .serializers import *
from django.contrib.auth.hashers import make_password

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "/api/token",
        "/api/token/refresh"
    ]
    return Response(routes)

@api_view(["POST"])
def register_user(request):
    serializer = UserAuthSerializer(data=request.data)
    if serializer.is_valid():
        password = serializer.validated_data.get('password')
        serializer.validated_data['password'] = make_password(password)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_user(request):
    serializer = UserAuthSerializer(data=request.data)
    if serializer.is_valid():
        username_registered = serializer.validated_data.get('username')
        user_data = User.objects.filter(username = username_registered)
        newserializer = UserAuthSerializer(user_data,  context={'request': request}, many=True)
        return Response(newserializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)