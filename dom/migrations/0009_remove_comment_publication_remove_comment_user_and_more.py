# Generated by Django 5.0.4 on 2024-05-01 16:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dom", "0008_remove_codepublication_likes_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="publication",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="user",
        ),
        migrations.DeleteModel(
            name="CodePublication",
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
    ]
