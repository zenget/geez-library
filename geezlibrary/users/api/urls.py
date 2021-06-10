from django.urls import path
from users.api.views import CurrentUserAPIView,UsersListAPIView

urlpatterns = [
    path("user/", CurrentUserAPIView.as_view(), name="current-user"),
    path("users/", UsersListAPIView.as_view(), name="user-list")
]