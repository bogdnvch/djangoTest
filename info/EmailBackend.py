from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Info


UserModel = get_user_model()


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                Info.objects.create(user=user, successful=True)
                return user
            else:
                Info.objects.create(user=user, successful=False)

