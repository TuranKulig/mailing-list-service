from rest_framework import viewsets
from rest_framework.response import Response
from decouple import config
import requests
import pytz
import datetime
from celery.utils.log import get_task_logger

from rest_framework.decorators import action

from mailing.models import Client, Message, Mailing
from mailing.serializers import ClientSerializer, MessageSerializer, MailingSerializer


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class MailingViewSet(viewsets.ModelViewSet):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()

    logger = get_task_logger(__name__)

    URL = config('URL')
    TOKEN = config('TOKEN')

    def send_message(self, data, client_id, mailing_id, url=URL, token=TOKEN):
        mailing = Mailing.objects.get(pk=mailing_id)
        client = Client.objects.get(pk=client_id)
        timezone = pytz.timezone(client.timezone)
        now = datetime.datetime.now(timezone)

        if mailing.time_start <= now.time() <= mailing.time_end:
            header = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'}
            try:
                requests.post(url=url + str(data['id']), headers=header, json=data)
            except requests.exceptions.RequestException as exc:
                raise self.retry(exc=exc)
            else:
                Message.objects.filter(pk=data['id']).update(sending_status='Sent')
        else:
            time = 24 - (int(now.time().strftime('%H:%M:%S')[:2]) -
                         int(mailing.time_start.strftime('%H:%M:%S')[:2]))
            return self.retry(countdown=60 * 60 * time)

    @action(detail=False, methods=['get'])
    def info(self, request):
        total = Mailing.objects.count()
        mailing = Mailing.objects.values('id')
        content = {'Total mailings': total,
                   'The number of messages sent': ''}
        result = {}

        for row in mailing:
            res = {'Total messages': 0, 'Sent': 0, 'No sent': 0}
            mail = Message.objects.filter(mailing_id=row['id']).all()
            group_sent = mail.filter(sending_status=1).count()
            group_no_sent = mail.filter(sending_status=2).count()
            res['Total messages'] = len(mail)
            res['Sent'] = group_sent
            res['No sent'] = group_no_sent
            result[row['id']] = res

        content['The number of messages sent'] = result
        return Response(content)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
