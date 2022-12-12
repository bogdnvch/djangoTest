from django.urls import path
from .views import index
from .views import LoginUserView
# from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginUserView.as_view(), name='login')
    # path('login/', LoginView.as_view(template_name='info/login.html'), name='login')
]
