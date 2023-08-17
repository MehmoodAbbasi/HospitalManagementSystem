from rest_framework import serializers
from api_v1.models import *
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','password2']

        def create(self,validated_data):
            password = validated_data.pop('password')
            password2 = validated_data.pop('password2')
            if password !=password2:
                raise serializers.ValidationError("Password does Not Match .")
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
