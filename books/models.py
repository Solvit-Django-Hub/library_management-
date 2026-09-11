from django.db import models
  

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    bio= models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address=models.CharField(blank=True)
    def __str__(self):
        return self.name
class Book(models.Model):
    title=models.CharField(max_length=200)
    isbn=models.CharField(max_length=13,unique=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books")
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE,related_name="books")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="books")
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
         return self.title
         