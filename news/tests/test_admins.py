from django.contrib import admin as main_admin
from django.contrib.auth import get_user_model
from django.test import TestCase

from news.models import Newspaper, Topic


class AdminPanelTests(TestCase):
    def setUp(self):
        self.admin_site = main_admin.site

    def test_models_are_registered_in_admin(self):
        registered_models = self.admin_site._registry

        self.assertIn(get_user_model(), registered_models)
        self.assertIn(Newspaper, registered_models)
        self.assertIn(Topic, registered_models)

    def test_redactor_admin_contains_custom_field(self):
        redactor_admin = self.admin_site._registry[get_user_model()]

        self.assertIn("years_of_experience", redactor_admin.list_display)

        flat_fields = []
        for name, field_options in redactor_admin.fieldsets:
            flat_fields.extend(field_options.get("fields", []))

        self.assertIn("years_of_experience", flat_fields)

    def test_newspaper_admin_configuration(self):
        newspaper_admin = self.admin_site._registry[Newspaper]

        self.assertEqual(
            newspaper_admin.list_display, ("title", "published_date", "topic")
        )
        self.assertEqual(newspaper_admin.list_filter, ("published_date", "topic"))
        self.assertEqual(newspaper_admin.search_fields, ("title", "content"))
