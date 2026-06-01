from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    product_price = serializers.DecimalField(
        source="product.price",
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    product_image = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product",
            "quantity",
            "product_name",
            "product_price",
            "product_image",
        ]

    def get_product_image(self, obj):
        image = obj.product.images.first()

        if image:
            return image.images.url

        return None


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(
        source="order_items",
        many=True,
        read_only=True
    )

    class Meta:
        model = Order
        fields = "__all__"