# Generated by Django 3.1.1 on 2020-09-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
