# Generated by Django 2.2.4 on 2019-08-07 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0043_auto_20190807_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcategory',
            name='allow_employee',
            field=models.BooleanField(default=False, verbose_name="Accessibile ai dipendenti dell'organizzazione"),
        ),
    ]