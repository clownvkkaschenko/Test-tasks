from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import CustomUser


class CustomUserForm(UserChangeForm):
    class Meta:
        widgets = {
            'phone': PhoneNumberPrefixWidget(),
        }


@register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserForm
    list_display = ('full_name_user', 'delivery_address', 'phone')
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        ('Регистрация',
            {'fields': (
                'first_name',
                'last_name',
                'phone',
                'street_name',
                'house_number',
                'apartment_number'
            )}
         )
    )
    fieldsets = (
        ('Пользователь',
            {'fields': (
                'username', 'password',
                ('is_active', 'is_staff'), 'date_joined'
            )}
         ),
        ('Контактные данные',
            {'fields': (
                'first_name', 'last_name', 'phone'
            )}
         ),
        ('Адрес',
            {'fields': (
                'street_name',
                'house_number',
                'apartment_number'
            )}
         )
    )
    list_filter = ('street_name',)
    search_fields = ('last_name', 'email', 'phone')
    ordering = ('id',)
    empty_value_display = '-пусто-'

    def full_name_user(self, obj):
        full_name = '%s %s' % (obj.first_name, obj.last_name)
        return full_name.strip()
    full_name_user.short_description = 'Имя пользователя'

    def delivery_address(self, obj):
        delivery_address = 'Ул.%s, Д.%s, Кв.%s' % (
            obj.street_name, obj.house_number, obj.apartment_number
        )
        return delivery_address.strip()
    delivery_address.short_description = 'Адрес пользователя'
