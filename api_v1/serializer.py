from rest_framework import serializers
from api_v1.models import *
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
        extra_kwargs ={'password':{'write_only':True}}
        def create(self,validated_data):
            user = User(**validated_data)
            user.save()
            return user

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields= ('__all__')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields= ['name','value','date']

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields= ('__all__')
