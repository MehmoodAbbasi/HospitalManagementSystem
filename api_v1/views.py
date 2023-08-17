from django.shortcuts import redirect , render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from . import serializer
from .serializer import *
from rest_framework import viewsets , status ,generics
from rest_framework.response import Response
from api_v1.models import Product
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from api_v1.forms import *


def index(request):
        return  render(request,'index.html')


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer = UserSerializer()


class ProductCreateView(APIView):

        def post(self,request):
                data = Product.objects.all()
                form = ProductForm(request.data)
                if form.is_valid():
                        task = form.save()
                        serializer = ProductSerializer(task)
                        # return Response(serializer.data,status=status.HTTP_201_CREATED)
                        return render(request, 'add_products.html', {'form': form, 'data': data,'serializer':serializer})
                else:
                        return Response(form.errors,status=status.HTTP_400_BAD_REQUEST)
        def get(self,request):
                data = Product.objects.all()
                form = ProductForm()
                return render(request,'add_products.html',{'form':form,'data':data})




class ProductUpdateView(APIView):
        def get(self,request,pk):
            data = Product.objects.get(pk=pk)
            serializer = ProductSerializer(data)
            return Response(serializer.data)
        def post(self,request,pk):
            data = Product.objects.get(pk=pk,)
            serializer = ProductSerializer(data,data=request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

        
class StudenttCreateView(APIView):

        def post(self,request):
                data = Student.objects.all()
                form = StudentForm(request.data)
                if form.is_valid():
                        task = form.save()
                        serializer = StudentSerializer(task)
                        # return Response(serializer.data,status=status.HTTP_201_CREATED)
                        return render(request, 'add_students.html', {'form': form, "data": data,'serializer':serializer})
                else:
                        # return Response(form.errors,status=status.HTTP_400_BAD_REQUEST)

                        return render(request, 'add_students.html', {'form': form, "data": data})
        def get(self,request):
                data = Student.objects.all()
                form = StudentForm()
                return render(request,'add_students.html',{'form':form,"data":data})


#Update the user Data


class StudentUpdateView(APIView):
        def get(self, request, pk):
                user = Student.objects.get(pk=pk)
                serializer = StudentSerializer(user)
                return Response(serializer.data)

        def post(self, request, pk):
                user = Student.objects.get(pk=pk)
                serializer = StudentSerializer(user, data=request.data)

                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








class UserCreateView(APIView):
        def post(self,request):
                form = UserCreationForm(request.data)
                if form.is_valid():
                        task = form.save()
                        serializer = UserSerializer(task)
                        return Response(serializer.data,status=status.HTTP_201_CREATED)
                else:
                        return Response(form.errors,status=status.HTTP_400_BAD_REQUEST)
        def get(self,request):
                data = Users.objects.all()
                form = UserCreationForm
                return render(request,'add_user.html',{'form':form,'data':data})


def login(request):
        return  render(request,'login.html')



class UserViewSet(viewsets.ModelViewSet):

        queryset = Users.objects.all()
        serializer_class = serializer.UserSerializer

class ProductViewSet(viewsets.ModelViewSet):

        queryset = Product.objects.all()
        serializer_class = serializer.ProductSerializer
