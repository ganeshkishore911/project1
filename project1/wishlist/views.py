from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Wishlist
from .serializer import WishlistSerializer
from products.authentication import CookieJWTAuthentication


class WishlistCreate(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class WishlistView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is not None:
            try:
                wishlist = Wishlist.objects.get(pk=pk,user=request.user)

            except Wishlist.DoesNotExist:
                return Response({"error": "Wishlist item not found"},status=status.HTTP_404_NOT_FOUND)

            serializer = WishlistSerializer(wishlist)

            return Response(serializer.data,status=status.HTTP_200_OK)

        wishlist = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(wishlist,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)


class WishlistDelete(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            wishlist = Wishlist.objects.get(pk=pk, user=request.user)

        except Wishlist.DoesNotExist:
            return Response({"error": "Wishlist item not found"},status=status.HTTP_404_NOT_FOUND)

        wishlist.delete()

        return Response({"message": "Removed from wishlist"},status=status.HTTP_200_OK)