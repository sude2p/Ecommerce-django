# Generated by Django 5.0.6 on 2024-06-27 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descritption',
            new_name='description',
        ),
    ]
