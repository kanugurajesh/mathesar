# Generated by Django 3.1.14 on 2022-03-29 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathesar', '0026_auto_20220126_1347'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='table',
            constraint=models.UniqueConstraint(fields=('oid', 'schema'), name='unique_table'),
        ),
    ]
