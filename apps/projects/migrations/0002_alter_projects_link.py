# Generated by Django 4.1.3 on 2023-10-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='link',
            field=models.URLField(max_length=500, verbose_name='ссылка'),
        ),
    ]
