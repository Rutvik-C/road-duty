import json
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
from .email import send_email_to_user
from rest_framework.decorators import api_view

import requests


@api_view(['POST'])
def post_function_request(request, pk):
    print(pk)
    obj = Rider.objects.filter(pk=pk).first()

    # send_email_to_user(obj.name, obj.email)
    return Response(data="asd", status=status.HTTP_201_CREATED)


class RiderViewSet(viewsets.ModelViewSet):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer

    def get_queryset(self):
        license_number = self.request.query_params.get('license_number')
        queryset = Rider.objects.all()
        if license_number:
            queryset = Rider.objects.filter(license_number=license_number)
            if queryset.count() == 0:
                vahan_endpoint = f"http://127.0.0.1:8000/vahan/?license_number={license_number}"
                response = requests.get(vahan_endpoint)
                # self.create(request=response.content)
                print("in rider", response.json())
                try:
                    response_data = response.json()[0]
                except:
                    # no one with that license plate
                    return None
                print("Here here")
                data = {
                    "license_number": response_data["license_number"],
                    "name": response_data["name"],
                    "email": response_data["email"],
                    "phone": response_data["phone"],
                }

                print("data", data)
                serializer = self.get_serializer(data=data)
                serializer.is_valid(raise_exception=True)
                obj = serializer.save()
                return Rider.objects.filter(license_number=license_number)
        return queryset


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
        print(request.data)
        new_data = json.dumps(request.data)
        new_data = json.loads(new_data)
        print(new_data, type(new_data))
        if not 'rider' in request.data and 'license_number' in request.data:
            params = {"license_number": new_data['license_number']}
            rider_info = requests.get("http://127.0.0.1:8000/" + "rider", params=params)
            rider_info = rider_info.json()

            if rider_info == []:
                # no such rider exists
                return
            new_data['rider'] = rider_info[0]['id']
            # obj = Rider.objects.filter(license_number=request.data['license_number'])
            # print(obj.first().pk)
            # new_data['rider'] = obj.first().pk
        # serializer = self.get_serializer(data=request.data)
        serializer = self.get_serializer(data=new_data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        headers = self.get_success_headers(serializer.data)
        if 'rider' in new_data:
            rider_obj = Rider.objects.filter(pk=new_data['rider']).first()
            challan_data = self.get_serializer(obj).data
            # print(rider_obj, challan_id['id'])
            send_email_to_user(rider_obj.name, rider_obj.email, new_data["location"], challan_data['id'])
        return Response(self.get_serializer(obj).data, status=status.HTTP_201_CREATED, headers=headers)

    def put(self, request, format=None):
        print(request.data)
        new_data = json.dumps(request.data)
        new_data = json.loads(new_data)
        print(new_data, type(new_data))
        if not 'rider' in request.data and 'license_number' in request.data:
            params = {"license_number": new_data['license_number']}
            rider_info = requests.get("http://127.0.0.1:8000/" + "rider", params=params)
            rider_info = rider_info.json()

            if rider_info == []:
                # no such rider exists
                return
            new_data['rider'] = rider_info[0]['id']
            # obj = Rider.objects.filter(license_number=request.data['license_number'])
            # print(obj.first().pk)
            # new_data['rider'] = obj.first().pk
        # serializer = self.get_serializer(data=request.data)
        serializer = self.get_serializer(data=new_data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        headers = self.get_success_headers(serializer.data)
        if 'rider' in new_data:
            rider_obj = Rider.objects.filter(pk=new_data['rider']).first()
            challan_data = self.get_serializer(obj).data
            # print(rider_obj, challan_id['id'])
            send_email_to_user(rider_obj.name, rider_obj.email, new_data["location"], challan_data['id'])
        return Response(self.get_serializer(obj).data, status=status.HTTP_201_CREATED, headers=headers)

    """def create(self, request, *args, **kwargs):
        print(request.data)
        new_data = json.dumps(request.data)
        new_data = json.loads(new_data)
        print(new_data, type(new_data))
        if not 'rider' in request.data:
            params = {"license_number": new_data['license_number']}
            rider_info = requests.get("http://127.0.0.1:8000/" + "rider", params=params)
            rider_info = rider_info.json()

            if rider_info == []:
                # no such rider exists
                return
            new_data['rider'] = rider_info[0]['id']
            # obj = Rider.objects.filter(license_number=request.data['license_number'])
            # print(obj.first().pk)
            # new_data['rider'] = obj.first().pk
        serializer = self.get_serializer(data=request.data)

        obj = Rider.objects.filter(pk=new_data['rider']).first()

        headers = self.get_success_headers(serializer.data)
        serializer = self.get_serializer(data=new_data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()

        send_email_to_user(obj.name, obj.email, new_data["location"])
        # print(self.get_serializer(obj).data)
        return Response(self.get_serializer(obj).data, status=status.HTTP_201_CREATED, headers=headers)"""

    def get_queryset(self):
        status = self.request.query_params.get('status')
        if status:
            queryset = Challan.objects.filter(status=status)
        else:
            queryset = Challan.objects.all()
        return queryset


class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

    def get_queryset(self):
        queryset = Query.objects.filter(challan__status="query_raised")
        return queryset


class VahanViewSet(viewsets.ModelViewSet):
    queryset = Vahan.objects.all()
    serializer_class = VahanSerializer

    def get_queryset(self):
        license_number = self.request.query_params.get('license_number')
        queryset = Vahan.objects.all()
        if license_number:
            queryset = Vahan.objects.filter(license_number=license_number)
            return queryset

        return queryset
