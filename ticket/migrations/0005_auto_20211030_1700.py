# Generated by Django 3.2.8 on 2021-10-30 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_auto_20211030_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='opened',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='responded',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='updated',
        ),
    ]