from django.shortcuts import render, redirect
from Members.models import Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomerRegistrationSerializer
from rest_framework.decorators import action
# from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin


# class CustomerViewSet(CreateModelMixin, DestroyModelMixin, UpdateModelMixin):
#     queryset = Customer.objects.all()
#     serializer = CustomerRegistrationSerializer

#     @action(detail=False)
#     def me(self, request):
#         print("asdddddddddddddd")
#         customer = Customer.objects.get(id=request.user.id)
#         return Response(request.user.id)


@api_view()
def access_handler(request):

    if request.method == "POST":
        if "signup" in request.POST:
            return Register_customer(request)
        elif "signin" in request.POST:
            return Login_customer(request)
    return Response(template_name="login.html")


@api_view(["POST"])
def Register_customer(request):
    serializer = CustomerRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.save()
        return Response(f"{data}")
    return Response(f"{serializer.errors}")


@api_view(["POST"])
def Login_customer(request):
    if request.method == "POST":

        username = request.data["user"]
        password = request.data["pass"]
        # print(dir(request))

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return Response("loggedin")
        return Response("this user does not exist")
    return Response(template_name="login.html")


@api_view()
def Logoutcustomer(request):
    print(request.user.is_authenticated)
    logout(request)
    return Response("Successfull logout")
