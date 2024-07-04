from django.contrib import admin
from . import models
# Register your models here.

# admin.site.register(models.Category)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('Brand_name',)}
    list_display=['Brand_name','slug']

admin.site.register(models.Brands)