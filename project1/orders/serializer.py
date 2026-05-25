from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name",read_only=True)
    class Meta:
        model = OrderItem
        fields = ["id","order","product","product_name","quantity"]


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True,read_only=True)
    username = serializers.CharField(source="user.username",  read_only=True)

    class Meta:
        model = Order
        fields = ["id","user","username","order_items"]