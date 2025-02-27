from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Model for categories
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for customers
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Model for hotel categories
class HotelCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='Default Description')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, default='Default City')
    state = models.CharField(max_length=100, default='Default State')
    country = models.CharField(max_length=100, default='Default Country')
    phone_number = models.CharField(max_length=20, default='000-000-0000')
    email = models.EmailField(default='default@example.com')
    category = models.ForeignKey(HotelCategory, on_delete=models.SET_NULL, null=True)
    image_url = models.URLField(default='https://via.placeholder.com/150')  # URL field for image

    def __str__(self):
        return self.name

# Model for rooms
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Default Room Name')
    description = models.TextField(default='Default Description')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image_url = models.URLField(default='https://via.placeholder.com/150')

    def __str__(self):
        return self.name

# Model for bookings
class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking by {self.customer} for room {self.room.name}"

# Model for reviews
class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    hotel = models.ForeignKey(Hotel, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review by {self.customer.user.username} for hotel {self.hotel.name}"

    def clean(self):
        if not (1 <= self.rating <= 5):
            raise ValidationError('Rating must be between 1 and 5')

# Model for amenities
class Amenity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Model for room images
class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return f"Image for {self.room.name}"

# Model for room amenities
class RoomAmenity(models.Model):
    room = models.ForeignKey(Room, related_name='amenities', on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amenity.name} in {self.room.name}"
