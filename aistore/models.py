from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    # product_set 자동생성

class Collection(models.Model):
    title = models.CharField(max_length=255)
    # prevent circular import by using string 'Product' and related_name='+'
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')
    
    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    title= models.CharField(max_length=255)
    slug = models.SlugField(default='-', null=True)
    description = models.TextField()
    # 666666.22
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)    
    inventory = models.PositiveSmallIntegerField()
    # 최종 업데이트한 시점(auto_now: 한번정하변 안변함)
    last_update = models.DateTimeField(auto_now_add=True)
    # 1:N relationship with collection
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    # M:N relationship with promotion
    promotions = models.ManyToManyField(Promotion, blank=True)
    # orderitem 자동생성
    
    def __str__(self) -> str:
        return self.title

class Customer(models.Model):
    MEMBERSHIP_BRONZE= 'B'
    MEMBERSHIP_SILVER= 'S'
    MEMBERSHIP_GOLD= 'G'
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),    
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_day = models.DateField(null=True, blank=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_GOLD)
    
    class Meta:
        ordering = ['first_name', 'last_name']
        indexes = [
            models.Index(fields=['last_name', 'first_name'])
        ]
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Order(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('P','Pending'),
        ('C', 'Complete'),
        ('F', 'Failed'),    
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default='P')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # one to one relationship with customer
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self) -> str:
        return f'{self.city}'

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    
    def __str__(self) -> str:
        return f'CartItem: {self.product.title} (x{self.quantity}) in Cart {self.cart.id}'