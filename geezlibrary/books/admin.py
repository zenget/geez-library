from django.contrib import admin
from books.models import Book, BorrowHistory

admin.site.register(Book)
admin.site.register(BorrowHistory)
