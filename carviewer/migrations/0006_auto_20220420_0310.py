# Generated by Django 3.2.3 on 2022-04-20 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carviewer', '0005_alter_cartype_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='car_image',
            field=models.ImageField(blank=True, upload_to='cars/%Y/%M/%D'),
        ),
        migrations.AlterField(
            model_name='carreview',
            name='car_image',
            field=models.ImageField(blank=True, upload_to='cars/%Y/%M/%D'),
        ),
        migrations.AlterField(
            model_name='cartype',
            name='car_image',
            field=models.ImageField(blank=True, upload_to='cars/%Y/%M/%D'),
        ),
    ]