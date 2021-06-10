from django.db import models
from django.conf import settings
    
class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    date_of_publication = models.DateTimeField()
    description = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    is_available = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="books")

    def __str__(self):
        return self.title


class BorrowHistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    borrower = models.CharField(max_length=50)
    book = models.ForeignKey(Book,
                                 on_delete=models.CASCADE,
                                 related_name="borrowHistories")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="borrowed")
    returned_date = models.DateTimeField(null=True,)
    return_date = models.DateTimeField(null=True,)


    def __str__(self):
        return self.created_by.username