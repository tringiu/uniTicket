# Generated by Django 3.0.3 on 2020-03-23 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("uni_ticket", "0068_auto_20200320_1902"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticketassignment",
            name="taken_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="taken_by_operator",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="ticketassignment",
            name="taken_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]