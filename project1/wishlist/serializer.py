from .models import Wishlist
from rest_framework import serializers

class WishlistSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name",read_only=True)
    username = serializers.CharField(source="user.username",read_only=True)

    class Meta:
        model = Wishlist
        fields = ["id","user","username","product","product_name","added_at"]
        read_only_fields = ["added_at"]