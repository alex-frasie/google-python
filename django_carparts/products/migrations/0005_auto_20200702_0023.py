# Generated by Django 3.0.8 on 2020-07-01 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200702_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
