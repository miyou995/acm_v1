# Generated by Django 4.0.3 on 2022-04-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='images/categories'),
        ),
    ]
