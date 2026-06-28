from django.contrib.auth import get_user_model
from django.test import TestCase

from news.forms import (NewspaperForm,
                        NewspaperSearchForm,
                        RedactorCreationForm
                        )
from news.models import Topic


class FormTests(TestCase):
    def test_newspaper_form_valid_data(self):
        topic = Topic.objects.create(name="Tech")
        user = get_user_model().objects.create_user(
            username="reporter_1",
            password="password123"
        )

        form_data = {
            "title": "Test Title",
            "content": "Test Content",
            "published_date": "2026-06-28",
            "topic": topic.id,
            "publishers": [user.id],
        }
        form = NewspaperForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_newspaper_form_invalid_if_empty(self):
        form = NewspaperForm(data={})

        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
        self.assertIn("content", form.errors)

    def test_newspaper_search_form_is_optional(self):
        form = NewspaperSearchForm(data={})

        self.assertTrue(form.is_valid())

    def test_redactor_creation_form_experience_validation(self):
        form_data = {
            "username": "new_reporter",
            "years_of_experience": -5,
            "password1": "secure_pass123",
            "password2": "secure_pass123",
        }
        form = RedactorCreationForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn("years_of_experience", form.errors)
        self.assertEqual(
            form.errors["years_of_experience"][0],
            "Years of experience must be positive",
        )
