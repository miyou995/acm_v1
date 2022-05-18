# Generated by Django 4.0.3 on 2022-04-20 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_warehouseorderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseorderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.warehouseorder', verbose_name='Commande'),
        ),
    ]
