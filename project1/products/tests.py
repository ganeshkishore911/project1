from django.test import TestCase
from rest_framework.test  import APIClient
from .models import (MainCategory,SubCategory,Product)
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User=get_user_model()

class MainCategoryTest(TestCase):
    def setUp(self):
        self.client=APIClient()
        self.category=(
            MainCategory.objects.create(name=123)
        )
        SubCategory.objects.create(
            main_category=self.category,name="Tshirt"
        )
    def test_get_categories(self):
        response=self.client.get("/api/category/")
        print("response",response.data)
        self.assertEqual(response.status_code,200)

    def test_get_subcategories(self):
        response=self.client.get(f"/api/category/{self.category.id}/")
        self.assertEqual(response.status_code,200)

class ProductCreateTest(TestCase):
    def setUp(self):
        self.client=APIClient()
        self.user=User.objects.create_user(username="ganesh",password="1233")
        self.main_category=MainCategory.objects.create(name="Men")
        self.sub_category=SubCategory.objects.create(main_category=self.main_category,name="Tshirt")
        refresh=RefreshToken.for_user(self.user)
        self.client.cookies['access_token']=str(refresh.access_token)

    def test_create_product(self):
        data={
            "subcategory": self.sub_category.id,
            "name": "Polo Tshirt",
            "description": "Cotton tshirt",
            "price": 500
        }   
        response=self.client.post("/api/productcreate/",data)
        print("cretae product",response.data)
        self.assertEqual(response.status_code,201)
        self.assertEqual(Product.objects.count(), 1)


    def test_create_product_without_login(self):
        data={
            "subcategory": self.sub_category.id,
            "name": "Polo Tshirt",
            "description": "Cotton tshirt",
            "price": 500
        } 
        self.client.cookies.clear()

        response = self.client.post("/api/productcreate/",data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Product.objects.count(), 0)