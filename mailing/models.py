import pytz as pytz
from django.db import models


class Mailing(models.Model):
    start_date = models.DateTimeField(verbose_name='Mailing list start time.')
    end_date = models.DateTimeField(verbose_name='Mailing list end time.')
    content = models.TextField(verbose_name='Message text for client.')
    tag = models.CharField(max_length=150, verbose_name='Filter by tag.', null=True, blank=True)
    code = models.CharField(max_length=3, verbose_name='Filter by mobile operator code.', blank=True, null=True)


class Client(models.Model):
    CHOICE = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    phone = models.CharField(max_length=11, verbose_name='Client phone number',
                             help_text='7XXXXXXXXXX (X - number from 0 to 9)')
    tag = models.CharField(max_length=150, verbose_name='Tag.', null=True, blank=True)
    code = models.CharField(max_length=3, verbose_name='Mobile operator code.', null=True, blank=True)
    timezone = models.CharField(verbose_name='Time zone.', max_length=32, choices=CHOICE, default='UTC')


class Message(models.Model):
    CHOICES = [
        (1, "Sent"),
        (2, "No sent"),
    ]
    start_date = models.DateTimeField(verbose_name='Date and time of creation.')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Mailing.')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Client.')
    sending_status = models.CharField(max_length=50, choices=CHOICES, verbose_name='Sending status.')
