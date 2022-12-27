from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    """Кастомная модель юзеров, которая основана на модели «AbstractUser».

    Поля модели:
      - email: электронная почта пользователя
      - first_name: имя пользователя
      - last_name: фамилия пользователя
      - phone: телефон пользователя
      - street_name: название улицы
      - house_number: номер дома
      - apartment_number: номер квартиры
    """
    username = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Электронная почта пользователя'
    )
    first_name = models.CharField(
        max_length=154,
        verbose_name='Имя пользователя'
    )
    last_name = models.CharField(
        max_length=154,
        verbose_name='Фамилия пользователя'
    )
    phone = PhoneNumberField(verbose_name='Телефон пользователя')
    street_name = models.CharField(
        max_length=154,
        verbose_name='Навзание улицы'
    )
    house_number = models.CharField(
        max_length=154,
        verbose_name='Номер дома'
    )
    apartment_number = models.CharField(
        max_length=154,
        null=True,
        verbose_name='Номер квартиры'
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
