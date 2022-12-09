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
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                # print(user.email, 'Успешно')
                Info.objects.create(user=user, successful=True)
                return user
            else:
                # print(user.email, 'Неуспешно')
                Info.objects.create(user=user, successful=False)
