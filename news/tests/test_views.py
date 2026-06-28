from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from news.models import Newspaper, Topic


class ViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="auth_user",
            password="secure_password",
        )
        self.topic = Topic.objects.create(name="Politics")
        self.newspaper = Newspaper.objects.create(
            title="Breaking News",
            content="Some text",
            published_date="2026-06-28",
            topic=self.topic,
        )

    def test_newspaper_list_page_redirects_if_anonymous(self):
        response = self.client.get(reverse("news:newspaper-list"))
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 302)

    def test_newspaper_lost_page_accessible_if_logged_in(self):
        self.client.login(username="auth_user", password="secure_password")
        response = self.client.get(reverse("news:newspaper-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "news/newspaper_list.html")
