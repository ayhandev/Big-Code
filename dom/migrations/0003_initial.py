# Generated by Django 5.0.4 on 2024-04-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("dom", "0002_delete_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="infa",
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
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("description", models.TextField(verbose_name="Description")),
                ("date", models.DateTimeField(verbose_name="Date and Time")),
            ],
        ),
    ]