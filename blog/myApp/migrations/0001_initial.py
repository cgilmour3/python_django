# Generated by Django 5.1.1 on 2024-09-24 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=30)),
                ('post_body', models.CharField(max_length=200)),
                ('post_date', models.DateField()),
            ],
        ),
    ]
