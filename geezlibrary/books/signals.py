from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from books.models import Book,BorrowHistory

@receiver(pre_save, sender=Book)
def add_slug_to_book(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string

@receiver(post_save, sender=BorrowHistory)
def update_book_availability(sender, instance, *args, **kwargs):
    print(instance.book.title)
    print(instance.borower)
    if instance and not instance.returned_date:
        instance.book.is_available = False
        instance.book.save()
