"""
apps configuration for the main project.
"""
from django.apps import AppConfig


class GreetingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'greeting'
