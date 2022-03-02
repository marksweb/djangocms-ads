from __future__ import annotations

HELPER_SETTINGS = {
    "TEST_RUNNER": "app_helper.pytest_runner.PytestTestRunner",
    "SECRET_KEY": "djangocms-ads-test-suite",
    "USE_TZ": False,
    "TIME_ZONE": "Europe/London",
    "INSTALLED_APPS": [
        "djangocms_attributes_field",
        "djangocms_ads",
    ],
    "MIGRATION_MODULES": {
        "auth": None,
        "cms": None,
        "menus": None,
        "djangocms_ads": None,
    },
    "CMS_PERMISSION": True,
    "LANGUAGES": (
        ("en", "English"),
    ),
    "CMS_LANGUAGES": {
        1: [
            {"code": "en", "name": "English"},
        ],
    },
    "LANGUAGE_CODE": "en",
    "DEFAULT_AUTO_FIELD": "django.db.models.AutoField",
}


def run() -> None:
    from app_helper import runner

    runner.cms("djangocms_ads", extra_args=[])


if __name__ == "__main__":
    run()
