import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from books.api.serializers import BorrowHistorySerializer, BookSerializer
from books.models import Book, BorrowHistory

class BooksViewSetTestCase(APITestCase):
    
    list_url = reverse("books")

    def setUp(self):
        self.user = User.objects.create_user(username="testcase",
                                             password="dgdg12345")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_book_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_book_detail_retrieve(self):
        response = self.client.get(reverse("books", kwargs={"slug": "aaaaa-9059t0"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_avaialble_book_list(self):
        response = self.client.get(reverse("books", kwargs={"is_available": "True"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


