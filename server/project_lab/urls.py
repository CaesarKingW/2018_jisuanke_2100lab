from django.urls import path
from . import kang_views, login_views, user_register, message_views

urlpatterns = [
    path('add_book', kang_views.add_book),
    path('show_books', kang_views.show_books),
    path('get_code_post', login_views.get_code_post),
    path('register_new_user', user_register.register_new_user),
    path('show_message', message_views.show_message),
    path('add_message',message_views.add_message)
]
