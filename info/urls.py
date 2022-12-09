from django.urls import path
from .views import index
from .views import LoginUserView

urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginUserView.as_view(), name='login')
]
