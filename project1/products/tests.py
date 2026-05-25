from django.test import TestCase
from rest_framework.test  import APIClient

from .models import (MainCategory,SubCategory)
class MainCategoryTest(TestCase):
    def setUp(self):
        self.client=APIClient()
        self.category=(
            MainCategory.objects.create(name="Men")
        )

        SubCategory.objects.create(
            main_category=self.category,
            name="Tshirt"
        )
    def test_get_categories(self):
        response=self.client.get("/api/category/")
        self.assertEqual(response.status_code,200)

    def test_get_subcategories(self):
        response=self.client.get(f"/api/category/{self.category.id}/")
        self.assertEqual(response.status_code,200)