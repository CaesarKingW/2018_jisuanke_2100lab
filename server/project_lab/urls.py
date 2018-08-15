from django.urls import path

urlpatterns = [
    path=('', kang_view.show_user, name='show_user'),
]
