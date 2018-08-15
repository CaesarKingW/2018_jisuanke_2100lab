from .models import User
def search_user(request):
    phone_number = request.POST.get('phone_number')
    user = User.Objects.get(phone_number = phone_number)
    return render(request, 'user_managing.html', {'user':user})