# Generated by Django 3.0.7 on 2020-06-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0131_auto_20200626_1006"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organizationalstructurewsarchipro",
            name="protocollo_email",
            field=models.EmailField(
                default="amministrazione@pec.unical.it",
                max_length=255,
                verbose_name="E-mail",
            ),
        ),
        migrations.AlterField(
            model_name="ticketcategorywsarchipro",
            name="protocollo_email",
            field=models.EmailField(
                default="amministrazione@pec.unical.it",
                max_length=255,
                verbose_name="E-mail",
            ),
        ),
    ]