# Generated by Django 3.2 on 2021-05-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_alter_worktype_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worktype',
            options={'verbose_name': 'Work type', 'verbose_name_plural': 'B - Work types'},
        ),
        migrations.AlterField(
            model_name='work',
            name='list_description',
            field=models.TextField(blank=True),
        ),
    ]
