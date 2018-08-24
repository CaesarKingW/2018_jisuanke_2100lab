from django.urls import path
from . import login_views, user_register, message_views
from . import praise_views, wyq_views, pic_views, wq_views

urlpatterns = [
    path('get_code_post', login_views.get_code_post),
    path('register_new_user', user_register.register_new_user),
    path('show_message', message_views.show_message),
    path('add_message', message_views.add_message),
    path('show_reply', message_views.show_reply),
    path('manager_login', wyq_views.manager_login),
    path('manager_search', wyq_views.manager_search),
    path('manager_change', wyq_views.manager_change),
    path('praise', praise_views.praise_record),
    path('add_reply', message_views.add_reply),
    path('add_picture', pic_views.add_picture),
    path('search_user', wq_views.search_user),
    path('authenticate', wq_views.authenticate),
    path('forbid_comment', wq_views.forbid_comment),
    path('search_comment', wq_views.search_comment),
    path('delete_comment', wq_views.delete_comment),
    path('search_order', wq_views.search_order),
    path('refund', wq_views.refund),
    path('payment', wyq_views.payment),
    path('notify', wyq_views.alipay_notify)
]
