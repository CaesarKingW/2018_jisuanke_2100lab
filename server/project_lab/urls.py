from django.urls import path
from . import login_views, user_register, message_views, praise_views, wyq_views, update_personal_information, wq_views
from . import  pic_views
from . import account_destroy

urlpatterns = [
    path('get_code_post', login_views.get_code_post),
    path('register_new_user', user_register.register_new_user),
    path('show_message', message_views.show_message),
    path('add_message', message_views.add_message),
    path('show_reply', message_views.show_reply),
    path('user_comment', wyq_views.user_comment),
    path('manager_login', wyq_views.manager_login),
    path('manager_search', wyq_views.manager_search),
    path('manager_change', wyq_views.manager_change),
    path('praise', praise_views.praise_record),
    path('add_reply', message_views.add_reply),
    path('user_comment', wyq_views.user_comment),
    path('add_picture', pic_views.add_picture),# test
    path('show_picture',pic_views.show_picture),# test
    path('update_avator', update_personal_information.update_avator),
    path('get_user_phone', update_personal_information.get_user_phone),
    path('search_user', wq_views.search_user),
    path('authenticate', wq_views.authenticate),
    path('forbid_comment', wq_views.forbid_comment),
    path('search_comment', wq_views.search_comment),
    path('delete_comment', wq_views.delete_comment),
    path('search_order', wq_views.search_order),
    path('refund', wq_views.refund),
    path('account_destroy', account_destroy.account_destroy)
]
