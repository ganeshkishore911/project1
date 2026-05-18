from django.db import models
#from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField() 
    image=models.ImageField(upload_to='profiles/',null=True,blank=True)

# class MainCategory(models.Model):
#     Category_Choices = [
#         ('men', 'Men'),
#         ('ladies', 'Ladies'),
#         ('kids', 'Kids')
#     ]
#     name=models.CharField(max_length=50,unique=True,choices=Category_Choices)   #Men,Ladies,Kids
#     def __str__(self):
#         return self.name

# class SubCategory(models.Model):
#     main_category=models.ForeignKey(MainCategory,on_delete=models.CASCADE,related_name='subcategories')
#     name=models.CharField(max_length=50)   #T-Shirts,Shirts,Jeans and no unique=True the tshirts can be in both men and ladies
#     banner_image=models.ImageField(upload_to='subCat_banner_img/',blank=True,null=True)
#     def __str__(self):
#         return f"{self.main_category.name}- {self.name}" 

# class Product(models.Model):
   
#     sub_category=models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name="products")
#     name=models.CharField(max_length=100)
#     description=models.TextField(blank=True)
#     price=models.DecimalField(max_digits=10,decimal_places=2)
#     is_new = models.BooleanField(default=False) 
#     new_arrival=models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.name} - {self.sub_category.name} - {self.price} " # this will return the name of the product, subcategory name, price and size in the admin panel
    
# class ProductImages(models.Model):
#     product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
#     images=models.ImageField(upload_to='products_img/',blank=True,null=True)  #store the file path in database
#     def __str__(self):
#         return f"Image for {self.product.name}"
    

# class ProductSize(models.Model):
#     SIZE_CHOICES = [
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#         ('XL', 'Extra Large'),
#         ('XXL', 'Extra Extra Large'),
#     ]

#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sizes")
#     size = models.CharField(max_length=10, choices=SIZE_CHOICES)
#     stock = models.PositiveIntegerField(default=0)  # add stock count

#     def __str__(self):
#         return f"{self.product.name} - {self.size} (Stock: {self.stock})"



# class BannerImage(models.Model):
#     main_category = models.ForeignKey(MainCategory,on_delete=models.CASCADE,related_name='banners')
#     product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='banners')
#     image = models.ImageField(upload_to='banners/')
#     title = models.CharField(max_length=100, blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

#     def __str__(self):
#         return self.title if self.title else f"Banner for {self.product.name}"