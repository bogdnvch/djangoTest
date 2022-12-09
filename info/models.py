from django.db import models
from users.models import User


class InfoQuerySet(models.QuerySet):
    def successful(self):
        return self.filter(successful=True)

    def unsuccessful(self):
        return self.filter(successful=False)


class InfoManager(models.Manager):
    def get_queryset(self):
        return InfoQuerySet(self.model)

    def successful(self):
        return self.get_queryset().successful()

    def unsuccessful(self):
        return self.get_queryset().unsuccessful()


class Info(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='records', on_delete=models.DO_NOTHING)
    successful = models.BooleanField(verbose_name='Успешная ли авторизация', default=False)

    def __str__(self):
        return ("%s: %s") % (self.user, "Успешно" if self.successful else "Неуспешно")

    objects = models.Manager()
    auths = InfoManager()

    class Meta:
        verbose_name = 'Запись об авторизации'
        verbose_name_plural = 'Записи об авторизациях'



