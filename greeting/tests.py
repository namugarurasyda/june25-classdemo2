"""
Tests for the greeting application.
This module contains test cases for the 'greeting' Django app.
"""

from django.test import TestCase, Client
from django.urls import reverse


class GreetingTests(TestCase):
    """A test case for the main greeting view."""

    def setUp(self):
        """Set up a test client for use in all test methods."""
        self.client = Client()

    def test_index_page(self):
        """
        Tests that the main index page returns a 200 status code,
        contains the text 'Hello', and uses the correct template.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello")
        self.assertTemplateUsed(response, "index.html")


class GreetingFunctionalityTests(TestCase):
    """A test case for the functionality of the greeting view."""

    def setUp(self):
        """Set up a test client."""
        self.client = Client()

    def test_greeting(self):
        """Tests that the context contains the correct greeting."""
        response = self.client.get(reverse("index"))
        self.assertEqual(response.context["greeting"], "Hello")
