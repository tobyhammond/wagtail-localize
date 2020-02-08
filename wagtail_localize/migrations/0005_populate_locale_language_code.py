# Generated by Django 2.2.9 on 2020-01-28 18:05

from django.db import migrations


def populate_locale_language_code(apps, schema_editor):
    Locale = apps.get_model("wagtail_localize.Locale")

    for locale in Locale.objects.all():
        locale.language_code = locale.language.code
        locale.save(update_fields=["language_code"])


class Migration(migrations.Migration):

    dependencies = [
        ("wagtail_localize", "0004_locale_language_code"),
    ]

    operations = [
        migrations.RunPython(populate_locale_language_code),
    ]