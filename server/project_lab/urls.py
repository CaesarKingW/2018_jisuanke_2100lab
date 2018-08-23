from django.urls import path
from . import login_views, user_register, message_views, praise_views, wyq_views, pic_views, wq_views

urlpatterns = [
    path('get_code_post', login_views.get_code_post),
    path('register_new_user', user_register.register_new_user),
    path('show_message', message_views.show_message),
    path('add_message', message_views.add_message),
    path('show_reply', message_views.show_reply),
    path('praise', praise_views.praise_record),
    path('add_reply', message_views.add_reply),
    path('user_comment', wyq_views.user_comment),
    path('add_picture', pic_views.add_picture),
    path('search_user', wq_views.search_user),
    path('authenticate', wq_views.authenticate),
    path('forbid_comment', wq_views.forbid_comment),
    path('search_comment', wq_views.search_comment),
    path('delete_comment', wq_views.delete_comment),
    path('search_order', wq_views.search_order),
    path('refund', wq_views.refund),
    path('add_img', wq_views.add_img),
    path('add_audi', wq_views.add_audi),
    path('set_start_time', wq_views.set_start_time),
    path('set_end_time', wq_views.set_end_time),
    path('add_course', wq_views.add_course),
    path('preview', wq_views.preview)
]
