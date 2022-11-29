from django.db import models
from django.utils.translation import gettext_lazy as _

CHOICES_SESSION_STATUS = (
    ("ACTIVE", "Активна"),
    ("CLOSED", "Закрыта"),
    ("NOT_COMED", "Не пришёл"),
)


class Clients:
    firstname = models.CharField(_("First name"), max_length=150)
    lastname = models.CharField(_("Last name"), max_length=150)


class Tatto:
    pass


class Sessions:
    client = models.ForeignKey(Clients)
    tatto_list = models.ManyToManyField(Tatto)
    datetime_session = models.DateTimeField(_("Date and time session"),
                                            editable=True)
    status = models.CharField(_("Status"),
                              choices=CHOICES_SESSION_STATUS,
                              default="ACTIVE")


class Photos:
    pass
