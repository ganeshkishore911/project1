from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer

class ProductCreate(APIView):
    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    

class ProductView(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            try:
                product=Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return Response({"error":"Not Found"},status=status.HTTP_400_BAD_REQUEST)
            serializer=ProductSerializer(product)
            return Response(serializer.data ,status=status.HTTP_200_OK)
        else:
            product=Product.objects.all()
            serializer=ProductSerializer(product,many=True)
            return Response(serializer.data ,status=status.HTTP_200_OK)
    
class ProductUpdate(APIView):

    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None
        
    def put(self,request,pk):   #update all fields
        product=self.get_object(pk)
        if product is None:
            return Response({"error":"Not found"},status=status.HTTP_400_BAD_REQUEST)
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):   #update only specific felids
        product=self.get_object(pk)
        if product is None:
            return Response({"error":"Not found"},status=status.HTTP_400_BAD_REQUEST)
        serializer=ProductSerializer(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        product=self.get_object(pk)
        if product is None:
            return Response({"error":"Not found"},status=status.HTTP_400_BAD_REQUEST)
        product.delete()
        return Response(status=status.HTTP_200_OK)
        


