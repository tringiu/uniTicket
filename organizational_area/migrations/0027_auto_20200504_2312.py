# Generated by Django 3.0.5 on 2020-05-04 21:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizational_area', '0026_usermanagestructure'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserManageStructure',
            new_name='UserManageOrganizationalStructure',
        ),
    ]