# Generated by Django 3.1.1 on 2020-09-15 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_merge_20200915_1307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('index',), 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='eventcategory',
            options={'ordering': ('index',), 'verbose_name': 'Event Category', 'verbose_name_plural': 'Event Categories'},
        ),
        migrations.AddField(
            model_name='event',
            name='index',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
