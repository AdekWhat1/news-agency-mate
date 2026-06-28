from django.contrib.auth import get_user_model
from django.test import TestCase

from news.models import Topic


class ModelTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(name="Science")
        self.assertEqual(str(topic), "Science")

    def test_redactor_str(self):
        redactor = get_user_model().objects.create(
            username="test_redactor",
            password="password123",
            first_name="John",
            last_name="Doe",
        )
        self.assertEqual(str(redactor), "test_redactor (John Doe)")
