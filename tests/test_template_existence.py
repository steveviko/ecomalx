import os
from django.http import HttpResponse
from django.template.loader import get_template
from unittest import TestCase
from django.conf import settings

class TestTemplateExistenceTestCase(TestCase):
    def test_template_existence(self):
        # Assert that the template file exists
        self.assertTrue(os.path.isfile(os.path.join(settings.BASE_DIR, 'templates/Core', 'index.html')))

        # Get the template
        template = get_template('Core/index.html')

        # Assert that the template exists
        self.assertIsNotNone(template)

        