# Generated by Django 4.0.3 on 2022-04-07 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/profiles'),
        ),
        migrations.AddField(
            model_name='user',
            name='Pseudo',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Role',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
