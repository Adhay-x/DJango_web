# Generated by Django 4.1.7 on 2023-04-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=50)),
                ('quantity', models.CharField(max_length=1024)),
                ('desc', models.TextField()),
            ],
        ),
    ]
