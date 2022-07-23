from django.test import TestCase, Client
from django.urls import resolve, reverse
from rest_framework import status

from ipInput.models import Link
import json


def create_link(self, link_name, link_text):
    return Link.objects.create(link_name=link_name, link_text=link_text)


def update_link(self, link_name, link_text):
    return Link.objects.create(link_name=link_name, link_text=link_text)


def delete_link(self, link_name, link_text):
    return Link.objects.create(link_name=link_name, link_text=link_text)


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.index = reverse('index')
        self.getlink = reverse('getLink')
        self.create = reverse('createLink')
        self.update = reverse('updateLink', args=[1])
        self.delete = reverse('deleteLink', args=[1])

    def test_project_index(self):
        response = self.client.get(self.index)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ipInput/home.html')

    def test_project_getlink(self):
        response = self.client.get(self.getlink)
        self.assertEquals(response.status_code, 200)

    def test_project_create(self):
        self.link = create_link(self, link_name='testing', link_text='10.1.128.131')
        response = self.client.post(self.create)
        self.assertEquals(response.status_code, 200)

    def test_project_update(self):
        self.link = update_link(self, link_name='testing1', link_text='10.1.128.85')
        response = self.client.put(self.update)
        self.assertEquals(response.status_code, 200)

    def test_project_delete(self):
        self.link = delete_link(self, link_name='testing', link_text='10.1.128.131')
        response = self.client.delete(self.delete)
        self.assertEquals(response.status_code, 302)
