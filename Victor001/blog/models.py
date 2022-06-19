from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=100)
    Text = models.TextField
    Author = models.ForeignKey(get_user_model)()
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField
