from .models import Wishlist
from rest_framework import serializers
from products.serializer import ProductSerializer
class WishlistSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    product_price = serializers.IntegerField(
        source="product.price",
        read_only=True
    )

    username = serializers.CharField(
        source="user.username",
        read_only=True
    )

    product_image = serializers.SerializerMethodField()

    def get_product_image(self, obj):
        image = obj.product.images.first()

        if image:
            return image.images.url

        return None

    class Meta:
        model = Wishlist
        fields = [
            "id",
            "user",
            "username",
            "product",
            "product_name",
            "product_price",
            "product_image",
            "added_at",
        ]

        extra_kwargs = {
            "user": {
                "read_only": True
            }
        }