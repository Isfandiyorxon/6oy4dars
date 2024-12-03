from django.db import models

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField
    biograph=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.first_name


class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publication_date=models.DateField
    photo= models.ImageField(upload_to='photos/',null=True,blank=True)
    isbn=models.CharField(max_length=13)
    genre=models.CharField(max_length=100)
    summary=models.TextField

    def __str__(self):
        return self.title

class Review (models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews')
    reviewer_name=models.CharField(max_length=100)
    comment=models.TextField(null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.reviewer_name

# Create your models here.
