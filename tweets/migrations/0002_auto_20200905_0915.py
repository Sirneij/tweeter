# Generated by Django 3.1.1 on 2020-09-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]