# Generated by Django 3.2.8 on 2021-10-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_id', models.TextField(max_length=200, verbose_name='Type ID')),
                ('label', models.TextField(max_length=200, verbose_name='Type Label')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Type Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Type Updated')),
                ('last_ticket', models.DateTimeField(auto_now=True, verbose_name='Type Last Ticket')),
                ('tickets', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ticket Count')),
            ],
        ),
    ]