# Generated by Django 5.0.6 on 2024-06-27 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_category_cat_image_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, upload_to='categories/'),
        ),
    ]
