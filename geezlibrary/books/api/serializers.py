from rest_framework import serializers
from books.models import Book, BorrowHistory


class BorrowHistorySerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    book = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    book_slug = serializers.SerializerMethodField()
    is_returned = serializers.SerializerMethodField()
    return_date = serializers.DateField(format=None,input_formats=['%Y-%m-%d',])

    class Meta:
        model = BorrowHistory
        exclude = ["returned_date"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_book_slug(self, instance):
        return instance.book.slug

    def get_is_returned(self, instance):
        return instance.returned_date is not None



class BookSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    date_of_publication = serializers.DateField(format=None,input_formats=['%Y-%m-%d',])

    class Meta:
        model = Book
        exclude = ["id","updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")
