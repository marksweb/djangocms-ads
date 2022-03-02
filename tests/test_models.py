from __future__ import annotations

from django.test import TestCase

from djangocms_ads.models import AdSlotPlugin, AdvancedAdContainerPlugin, AdvertPlugin, SimpleAdContainerPlugin


class ModelTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_advertplugin_instance(self):
        AdvertPlugin.objects.create(
            label="test advert",
            div_id="test-id-123",
        )
        instance = AdvertPlugin.objects.all()
        self.assertEqual(instance.count(), 1)
        instance = AdvertPlugin.objects.first()
        self.assertEqual(instance.label, "test advert")
        self.assertEqual(instance.div_id, "test-id-123")
        # test string repr
        self.assertEqual(str(instance), "test advert")

    def test_advanced_instance(self):
        AdvancedAdContainerPlugin.objects.create(
            internal_name="Test advanced container",
            content="",
        )
        instance = AdvancedAdContainerPlugin.objects.all()
        self.assertEqual(instance.count(), 1)
        instance = AdvancedAdContainerPlugin.objects.first()
        # test strings
        self.assertEqual(str(instance), "Test advanced container")

    def test_simple_instance(self):
        SimpleAdContainerPlugin.objects.create(
            internal_name="Test simple container",
        )
        instance = SimpleAdContainerPlugin.objects.all()
        self.assertEqual(instance.count(), 1)
        instance = SimpleAdContainerPlugin.objects.first()
        # test strings
        self.assertEqual(str(instance), "Test simple container")

    def test_adslot_instance(self):
        AdSlotPlugin.objects.create(
            internal_name="Test ad slot",
            ad_unit_path="/1234/testing",
            sizes="[10, 20]",
            div_id="test-ad-1234"
        )
        instance = AdSlotPlugin.objects.all()
        self.assertEqual(instance.count(), 1)
        instance = AdSlotPlugin.objects.first()
        # test strings
        self.assertEqual(str(instance), "Test ad slot")
