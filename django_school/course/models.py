from django.db import models

# Create your models here.
class Course(models.Model):
    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    author= models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    stream=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    