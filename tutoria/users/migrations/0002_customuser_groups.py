# Generated by Django 4.1.7 on 2023-05-08 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="groups",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="auth.group",
            ),
        ),
    ]
