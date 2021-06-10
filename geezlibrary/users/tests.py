import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from books.api.serializers import BorrowHistorySerializer, BookSerializer
from books.models import Book, BorrowHistory

class RegistrationTestCase(APITestCase):
    
    def test_registration(self):
        data = {"username": "testcase", "email": "test@geez.com",
                "password1": "dgdg12345", "password2": "dgdg12345"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration(self):
        data = {"username": "testcase", "email": "test@geez.com",
                "password1": "dgdg12345"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UserDetailsTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="testcase",
                                             password="dgdg12345")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_user_detail_authenticated(self):
        response = self.client.get(reverse("user"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["borrowed_count"], 2)
        self.assertEqual(response.data["due_for_return_in_30_days_count"], 1)

