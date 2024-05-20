from django.contrib.auth.models import User
from django.db import models
import array
# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    BirthDate = models.DateField()
    PhoneNumber = models.CharField(max_length=10)
    Address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user}'

class Category(models.Model):
    CategoryName = models.CharField(max_length=45, primary_key=True)
    AgeMin = models.IntegerField()
    AgeMax = models.IntegerField()
    Time = models.CharField(max_length=45)

    def __str__(self):
        return  f'{self.CategoryName} {self.AgeMin}-{self.AgeMax} {self.Time}'

class Book(models.Model):
    BookName = models.CharField(max_length=45)
    CategoryName = models.ForeignKey(Category,on_delete=models.CASCADE)
    Is_barrowed = models.BooleanField()

    def __str__(self):
        return f'{self.BookName} {self.CategoryName}'

class Barrowed_book(models.Model):
    UserId = models.ForeignKey(Person,on_delete=models.CASCADE)
    BookId = models.ForeignKey(Book,on_delete=models.CASCADE)
    DateBarrowed= models.DateField()
    ReturnDate = models.DateField()
