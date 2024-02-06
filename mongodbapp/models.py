from djongo import models

class students(models.Model):
    Id = models.CharField(max_length=2,primary_key=True)
    Name = models.CharField(max_length=15)
    Age = models.CharField(max_length=2)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=10)
    Address = models.CharField(max_length=50)
    
    

# Create your models here.
