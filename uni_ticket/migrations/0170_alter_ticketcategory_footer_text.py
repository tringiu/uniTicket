# Generated by Django 3.2.7 on 2021-11-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0169_alter_ticketcategory_footer_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticketcategory",
            name="footer_text",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Testo in calce per versione stampabile",
            ),
        ),
    ]