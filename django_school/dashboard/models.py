from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    address=models.CharField(max_length=255)
    # pic=models.ImageField(upload_to='profile_pics/', null=True, blank=True)()
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username