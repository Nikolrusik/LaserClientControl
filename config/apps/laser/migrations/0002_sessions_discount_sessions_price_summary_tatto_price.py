# Generated by Django 4.1.3 on 2022-12-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("laser", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sessions",
            name="discount",
            field=models.IntegerField(blank=True, null=True, verbose_name="Discount"),
        ),
        migrations.AddField(
            model_name="sessions",
            name="price_summary",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Price summary"
            ),
        ),
        migrations.AddField(
            model_name="tatto",
            name="price",
            field=models.FloatField(blank=True, null=True, verbose_name="Price"),
        ),
    ]