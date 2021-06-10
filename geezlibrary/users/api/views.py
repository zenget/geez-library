from users.models import CustomUser
from django.contrib.auth.models import User
from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserDisplaySerializer


class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)


class UsersListAPIView(generics.ListAPIView):
    serializer_class = UserDisplaySerializer

    def get_queryset(self):
        return CustomUser.objects.all()


    