# Generated by Django 3.2 on 2022-11-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pegi',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
