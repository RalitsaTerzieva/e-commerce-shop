# Generated by Django 4.2 on 2023-04-05 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
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
                ("title", models.CharField(max_length=200)),
                ("price", models.FloatField()),
                ("discount_price", models.FloatField()),
                ("category", models.CharField(max_length=200)),
                ("description", models.TextField(max_length=500)),
                ("image", models.CharField(max_length=300)),
            ],
        ),
    ]
