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


class Clients(models.Model):
    firstname = models.CharField(_("First name"), max_length=150)
    lastname = models.CharField(_("Last name"), max_length=150)
    birthday = models.DateField(_("Birthday"), blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        verbose_name = _("Clients")
        verbose_name_plural = _("Clients")


class Tatto(models.Model):
    name = models.CharField(_("Name tatto"), max_length=150)
    price = models.FloatField(_("Price"), null=True, blank=True)
    image = models.ImageField(upload_to=tatto_photo_path,
                              blank=True,
                              null=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        verbose_name = _("Tatto")
        verbose_name_plural = _("Tatto")


class Sessions(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    tatto_list = models.ManyToManyField(Tatto)
    price_summary = models.FloatField(
        _("Price summary"),
        null=True,
        blank=True,
    )
    discount = models.IntegerField(_("Discount"), null=True, blank=True)
    datetime_session = models.DateTimeField(_("Date and time session"),
                                            editable=True)
    status = models.CharField(_("Status"),
                              max_length=200,
                              choices=CHOICES_SESSION_STATUS,
                              default="ACTIVE")
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")


class Photos(models.Model):
    tatto = models.ForeignKey(Tatto, on_delete=models.CASCADE)
    session = models.ForeignKey(Sessions, on_delete=models.CASCADE)
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