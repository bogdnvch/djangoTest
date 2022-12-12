from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import Info
from django.urls import reverse_lazy


def index(request):
    successful_count = Info.auths.successful().count()
    unsuccessful_count = Info.auths.unsuccessful().count()
    all_count = Info.objects.all().count()

    success_rate = round(successful_count / all_count * 100, 2)
    unsuccess_rate = round(unsuccessful_count / all_count * 100, 2)

    context = {
        'email': '4elovekconstanta@vought.com',
        'successful_count': successful_count,
        'unsuccessful_count': unsuccessful_count,
        'all_count': all_count,
        'success_rate': success_rate,
        'unsuccess_rate': unsuccess_rate
    }
    return render(request, 'info/base.html', context)


class LoginUserView(LoginView):
    template_name = 'info/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
