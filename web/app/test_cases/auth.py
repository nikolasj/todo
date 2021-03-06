from django.test import Client, TestCase
from django.urls import reverse

from django.contrib.auth.models import User


class TestApp(TestCase):
    def test_ok(self):
        """The app returns 200 OK for a user."""
        client = Client()
        user = User()
        client.force_login(user)

        response = client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_access(self):
        """Unauthenticated users are redirected to the login page."""
        client = Client()

        response = client.get(reverse("index"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("account_login"), response.get("Location"))
