from django.urls import path

from book.views import BookList

urlpatterns = [
    path('book/', BookList.as_view(), name='list-create'),
    path('book/<int:pk>', BookList.as_view(), name='detail')
]