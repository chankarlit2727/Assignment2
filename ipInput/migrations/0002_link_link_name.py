# Generated by Django 2.2 on 2022-07-19 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipInput', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='link_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
