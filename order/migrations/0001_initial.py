# Generated by Django 4.0.3 on 2022-03-27 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nom')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Prenom')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Adresse')),
                ('phone', models.CharField(max_length=25, verbose_name='Téléphone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('order_type', models.CharField(blank=True, choices=[('BC', 'Bon de commande'), ('FF', 'Facture finale'), ('BL', 'Bon de livraison')], max_length=2, null=True, verbose_name='type de commande')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_delivered', models.BooleanField(default=False)),
                ('is_cib', models.BooleanField(default=False)),
                ('cib_order_code', models.CharField(blank=True, max_length=2, null=True, verbose_name='code de commande cib')),
                ('coupon', models.CharField(blank=True, max_length=2, null=True, verbose_name='coupon')),
                ('is_return', models.BooleanField(default=False)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='remise')),
                ('delivery_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='cout de livraison')),
                ('note', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
                ('commune', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='location.commune')),
                ('delivery_man', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_orders', to=settings.AUTH_USER_MODEL, verbose_name='livreur')),
            ],
            options={
                'verbose_name': 'ClientOrder',
                'verbose_name_plural': 'ClientOrders',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nom du fournisseur')),
                ('adress', models.CharField(blank=True, max_length=150, null=True, verbose_name='Adresse du fournisseur')),
                ('rc_code', models.CharField(blank=True, max_length=150, null=True, verbose_name='numéro du registre de commerce')),
                ('art_code', models.CharField(blank=True, max_length=150, null=True, verbose_name="numéro d'article")),
                ('nif_code', models.CharField(blank=True, max_length=150, null=True, verbose_name='numéro identité fiscale')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
            ],
            options={
                'verbose_name': 'supplier',
                'verbose_name_plural': 'suppliers',
            },
        ),
        migrations.CreateModel(
            name='SupplyOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supply_type', models.CharField(blank=True, choices=[('BC', 'Bon de commande'), ('BR', 'Bon de récéption')], max_length=2, null=True, verbose_name='type de commande')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_received', models.BooleanField(default=False)),
                ('is_return', models.BooleanField(default=False)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='remise')),
                ('delivery_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='cout de livraison')),
                ('note', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supply_orders', to='inventory.warehouse', verbose_name='receiver')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_orders', to='order.supplier', verbose_name='sender')),
            ],
            options={
                'verbose_name': 'supply_order',
                'verbose_name_plural': 'supply_orders',
            },
        ),
        migrations.CreateModel(
            name='WareHouseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', models.CharField(blank=True, choices=[('BC', 'Bon de commande'), ('FF', 'Facture finale'), ('BL', 'Bon de livraison')], max_length=2, null=True, verbose_name='type de commande')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='numéro')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_delivered', models.BooleanField(default=False)),
                ('is_return', models.BooleanField(default=False)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='remise')),
                ('delivery_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='cout de livraison')),
                ('note', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
                ('delivery_man', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='internal_orders', to=settings.AUTH_USER_MODEL, verbose_name='livreur')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_orders', to=settings.AUTH_USER_MODEL, verbose_name='receiver')),
            ],
            options={
                'verbose_name': 'WareHouseOrder',
                'verbose_name_plural': 'WareHouseOrders',
            },
        ),
        migrations.CreateModel(
            name='WareHouseOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='quantité')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='prix')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.warehouseorder', verbose_name='commande')),
                ('warehouse_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_order_items', to='inventory.warehouseitem', verbose_name='produit')),
            ],
        ),
        migrations.CreateModel(
            name='SupplyOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='quantité')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='prix')),
                ('note', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supply_order_items', to='order.supplyorder', verbose_name='commande')),
                ('warehouse_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.warehouseitem', verbose_name='produit')),
            ],
        ),
        migrations.CreateModel(
            name='ClientOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='quantité')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='prix')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_orders', to='order.clientorder', verbose_name='commande')),
                ('warehouse_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_order_items', to='inventory.warehouseitem', verbose_name='produit')),
            ],
        ),
    ]
