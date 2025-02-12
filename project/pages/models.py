from django.db import models

# Create your models here.


class Signup(models.Model):
    username = models.CharField(max_length=100 , default='user' )
    password = models.CharField(max_length=100 , default='0000')
    cpassword = models.CharField( max_length=100  , default='0000')
    email = models.CharField(max_length=100 , default='user@gmail.com')
    role = models.CharField(max_length=100 , default='admin')
    def __str__(self):
        return self.username
    



class books(models.Model):
    book_id = models.CharField(max_length=50 ,default= '0')
    book_name = models.CharField(max_length=50 , default ='book')
    book_author = models.CharField(max_length=50 , default = 'author')
    book_category = models.CharField(max_length=50 , default = 'category')    
    def __str__(self):
        return self.book_id



class borrowedbooks(models.Model):
    book_id = models.CharField(max_length=50 ,default= '0')
    book_name = models.CharField(max_length=50 , default ='book')
    book_author = models.CharField(max_length=50 , default = 'author')
    book_category = models.CharField(max_length=50 , default = 'category')    
    def __str__(self):
        return self.book_id