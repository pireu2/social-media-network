# Generated by Django 4.2.4 on 2023-09-13 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0002_post_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Like",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="liked",
                        to="network.post",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="usrlikes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
