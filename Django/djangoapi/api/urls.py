from django.urls import path
from . import views

urlpatterns = [
    path('test', views.welcome),
    path('', views.test),
    path('books', views.get_all_books),
    path('add_book', views.add_book),
    path('add_owner', views.add_owner),
     path('add_website', views.add_website),
    path('update_book/<int:book_id>', views.update_book),
    path('delete_book/<int:book_id>', views.delete_book),
    path('get_book/<int:book_id>', views.get_book_by_id),
    path('authors', views.get_all_authors),
]
