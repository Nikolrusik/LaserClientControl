from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("firstname"),
                                  max_length=150,
                                  blank=True,
                                  null=True)
    last_name = models.CharField(_("lastname"),
                                 max_length=150,
                                 blank=True,
                                 null=True)
    email = models.CharField(_("Email"), unique=True, max_length=250)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. \
    Unselect this instead of deleting accounts."),
    )
    objects = UserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["email"]
