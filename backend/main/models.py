from django.db import models


class BotUser(models.Model):
    tg_id = models.BigIntegerField(verbose_name='ID Telegram',unique=True)
    username = models.CharField(max_length=255, verbose_name='Username', null=True, blank=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.tg_id}'


class BotAdmin(models.Model):
    tg_id = models.BigIntegerField(verbose_name='ID Telegram',unique=True)
    name = models.CharField(max_length=255, verbose_name='Имя')

    class Meta:
        verbose_name = 'Администратора'
        verbose_name_plural = 'Администраторы'

    def __str__(self):
        return f'{self.tg_id}'


class BotToken(models.Model):
    ids = models.IntegerField(default=1, unique=True, editable=False)
    token = models.TextField(verbose_name='Токен',unique=True)

    class Meta:
        verbose_name = 'Токен'
        verbose_name_plural = 'Токен'

    def __str__(self):
        return f'{self.token}'
