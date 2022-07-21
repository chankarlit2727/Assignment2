from django.urls import resolve, reverse
from unittest import TestCase
from ipInput.views import index, getLink, CreateLink, UpdateLink, DeleteLink
import pytest
from django import urls


@pytest.mark.parametrize('param', [
    'index',
    'getLink',
    'createLink'
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200

    # def test_link_url_is_resolved(self):
    #     url = reverse('index')
    #     self.assertEquals(resolve(url).func, index)
    #
    # def test_get_url_is_resolved(self):
    #     url = reverse('getLink')
    #     self.assertEquals(resolve(url).func, getLink)
    #
    # def test_create_url_is_resolved(self):
    #     url = reverse('createLink')
    #
    #     self.assertEquals(resolve(url), CreateLink)

    # def test_update_url_is_resolved(self):
    #     url = reverse('updateLink', args=['1'])
    #     self.assertEquals(resolve(url).func, UpdateLink)
    #
    # def test_delete_url_is_resolved(self):
    #     url = reverse('deleteLink', args=['1'])
    #     self.assertEquals(resolve(url).func, DeleteLink)
