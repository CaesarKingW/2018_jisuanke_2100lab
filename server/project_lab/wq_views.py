from .models import User
from .models import Operating_history
from django.views.generic.base import View


def search_user(request):
    phone_number = request.POST.get('phone_number')
    user = User.objects.get(phone_number=phone_number)
    return render(request, 'user_managing.html', {'user':user})


def anthenticate(request):
    phone_number = request.POST.get('anthenticate')
    User.objects.get(phone_number=phone_number).Is_teacher = True
    Operating_history.objects.create()
    return redirect('user_managing')


def forbid_user_speech(request):
    phone_number = request.POST.get('forbid_use_speech')
    User.objects.get(phone_number=phone_number).Can_comment = False


def close_account(request):
    phone_number = request.POST.get('close_account')
    User.objects.get(phone_number=phone_number).delete()