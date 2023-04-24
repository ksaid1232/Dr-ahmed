from .models import ProductModel
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductModel
        fields = (
            'id', 'title', 'short_description', 'thumbnail'
        )
