from django.contrib import admin
from django.utils.translation import gettext_lazy
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.apps import apps

# Get all models from the app 'invent_app'
app_name = 'core'
app_models = apps.get_app_config(app_name).get_models()

# Register all models and their fields with the admin
for model in app_models:
    admin_class_attrs = {
        '__module__': model.__module__,
        'list_display': [field.name for field in model._meta.fields],
    }
    admin_class = type(f'{model.__name__}Admin', (admin.ModelAdmin,), admin_class_attrs)
    admin.site.register(model, admin_class)
