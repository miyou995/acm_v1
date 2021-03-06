# Generated by Django 4.0.3 on 2022-04-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_rename_name_supplier_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientorder',
            name='is_defect',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='supplyorder',
            name='is_defect',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='warehouseorder',
            name='is_defect',
            field=models.BooleanField(default=False),
        ),
    ]
