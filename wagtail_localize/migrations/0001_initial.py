# Generated by Django 2.1.9 on 2019-06-21 09:16

from django.db import migrations, models
import django.db.models.deletion
import wagtail_localize.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=100, unique=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["-is_active", "code"]},
        ),
        migrations.CreateModel(
            name="Locale",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="locales",
                        to="wagtail_localize.Language",
                    ),
                ),
            ],
            options={
                "ordering": [
                    "-is_active",
                    "-region__is_default",
                    "region__name",
                    "language__code",
                ]
            },
            managers=[("objects", wagtail_localize.models.LocaleManager())],
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=100, unique=True)),
                ("is_default", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("languages", models.ManyToManyField(to="wagtail_localize.Language")),
            ],
            options={"ordering": ["-is_active", "-is_default", "name"]},
        ),
        migrations.AddField(
            model_name="locale",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="locales",
                to="wagtail_localize.Region",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="locale", unique_together={("region", "language")}
        ),
    ]
