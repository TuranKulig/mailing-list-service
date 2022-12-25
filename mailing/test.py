from rest_framework.test import APITestCase


class TestViews(APITestCase):

    def test_mailing_get(self):
        response = self.client.get('/mailing/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_mailing_info_get(self):
        response = self.client.get('/mailing/info/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_client_get(self):
        response = self.client.get('/client/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_message_get(self):
        response = self.client.get('/message/', format='json')
        self.assertEqual(response.status_code, 200)
