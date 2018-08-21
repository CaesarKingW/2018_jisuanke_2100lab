from django.urls import path
from . import  login_views, user_register, message_views ,wyq_views

urlpatterns = [
    path('get_code_post', login_views.get_code_post),
    path('register_new_user', user_register.register_new_user),
    path('show_message', message_views.show_message),
    path('add_message', message_views.add_message),
    path('show_reply', message_views.show_reply),
    path('user_comment', wyq_views.user_comment)
]
