# Generated by Django 3.2.3 on 2022-02-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_missing_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missing',
            name='img',
            field=models.ImageField(default='media/missing-people/park.JPG', upload_to='missing-people/'),
        ),
    ]