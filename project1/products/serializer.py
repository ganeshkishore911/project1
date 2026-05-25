from rest_framework import serializers
from .models import Product,MainCategory,SubCategory,ProductImages,ProductSize,BannerImage

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImages
        fields=["id","images"]

class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductSize
        fields=["id","size"]

class ProductSerializer(serializers.ModelSerializer):
    images=ProductImagesSerializer(many=True,read_only=True)
    sizes=ProductSizeSerializer(many=True,read_only=True)
    class Meta:
        model=Product
        fields=["id","sub_category","name","description","price","is_new","images","sizes"]

class SubCategorySerializer(serializers.ModelSerializer):
    products=ProductSerializer(many=True,read_only=True)
    class Meta:
        model=SubCategory
        fields=["id","main_category","name","banner_image","products"]

class BannerImageSerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(source="product.name",read_only=True)
    main_category_name=serializers.CharField(source="main_category.name",read_only=True)
    class Meta:
        model=BannerImage
        fields=["id","main_category","main_category_name","product","product_name","image","title","price"]

class MainCategorySerilaizer(serializers.ModelSerializer):
    subcategories=SubCategorySerializer(many=True,read_only=True)
    banners=BannerImageSerializer(many=True,read_only=True)
    class Meta:
        model=MainCategory
        fields=["id","name","subcategories","banners"]