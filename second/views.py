from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

from .models import Test
from .serializers import TestSerializer
from .permissions import TestPermission



class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    authentication_classes = (BasicAuthentication,)
    # permission_classes = TestPermission

    def get_queryset(self):
        return Test.objects.none()
