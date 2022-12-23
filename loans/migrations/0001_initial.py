# Generated by Django 4.1.4 on 2022-12-22 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Borrower",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Investor",
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
                ("name", models.CharField(max_length=200)),
                ("balance", models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Loan",
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
                ("status", models.CharField(max_length=200)),
                ("amount", models.IntegerField(max_length=100)),
                ("period", models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Offer",
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
                ("LoanID", models.IntegerField(max_length=100)),
                ("InvestorID", models.IntegerField(max_length=100)),
                ("BorrowerID", models.IntegerField(max_length=100)),
                ("AIR", models.IntegerField(max_length=100)),
                ("status", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Payments",
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
                ("LoanID", models.IntegerField(max_length=100)),
                ("status", models.CharField(max_length=200)),
                ("amount", models.IntegerField(max_length=100)),
            ],
        ),
    ]
