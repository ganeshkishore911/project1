from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated

from .authentication import CookieJWTAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import MainCategory, SubCategory,BannerImage
from .serializer import (
    MainCategorySerilaizer,
    SubCategorySerializer,BannerImageSerializer)


class MainCategoryView(APIView):

    def get(self, request, pk=None):
        # GET all main categories
        if pk is None:
            categories = MainCategory.objects.all()
            serializer = MainCategorySerilaizer(categories,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

        # GET subcategories of specific main category
        try:
            category = MainCategory.objects.get(pk=pk)

        except MainCategory.DoesNotExist:
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = SubCategorySerializer(category.subcategories.all(),many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
class ProductCreate(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProductList(APIView):
    def get(self, request, id):
        products = Product.objects.filter(
            sub_category=id
        )

        serializer = ProductSerializer(
            products,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
class ProductView(APIView):

    def get(self, request, pk=None):

        # print("REQUEST USER:", request.user)
        # print("AUTH:", request.auth)

        if pk is not None:

            try:
                product = Product.objects.get(pk=pk)

            except Product.DoesNotExist:
                return Response(
                    {"error": "Product not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = ProductSerializer(product)

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        products = Product.objects.all()

        serializer = ProductSerializer(
            products,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class ProductUpdate(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)

        except Product.DoesNotExist:
            return None

    def put(self, request, pk):
        product = self.get_object(pk)

        if product is None:
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductSerializer(
            product,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):

        product = self.get_object(pk)

        if product is None:
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductSerializer(
            product,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):

        product = self.get_object(pk)

        if product is None:
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        product.delete()

        return Response(
            {"message": "Product deleted successfully"},
            status=status.HTTP_200_OK
        )
    

class HomeBannerView(APIView):
    def get(self, request, category):

        banners = BannerImage.objects.filter(
            main_category__name__iexact=category
        )
        serializer = BannerImageSerializer(
            banners,
            many=True
        )

        return Response(serializer.data)