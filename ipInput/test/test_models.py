from django.test import TestCase, Client
from django.urls import resolve, reverse
from ipInput.models import Link


class TestModels(TestCase):

    def setUp(self):
        self.link = Link.objects.create(link_name='testing', link_text='10.1.128.131')

    def test_model_creation(self):
        link = Link.objects.get(link_name='testing')
        self.assertEquals(link.link_text, "10.1.128.131")


