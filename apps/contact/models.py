from django.db import models
from django_enumfield import enum

from apps.studio.models import SocialMedia


class EmailQuery(models.Model):
    """
    Query model
    """
    class EmailQueryType(enum.Enum):
        ENQUIRIES = 0
        JOBS = 1

        __labels__ = {
            ENQUIRIES: "Enquiries",
            JOBS: "Jobs"
        }

    email = models.CharField(max_length=255)
    email_type = enum.EnumField(
        EmailQueryType,
        verbose_name="Select email type"
    )
    text = models.TextField(null=True)

    class Meta:
        verbose_name = "Email type"
        verbose_name_plural = "A - Email type"

    def __str__(self):
        return f'{self.email} - {self.email_type.name}'


class ContactNumber(models.Model):
    """
    Contactnumber Model
    """
    class ContactNumberType(enum.Enum):
        LANDLINE = 0
        MOBILE = 1

        __labels__ = {
            LANDLINE: "Landline",
            MOBILE: "Mobile"
        }
    number = models.CharField(max_length=16)
    contactnumber_type = enum.EnumField(
        ContactNumberType,
        verbose_name="Select contact number type"
    )

    class Meta:
        verbose_name = "Contact Number type"
        verbose_name_plural = "B - Contact Number types "

    def __str__(self):
        return f'{self.number} - {self.contactnumber_type.name}'


class Contact(models.Model):
    contact_number = models.ManyToManyField(
        ContactNumber
    )
    address = models.CharField(
        max_length=255
    )
    social_media = models.ManyToManyField(SocialMedia)
    query_type = models.ManyToManyField(EmailQuery)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "C - Contacts "

    def __str__(self):
        return str(self.id)
