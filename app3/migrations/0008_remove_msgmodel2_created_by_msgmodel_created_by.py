# Generated by Django 4.0.4 on 2022-05-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app3', '0007_remove_msgmodel2_created_by_msgmodel2_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msgmodel2',
            name='created_by',
        ),
        migrations.AddField(
            model_name='msgmodel',
            name='created_by',
            field=models.ManyToManyField(to='app3.msgmodel2'),
        ),
    ]
