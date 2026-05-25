from django.contrib import admin
from .models import Product,MainCategory,SubCategory,BannerImage,ProductImages,ProductSize

# Register your models here.
class ProductImagesInline(admin.TabularInline):
    model=ProductImages
class ProductSizeInline(admin.TabularInline):
    model=ProductSize
class PrdouctAdmin(admin.ModelAdmin):
    inlines=[ProductSizeInline,ProductImagesInline]

class BannerImageInline(admin.TabularInline):
    model=BannerImage

class MainCAategoryAdmin(admin.ModelAdmin):
    inlines=[BannerImageInline]

admin.site.register(Product,PrdouctAdmin)
admin.site.register(MainCategory,MainCAategoryAdmin)
admin.site.register(SubCategory)
