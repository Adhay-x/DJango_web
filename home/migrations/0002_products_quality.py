# Generated by Django 4.1.7 on 2023-04-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='quality',
            field=models.CharField(default=True, max_length=50),
            preserve_default=False,
        ),
    ]
