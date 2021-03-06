from django.urls import path
from . import login_views, user_register, message_views, praise_views
from . import wyq_views, update_personal_information, wq_views, wchxviews
from . import pic_views
from . import account_destroy
from . import show_all_course
from . import takes_views, orders_views

urlpatterns = [
    path('get_code_post', login_views.get_code_post),
    path('get_user_code', login_views.get_user_code),
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
    path('show_picture', pic_views.show_picture),
    path('update_avator', update_personal_information.update_avator),
    path('update_nickname', update_personal_information.update_nickname),
    path('get_old_avator', update_personal_information.get_old_avator),
    path('get_user_information',
         update_personal_information.get_user_information),
    path('show_takes', takes_views.show_takes),
    path('add_or_update_takes', takes_views.add_or_update_takes),
    path('add_new_take', takes_views.add_new_take),
    path('set_burn', takes_views.set_burn),
    path('get_burn_status', takes_views.get_burn_status),
    path('add_share', takes_views.add_share),
    path('show_orders', orders_views.show_orders),
    path('get_order_payment', orders_views.get_order_payment),
    path('awardpay', orders_views.award_pay),
    path('search_user', wq_views.search_user),
    path('authenticate', wq_views.authenticate),
    path('forbid_comment', wq_views.forbid_comment),
    path('search_comment', wq_views.search_comment),
    path('delete_comment', wq_views.delete_comment),
    path('search_order', wq_views.search_order),
    path('refund', wq_views.refund),
    path('get_status', wchxviews.get_status),
    path('del_status', wchxviews.del_status),
    path('payment', wyq_views.payment),
    path('notify', wyq_views.alipay_get),
    path('account_destroy', account_destroy.account_destroy),
    path('show_free_course', show_all_course.show_free_course),
    path('show_paying_course', show_all_course.show_paying_course),
    path('get_specified_course', show_all_course.get_specified_course),
    path('get_course_info', wchxviews.get_course_info),
    path('back_log_out', wyq_views.back_logout),
    path('user_amount', wyq_views.user_amount),
    path('order_amount', wyq_views.order_amount),
    path('money_amount', wyq_views.money_amount),
    path('free_watch', wyq_views.free_watch),
    path('pay_watch', wyq_views.pay_watch),
    path('pay_sale', wyq_views.pay_sale),
    path('search_user', wq_views.search_user),
    path('authenticate', wq_views.authenticate),
    path('forbid_comment', wq_views.forbid_comment),
    path('search_comment', wq_views.search_comment),
    path('delete_comment', wq_views.delete_comment),
    path('search_order', wq_views.search_order),
    path('refund', wq_views.refund),
    path('add_course', wq_views.add_course),
    path('add_img', wq_views.add_img),
    path('add_audi', wq_views.add_audi),
    path('set_start_time', wq_views.set_start_time),
    path('set_end_time', wq_views.set_end_time),
    path('preview', wq_views.preview),
    path('supplement_course_information',
         wq_views.supplement_course_information),
    path('search_manager', wq_views.search_manager),
    path('modify', wq_views.modify),
    path('backstage_login', wq_views.backstage_login),
    path('backstage_register', wq_views.backstage_register),
    path('check', wq_views.check),
    path('get_mstatus', wq_views.get_mstatus),
    path('search_history', wq_views.search_history),
    path('search_course', wq_views.search_course),
    path('delete_course', wq_views.delete_course),
    path('search_one_course', wq_views.search_one_course),
    path('test', wq_views.test),
    path('editCourse', wq_views.editCourse),
    path('backstage_logout', wq_views.backstage_logout),
    path('modify_code', wq_views.modify_code),
    path('get_code', wq_views.get_code),
    path('half', wq_views.half),
    path('get_all_courses', wq_views.get_all_courses),
    path('get_all_users', wq_views.get_all_users),
    path('delete_user', wq_views.delete_user),
    path('get_all_messages', wq_views.get_all_messages),
    path('get_all_orders', wq_views.get_all_orders)
]
