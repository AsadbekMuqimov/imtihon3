from django.db import models

class Banner(models.Model):
    title  = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    
    
    def __str__(self):
        return self.title


class Center_about(models.Model):
    title  = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    image = models.ImageField(max_length=255) 
    def __str__(self):
        return f"{self.title} "
    

class Address(models.Model):
    f_name  = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    messege = models.TextField()
   
    
    def __str__(self):
        return f"({self.f_name}, {self.phone}, {self.email}, {self.messege})"
    
    
    
class Staff(models.Model):
    name = models.CharField(max_length=255)
    group = models.FloatField()
    
    def __str__(self):
        return f"{self.name}, {self.group}"
    

class Student(models.Model):
    f_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    group = models.ForeignKey(Staff, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.f_name}, {self.gender}, {self.group}"