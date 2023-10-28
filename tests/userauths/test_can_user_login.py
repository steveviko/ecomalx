from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import Client


def is_client_authenticated(client):
    """Returns True if the client is authenticated, False otherwise."""

    try:
        user = client.user
    except AttributeError:
        return False

    return user.is_authenticated

class TestUserModelLoginTestCase(TestCase):
    def test_can_login_user(self):
        user = get_user_model()(email='steve.viko@example.com', username='steveviko')
        user.set_password('password123')
        user.save()

        # Login the user.
        client = Client()
        client.login(email='steve.viko@example.com', password='password123')

        # Assert that the user is logged in.
        self.assertTrue(is_client_authenticated(client))