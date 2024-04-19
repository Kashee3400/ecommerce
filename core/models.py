from django.db import models
from django.contrib.auth.models import User

class Logo(models.Model):
    image = models.ImageField(upload_to='logo/')

    class Meta:
        db_table = 'tbl_logo'
        managed = True
        verbose_name = 'Logo'
        verbose_name_plural = 'Logoes'


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Discount(models.Model):
    percentage = models.FloatField()

    def __str__(self):
        return f"{self.percentage}%"

from decimal import Decimal

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()
        else:
            raise ValueError("Insufficient stock")

    def get_discounted_price(book):
        if book.discount:
            percentage = Decimal(str(book.discount.percentage))  # Convert float to Decimal
            discounted_price = book.price - (book.price * (percentage / 100))
            return discounted_price
        else:
            return book.price
        
    def add_to_cart(self, user, quantity=1):
        # Convert quantity to an integer
        quantity = int(quantity)
        
        # Check if requested quantity is available in stock
        if quantity > int(self.stock):
            # Handle case where quantity exceeds stock
            return False

        # Get or create the cart item
        cart_item, created = CartItem.objects.get_or_create(user=user, book=self)
        if not created:
            # If cart item already exists, update its quantity
            cart_item.quantity = quantity
            cart_item.save()
        else:
            # If cart item is created for the first time, set its quantity
            cart_item.quantity = quantity
            cart_item.save()

        # Reduce the stock
        self.reduce_stock(quantity=quantity) 
        return True

    def remove_from_cart(self, user):
        CartItem.objects.filter(user=user, book=self).delete()

    def is_available(self, quantity=1):
        return self.quantity_available >= quantity
    
from django.db.models import Sum,F,Case,When

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cart_item')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.book.title} for {self.user.username}"

    @property
    def subtotal(self):
        if self.book.discount:
            discounted_price = self.book.get_discounted_price()
            return self.quantity * discounted_price
        else:
            return self.quantity * self.book.price
        
    @classmethod
    def total_price(cls, user):
        # Get all cart items for the user
        cart_items = cls.objects.filter(user=user)

        # Calculate total price considering quantity and discounted price for each item
        total_price = cart_items.aggregate(
            total_price=Sum(
                F('quantity') * Case(
                    When(book__discount__isnull=False, then=F('book__discount__price')),
                    default=F('book__price'),
                    output_field=models.DecimalField()
                ),
                output_field=models.DecimalField()
            )
        )['total_price'] or 0

        return total_price
    
import random
import string

class Address(models.Model):
    user = user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_address')
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country} - {self.postal_code}"
    
class PaymentMethod(models.Model):
    method = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.method
    
    class Meta:
        db_table = 'tbl_payment_method'
        verbose_name = 'Payment Method'
        verbose_name_plural = 'Payment Methods'

class Order(models.Model):
    PENDING = 'Pending'
    PROCESSED = 'Processed'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'

    ORDER_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PROCESSED, 'Processed'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders')
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default=PENDING)
    order_comment = models.TextField(blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=11, unique=True, editable=False, blank=True,null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name="order_address")
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, related_name="order_payments", null=True)

    def save(self, *args, **kwargs):
        self.order_id = self.generate_order_id()
        super().save(*args, **kwargs)

    def generate_order_id(self):
        prefix = 'ODR'
        # Generate random 8-digit number
        random_digits = ''.join(random.choices(string.digits, k=8))
        return f'{prefix}{random_digits}'

    def __str__(self):
        return f"Order for {self.user.username} ({self.status})"

    def mark_as_processed(self):
        if self.status == self.PENDING:
            self.status = self.PROCESSED
            self.save()
        else:
            raise ValueError("Cannot mark order as processed. Current status is not Pending.")

    def mark_as_delivered(self):
        if self.status == self.PROCESSED:
            self.status = self.DELIVERED
            self.save()
        else:
            raise ValueError("Cannot mark order as delivered. Current status is not Processed.")

    def cancel_order(self):
        if self.status == self.PENDING or self.status == self.PROCESSED:
            self.status = self.CANCELLED
            self.save()
        else:
            raise ValueError("Cannot cancel order. Current status is Delivered or Cancelled.")

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.quantity * self.book.price

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.book.reduce_stock(self.quantity)

    def __str__(self):
        return f"{self.quantity} x {self.book.title}"

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_images")
    image = models.ImageField(upload_to='book_images/')

    def __str__(self):
        return f"Image for {self.book.title}"


class TransactionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Transaction of {self.amount} for {self.order} by {self.user.username}"

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"Wishlist for {self.user.username}"

from datetime import datetime

class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_profile')
    phone_number = models.CharField(max_length=20,null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=200,choices=GENDER_CHOICES, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    class Meta:
        db_table = 'tbl_user_profile'
        managed = True
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def save(self, *args, **kwargs):
        if self.dob:  # Check if dob is not None
            today = datetime.today()
            dob = self.dob
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            self.age = age
        super(Profile, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.user.username} {self.dob}"
    
    def update_user_data(self, first_name, last_name, email):
        self.user.first_name = first_name
        self.user.last_name = last_name
        self.user.email = email
        self.user.save()
    
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class MediaGallery(models.Model):
    image = models.FileField(upload_to='gallery/',blank=True,null=True)
    image_url = models.URLField(blank=True,null=True)
    video_url = models.URLField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.image:
            return f"{self.image} - {self.created_at}"
        elif self.image_url:
            return f"{self.image_url} - {self.created_at}"
        else:
            return f"{self.video_url} - {self.created_at}"
        
    class Meta:
        db_table = 'tbl_medias'
        managed = True
        verbose_name = 'Media Gallery'
        verbose_name_plural = 'Media Gallerys'
