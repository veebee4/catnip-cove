from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog import views


class TestBlogUrls(SimpleTestCase):

    def test_blog_index_url(self):
        url = reverse('blog_index')
        self.assertEqual(resolve(url).func, views.blog_index)

    def test_blog_detail_url(self):
        url = reverse('blog_detail', args=[1])
        self.assertEqual(resolve(url).func, views.blog_detail)

    def test_blog_category_url(self):
        url = reverse('blog_category', args=['tech'])
        self.assertEqual(resolve(url).func, views.blog_category)

    def test_add_blog_url(self):
        url = reverse('add_blog')
        self.assertEqual(resolve(url).func, views.add_blog)

    def test_edit_blog_url(self):
        url = reverse('edit_blog', args=[1])
        self.assertEqual(resolve(url).func, views.edit_blog)

    def test_delete_blog_url(self):
        url = reverse('delete_blog', args=[1])
        self.assertEqual(resolve(url).func, views.delete_blog)

    def test_delete_comment_url(self):
        url = reverse('delete_comment', args=[1])
        self.assertEqual(resolve(url).func, views.delete_comment)
