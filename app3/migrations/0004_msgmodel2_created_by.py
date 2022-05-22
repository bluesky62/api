# Generated by Django 4.0.4 on 2022-05-21 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app3', '0003_msgmodel2'),
    ]

    operations = [
        migrations.AddField(
            model_name='msgmodel2',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_by',
                                    to='app3.msgmodel'),
            preserve_default=False,
        ),
    ]