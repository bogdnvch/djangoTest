from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import Info


def index(request):
    context = {
        'email': '4elovekconstanta@vought.com',
        'successful': Info.auths.successful().count(),
        'unsuccessful': Info.auths.unsuccessful().count()
    }
    return render(request, 'info/base.html', context)


class LoginUserView(LoginView):
    template_name = 'info/login.html'
