from .models import Order
from .serializer import OrderItemSerializer,OrderSerializer
from rest_framework.permissions import IsAuthenticated
from products.authentication import CookieJWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from cart.models import Cart
from .models import Order, OrderItem
from django.db.models import Sum

class CreateOrder(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart_items = Cart.objects.filter(user=request.user)

        if not cart_items.exists():
            return Response(
                {"error": "Cart is empty"},
                status=status.HTTP_400_BAD_REQUEST
            )

        order = Order.objects.create(user=request.user)

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        cart_items.delete()

        return Response(
            {"message": "Order created"},
            status=status.HTTP_201_CREATED
        )

class OrderView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is not None:
            try:
                order = Order.objects.get(pk=pk,user=request.user)
            except Order.DoesNotExist:
                return Response({"error": "Order not found"},status=status.HTTP_404_NOT_FOUND)

            serializer = OrderSerializer(order)
            return Response(serializer.data,status=status.HTTP_200_OK)

        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class OrderStats(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[CookieJWTAuthentication]
    def get(self,request):
        stats=(OrderItem.objects.filter(order__user=request.user).values("product__name").annotate(total_quantity=Sum("quantity")))
        data=[
            {
                "name":item["product__name"],
                "quantity":item["total_quantity"]
            }
            for item in stats
        ]# list comprehension

        return Response(data)
    
class OrderpricesStats(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[CookieJWTAuthentication]
    def get(self,request):
        pass