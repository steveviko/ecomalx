from django.contrib.auth import get_user_model
from django.test import TestCase

class TestUserModelCreateTestCase(TestCase):
    def test_can_create_user(self):
        user = get_user_model()(email='steve.viko@example.com', username='steveviko')
        user.set_password('password123')
        user.save()

        self.assertTrue(user.is_active)
        self.assertEqual(user.email, 'steve.viko@example.com')
        self.assertEqual(user.username, 'steveviko')