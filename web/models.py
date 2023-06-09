from django.db import models
import uuid

FAQ_TYPE = (
    ("rent_tracking", "Rent Tracking"),
    ("new_deposit", "New Deposit"),
    ("existing_deposit", "Existing Deposit")
)


class Testimonial(models.Model):
    name = models.CharField(max_length=225, default="NISHMAL" )
    designation = models.CharField(max_length=255, default="Software Engineer")
    image = models.ImageField(upload_to="testimonials")
    description = models.TextField(blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Promoter(models.Model):
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to="promoters/")

    def __str__(self):
        return self.name
    

class Faq(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    faq_type = models.CharField(max_length=128, choices=FAQ_TYPE)

    def __str__(self):
        return self.title
    

class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class TestModel(models.Model):
    document= models.FileField(upload_to="documents/")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Car (models.Model):
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    manufacturer = models.ForeignKey("web.Manufacturer", on_delete=models.CASCADE)


class Manufacturer(models.Model):
    name = models.CharField(max_length=128)