# Generated by Django 3.2.3 on 2021-05-15 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20210515_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='vip',
            new_name='VIP',
        ),
    ]