from django.urls import path
from . import login_views, user_register, message_views, praise_views, wyq_views, update_personal_information, wq_views
from . import  pic_views
from . import account_destroy
from . import show_all_course

urlpatterns = [
    path('get_code_post', login_views.get_code_post),
    path('get_user_code', login_views.get_user_code),
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
    path('update_nickname', update_personal_information.update_nickname),
    path('get_old_avator',update_personal_information.get_old_avator),
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
    path('preview', wq_views.preview),
    path('account_destroy', account_destroy.account_destroy),
    path('show_free_course', show_all_course.show_free_course),
    path('show_paying_course', show_all_course.show_paying_course)
    
]
