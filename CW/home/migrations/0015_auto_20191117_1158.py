# Generated by Django 2.2.4 on 2019-11-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20191117_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuinfo',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
