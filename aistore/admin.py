from django.contrib import admin
from .models import Address, Cart, CartItem, Customer, Order, OrderItem, Product, Collection, Promotion

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory']
    list_editable = ['unit_price', 'inventory']
    search_fields = ['title__istartswith']
    list_per_page = 10

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured_product']
    list_editable = ['featured_product']
    list_per_page = 10

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['description', 'discount']
    list_per_page = 10

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'city', 'customer']
    list_per_page = 10

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    list_per_page = 10

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['placed_at', 'payment_status', 'customer']
    list_per_page = 10

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'unit_price']
    list_per_page = 10

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']
    list_per_page = 10

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']
    list_per_page = 10