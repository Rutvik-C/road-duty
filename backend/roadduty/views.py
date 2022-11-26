from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions


from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import resolve
from rest_framework import viewsets, status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from .custom_renders import JPEGRenderer, PNGRenderer


class RiderViewSet(viewsets.ModelViewSet):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer


class ChallanImageViewSet(viewsets.ModelViewSet):
    queryset = ChallanImage.objects.all()
    serializer_class = ChallanImageSerializer

    def get_queryset(self):
        challan = self.request.query_params.get('challan')
        image_type = self.request.query_params.get('type')
        if challan:
            queryset = ChallanImage.objects.filter(challan=challan)
            if image_type:
                queryset = queryset.filter(type=image_type)
        else:
            queryset = ChallanImage.objects.all()
            if image_type:
                queryset = queryset.filter(type=image_type)
        return queryset


class ChallanViewSet(viewsets.ModelViewSet):
    queryset = Challan.objects.all()
    serializer_class = ChallanSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(self.get_serializer(obj).data, status=status.HTTP_201_CREATED, headers=headers)


class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
