from django.urls import path
from . import kang_views, login_views

urlpatterns = [
    path('add_book', kang_views.add_book),
    path('show_books', kang_views.show_books),
    path('get_code_post', login_views.get_code_post),
]
