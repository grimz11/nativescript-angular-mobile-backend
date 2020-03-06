from django.contrib import admin

# Register your models here.
from .models import Groceries

class GroceriesAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'is_published', 'price', 'receive_date', 'description', 'date_publish','category')
  list_display_links = ('id', 'name')
  list_filter = ('category',)
  list_editable = ('is_published',)
  search_fields = ('id', 'name', 'is_published', 'price', 'receive_date', 'description', 'date_publish','category')
  list_per_page = 25

admin.site.register(Groceries, GroceriesAdmin)