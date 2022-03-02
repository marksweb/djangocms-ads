from __future__ import annotations

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangocmsAdsConfig(AppConfig):
    """App config"""
    label = 'djangocms_ads'
    name = 'djangocms_ads'
    verbose_name = _('djangocms ads')
