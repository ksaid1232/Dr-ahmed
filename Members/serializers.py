from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from Members.models import Customer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", 'username', 'password', 'email']


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["username", "email", "password"]
    #    extra_kwargs={
     #       "password":{'write_only':True}

      #      }

      #  }
