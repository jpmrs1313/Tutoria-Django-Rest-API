# Generated by Django 4.1.7 on 2023-02-27 18:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("building", models.CharField(max_length=64)),
            ],
            options={
                "unique_together": {("name", "building")},
            },
        ),
    ]