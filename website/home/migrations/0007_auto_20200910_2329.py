# Generated by Django 3.1.1 on 2020-09-10 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_event_eventcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='eventcategory',
            options={'verbose_name': 'Event Category', 'verbose_name_plural': 'Event Categories'},
        ),
    ]
