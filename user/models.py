from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField


# Create your models here.


class CustomAccoutManager(BaseUserManager):

    def create_user(self, email, name, surname, group, password, ):
        if not email:
            raise ValueError(_('Email adresinizi daxil edin'))
        if not group:
            raise ValueError(_('Qrupunuzu daxil edin'))

        email = self.normalize_email(email)
        user = self.model(email=email, surname=surname, name=name, group=group)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, surname, group, password, ):
        user = self.create_user(
            email=email,
            name=name,
            surname=surname,
            group=group,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name='Email adresiniz', unique=True)
    date_joined = models.DateTimeField(verbose_name="Qoşulma tarixi", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Son giriş tarixi", auto_now=True)
    name = models.CharField(verbose_name='Adınız', max_length=150)
    surname = models.CharField(verbose_name='Soyadınız', max_length=150)
    group = models.CharField(max_length=100, verbose_name='Qrupunuz')
    point = models.IntegerField(verbose_name="İlkin bal", default="0")
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'group']
    object = CustomAccoutManager()

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
