from django.db import models
from django.utils.translation import gettext_lazy as _
from pathlib import Path
from time import time

CHOICES_SESSION_STATUS = (
    ("ACTIVE", "Активна"),
    ("CLOSED", "Закрыта"),
    ("NOT_COMED", "Не пришёл"),
)


def tatto_photo_path(instance, filename):
    # file will be uploaded to
    # MEDIA_ROOT / tatto_<tatto_name> / <filename>
    num = int(time() * 1000)
    suff = Path(filename).suffix

    return "tatto_{0}/{1}".format(instance.name, f"tatto_{num}{suff}")


class Clients:
    firstname = models.CharField(_("First name"), max_length=150)
    lastname = models.CharField(_("Last name"), max_length=150)
    birthday = models.DateField(_("Birthday"), blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        verbose_name = _("Clients")
        verbose_name_plural = _("Clients")


class Tatto:
    name = models.CharField(_("Name tatto"), max_length=150)
    image = models.ImageField(upload_to=tatto_photo_path,
                              blank=True,
                              null=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        verbose_name = _("Tatto")
        verbose_name_plural = _("Tatto")


class Sessions:
    client = models.ForeignKey(Clients)
    tatto_list = models.ManyToManyField(Tatto, blank=True, null=True)
    datetime_session = models.DateTimeField(_("Date and time session"),
                                            editable=True)
    status = models.CharField(_("Status"),
                              choices=CHOICES_SESSION_STATUS,
                              default="ACTIVE")
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")


class Photos:
    tatto = models.ForeignKey(Tatto)
    session = models.ForeignKey(Sessions)
    before_photo = models.ImageField(_("Before photo"),
                                     upload_to=tatto_photo_path,
                                     blank=True,
                                     null=True)
    after_photo = models.ImageField(_("After photo"),
                                    upload_to=tatto_photo_path,
                                    blank=True,
                                    null=True)

    class Meta:
        verbose_name = _("Photos")
        verbose_name_plural = _("Photos")