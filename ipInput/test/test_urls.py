from django.urls import resolve, reverse
from django.test import TestCase
from ipInput.views import index, getLink, CreateLink, UpdateLink, DeleteLink


class TestUrlTests(TestCase):
    def test_link_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_get_url_is_resolved(self):
        url = reverse('getLink')
        self.assertEquals(resolve(url).func, getLink)

    def test_create_url_is_resolved(self):
        url = reverse('createLink')
        found = resolve(url)
        self.assertEquals(found.func.view_class, CreateLink)

    def test_update_url_is_resolved(self):
        url = reverse('updateLink', args=['1'])
        found = resolve(url)
        self.assertEquals(found.func.view_class, UpdateLink)

    def test_delete_url_is_resolved(self):
        url = reverse('deleteLink', args=['1'])
        found = resolve(url)
        self.assertEquals(found.func.view_class, DeleteLink)
