from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.fields import ReadOnlyField  # token table


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


# class CompanySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = ["id", "url", "name", "seller", "address"]

class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = "__all__"


class VahanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vahan
        fields = "__all__"


class ChallanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challan
        fields = "__all__"


class ChallanImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallanImage
        fields = "__all__"


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = "__all__"


"""
class ChallanSerializer(serializers.ModelSerializer):
    # https://stackoverflow.com/questions/60102891/how-to-get-foreign-key-reference-in-serializer-using-input-value

    image = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="image-detail")
    # company = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    # images = ImageSerializer()
    # company = CompanySerializer()

    class Meta(object):
        model = Challan
        fields = ["id", "rider", "license_number", "status", "amount", "date_time", "image"]
"""
