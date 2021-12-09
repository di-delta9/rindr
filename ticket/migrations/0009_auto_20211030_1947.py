# Generated by Django 3.2.8 on 2021-10-30 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0008_remove_ticket_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ticket Updated'),
        ),
    ]
