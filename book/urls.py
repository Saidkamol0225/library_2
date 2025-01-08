from django.urls import path

from book.views import BookListCreateView, BookDetailView

urlpatterns = [
    path('book/', BookListCreateView.as_view()),
    path('book/<int:pk>', BookDetailView.as_view())
]