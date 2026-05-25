from .models import Order
from .serializer import OrderItemSerializer,OrderSerializer
from rest_framework.permissions import IsAuthenticated
from products.authentication import CookieJWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class OrderItemCreate(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrderItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


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