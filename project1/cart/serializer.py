from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username",read_only=True)
    product_name = serializers.CharField(source="product.name",read_only=True)

    class Meta:
        model = Cart
        fields = ["id","user","username","product","product_name","quantity"]