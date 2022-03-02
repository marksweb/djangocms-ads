from __future__ import annotations

from cms.api import add_plugin, create_page
from cms.test_utils.testcases import CMSTestCase


class AdPluginsTestCase(CMSTestCase):

    def setUp(self):
        self.language = "en"
        self.page = create_page(
            title="home",
            template="page.html",
            language=self.language,
        )
        # self.page.publish(self.language)
        self.placeholder = self.page.placeholders.get(slot="content")
        self.superuser = self.get_superuser()

    def tearDown(self):
        self.page.delete()
        self.superuser.delete()

    def test_ad_rendering(self):
        request_url = self.page.get_absolute_url(self.language) + "?toolbar_off=true"

        add_plugin(
            self.page.placeholders.get(slot="content"),
            "SimpleAdContainer",
            self.language,
            internal_name="simple plugin",
            template='default',
        )
        ad_slot = add_plugin(
            self.page.placeholders.get(slot="content"),
            "AdSlot",
            self.language,
            internal_name="render test slot",
            template="default",
            ad_unit_path="/4321/Leaderboard",
            sizes="[300, 250]",
            div_id="div-render-test"
        )
        advert = add_plugin(
            self.page.placeholders.get(slot="content"),
            "Advert",
            self.language,
            label="Test render advert",
            template="default",
            div_id="div-render-test"
        )

        self.page.publish(self.language)
        self.assertEqual(ad_slot.div_id, "div-render-test")
        self.assertEqual(advert.label, "Test render advert")
        self.assertEqual(advert.div_id, "div-render-test")

        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)

        self.assertIn(b"div-render-test", response.content)
