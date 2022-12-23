from django.contrib import admin

from .models import Mailing, Client, Message

admin.site.register([Mailing, Client, Message])
