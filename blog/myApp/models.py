from django.db import models

# Create your models here.
class Posts(models.Model):
    post_title = models.CharField(max_length=30)
    post_body = models.TextField(max_length=200)
    post_date = models.DateField()
    
    def __str__(self):
        return self.post_title