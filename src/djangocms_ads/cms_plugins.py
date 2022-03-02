from __future__ import annotations

from typing import Any

from django.utils.translation import gettext_lazy as _

from cms.models import Placeholder
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import AdSlotPlugin, AdvancedAdContainerPlugin, AdvertPlugin, SimpleAdContainerPlugin

__all__ = ["Advert"]


@plugin_pool.register_plugin
class AdvancedAdContainer(CMSPluginBase):
    """Advanced ad container plugin"""
    module = _("Adverts")
    name = _("Advert Container (advanced)")
    model = AdvancedAdContainerPlugin

    def get_render_template(self, context: dict[Any, Any], instance: AdvancedAdContainerPlugin,
                            placeholder: Placeholder) -> str:
        return f"djangocms_ads/{instance.template}/container_advanced.html"


@plugin_pool.register_plugin
class SimpleAdContainer(CMSPluginBase):
    """Simple ad container plugin"""
    module = _("Adverts")
    name = _("Advert Container")
    model = SimpleAdContainerPlugin
    allow_children = True
    child_classes = ['AdSlot']

    def get_render_template(self, context: dict[Any, Any], instance: SimpleAdContainerPlugin,
                            placeholder: Placeholder) -> str:
        return "djangocms_ads/default/container_simple.html"


@plugin_pool.register_plugin
class AdSlot(CMSPluginBase):
    """Ad slot plugin"""
    module = _("Adverts")
    name = _("Advert Slot")
    model = AdSlotPlugin
    require_parent = True
    parent_classes = ['SimpleAdSlotContainer']

    def get_render_template(self, context: dict[Any, Any], instance: AdSlotPlugin, placeholder: Placeholder) -> str:
        return f"djangocms_ads/{instance.template}/ad_slot.html"


@plugin_pool.register_plugin
class Advert(CMSPluginBase):
    """Advert plugin"""
    module = _("Adverts")
    name = _("Advert")
    model = AdvertPlugin

    def get_render_template(self, context: dict[Any, Any], instance: AdvertPlugin, placeholder: Placeholder) -> str:
        return f"djangocms_ads/{instance.template}/advert.html"
