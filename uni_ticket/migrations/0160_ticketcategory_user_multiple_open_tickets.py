# Generated by Django 3.2 on 2021-09-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0159_auto_20210305_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketcategory',
            name='user_multiple_open_tickets',
            field=models.BooleanField(default=True, verbose_name='Gli utenti possono aprire più richieste contemporaneamente'),
        ),
    ]
