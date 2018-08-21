from django.urls import path
from . import login_views, user_register, message_views, praise_views, wyq_views, pic_views

urlpatterns = [
    path('get_code_post', login_views.get_code_post),
    path('register_new_user', user_register.register_new_user),
    path('show_message', message_views.show_message),
    path('add_message', message_views.add_message),
    path('show_reply', message_views.show_reply),
    path('praise', praise_views.praise_record),
    path('add_reply', message_views.add_reply),
    path('user_comment', wyq_views.user_comment),
    path('add_picture', pic_views.add_picture)
]
