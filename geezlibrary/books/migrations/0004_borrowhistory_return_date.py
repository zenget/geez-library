# Generated by Django 3.2.4 on 2021-06-10 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210610_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowhistory',
            name='return_date',
            field=models.DateTimeField(null=True),
        ),
    ]
