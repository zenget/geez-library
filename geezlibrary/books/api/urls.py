from django.urls import include, path
from rest_framework.routers import DefaultRouter

from books.api import views as qv

router = DefaultRouter()
router.register(r"books", qv.BookViewSet)

urlpatterns = [
    path("", include(router.urls)), 

    path("books/<slug:slug>/borrowhistories/", 
         qv.BorrowHistoryListAPIView.as_view(),
         name="history-list"),

    path("books/<slug:slug>/borrow/", 
         qv.BorrowHistoryCreateAPIView.as_view(),
         name="history-create"),

    path("history/<int:pk>/", 
         qv.BorrowHistoryRUDAPIView.as_view(),
         name="history-detail"),
]