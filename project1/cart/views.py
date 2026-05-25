from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .serializer import CartSerializer
from products.authentication import CookieJWTAuthentication


class CartCreate(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CartView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is not None:
            try:
                cart = Cart.objects.get(pk=pk,user=request.user)
            except Cart.DoesNotExist:
                return Response({"error": "Cart item not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = CartSerializer(cart)
            return Response(serializer.data,status=status.HTTP_200_OK)

        cart_items = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart_items,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)


class CartUpdate(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk,user=self.request.user)

        except Cart.DoesNotExist:
            return None

    def put(self, request, pk):
        cart = self.get_object(pk)
        if cart is None:
            return Response({"error": "Cart item not found"},status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK )

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    

    def delete(self, request, pk):
        cart = self.get_object(pk)
        if cart is None:
            return Response(
                {"error": "Cart item not found"},status=status.HTTP_404_NOT_FOUND)
        cart.delete()
        return Response({"message": "Cart item deleted"},status=status.HTTP_200_OK)