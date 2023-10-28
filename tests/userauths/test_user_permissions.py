from django.contrib.auth import get_user_model
from django.test import TestCase


class TestUserModelPermissionsTestCase(TestCase):
    def test_user_has_required_permissions(self):
        user = get_user_model()(email='steve.viko@example.com', username='steveviko')
        user.set_password('password123')
        user.is_staff = True
        user.save()

        self.assertTrue(user.has_perm('auth.add_user'))
        self.assertTrue(user.has_perm('auth.change_user'))
        self.assertTrue(user.has_perm('auth.delete_user'))