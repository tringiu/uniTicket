# Generated by Django 2.2.4 on 2019-09-04 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0047_auto_20190904_0941"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ticket",
            options={
                "ordering": ["is_closed", "priority", "is_taken", "-created", "code"],
                "verbose_name": "Ticket",
                "verbose_name_plural": "Ticket",
            },
        ),
        migrations.RenameField(
            model_name="ticket",
            old_name="is_preso_in_carico",
            new_name="is_taken",
        ),
    ]