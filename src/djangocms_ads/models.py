from __future__ import annotations

from typing import Any

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin
from djangocms_attributes_field.fields import AttributesField

__all__ = ["AdSlotPlugin", "AdvancedAdContainerPlugin", "AdvertPlugin", "SimpleAdContainerPlugin"]


# Add additional choices through the ``settings.py``.
TEMPLATE_DEFAULT = "default"


def get_templates() -> list[tuple[str, Any]]:
    choices = [(TEMPLATE_DEFAULT, _("Default"))]
    choices += getattr(settings, "DJANGOCMS_ADS_TEMPLATES", [])
    return choices


class AdvancedAdContainerPlugin(CMSPlugin):
    """Advanced ad container allowing javascript to be added directly"""
    internal_name = models.CharField(
        verbose_name=_("internal name"),
        max_length=255,
        help_text=_("Provide internal name for Ad slot."),
    )
    content = models.TextField(
        verbose_name=_("Advert script tag"),
        help_text=_("The script tag for the head of the page")
    )
    template = models.CharField(
        verbose_name=_("Template"),
        choices=get_templates(),
        default=TEMPLATE_DEFAULT,
        max_length=255,
    )
    modified = models.DateTimeField(
        verbose_name=_("Modified"), auto_now=True
    )

    class Meta:
        app_label = 'djangocms_ads'
        verbose_name = _("Advanced ad container")
        verbose_name_plural = _("Advanced ad containers")

    def __str__(self) -> str:
        return self.internal_name


class SimpleAdContainerPlugin(CMSPlugin):
    """Simple ad container which doesn't contain javascript"""
    internal_name = models.CharField(
        verbose_name=_("internal name"),
        max_length=255,
        help_text=_("Provide internal name for Ad slot."),
    )
    template = models.CharField(
        verbose_name=_("Template"),
        choices=get_templates(),
        default=TEMPLATE_DEFAULT,
        max_length=255,
    )
    modified = models.DateTimeField(
        verbose_name=_("Modified"), auto_now=True
    )

    class Meta:
        app_label = 'djangocms_ads'
        verbose_name = _("Simple ad container")
        verbose_name_plural = _("Simple ad containers")

    def __str__(self) -> str:
        return self.internal_name


class AdSlotPlugin(CMSPlugin):
    """Ad slot definition"""
    internal_name = models.CharField(
        verbose_name=_("internal name"),
        max_length=255,
        help_text=_("Provide internal name for Ad slot."),
    )
    ad_unit_path = models.CharField(
        verbose_name=_("Ad unit path"),
        max_length=255,
        help_text=_("The first item provided by google for the slot, e.g. '/4321234/MPU'")
    )
    sizes = models.CharField(
        verbose_name=_("Ad sizes"),
        max_length=255,
        help_text=_("The second item provided by google for the slot, e.g. [300, 250]")
    )
    div_id = models.CharField(
        verbose_name=_("Div ID"),
        max_length=100,
        help_text=_("The third item provided by google for the slot, e.g. 'div-gpt-ad-12345-0'")
    )
    template = models.CharField(
        verbose_name=_("Template"),
        choices=get_templates(),
        default=TEMPLATE_DEFAULT,
        max_length=255,
    )
    modified = models.DateTimeField(
        verbose_name=_("Modified"), auto_now=True
    )

    class Meta:
        app_label = 'djangocms_ads'
        verbose_name = _("ad slot")
        verbose_name_plural = _("ad slots")

    def __str__(self) -> str:
        return self.internal_name


class AdvertPlugin(CMSPlugin):
    """Advert to display in the page"""
    label = models.CharField(verbose_name=_("label"), max_length=120)
    template = models.CharField(
        verbose_name=_("Template"),
        choices=get_templates(),
        default=TEMPLATE_DEFAULT,
        max_length=255,
    )
    div_id = models.CharField(
        verbose_name=_("Div ID"),
        max_length=100,
        help_text=_("The third item provided by google for the slot, e.g. 'div-gpt-ad-12345-0'")
    )
    attributes = AttributesField(
        verbose_name=_("Attributes"), blank=True, excluded_keys=["href", "target", "id"]
    )

    class Meta:
        app_label = 'djangocms_ads'
        verbose_name = _("advert plugin model")
        verbose_name_plural = _("advert plugin models")

    def __str__(self) -> str:
        return self.label
