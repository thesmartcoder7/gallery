# Generated by Django 4.1.1 on 2022-11-28 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
