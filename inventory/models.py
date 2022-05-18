from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext as _
# from django.conf import settings
# Create your models here.
from django.utils.text import slugify
import order
from django.db.models.signals import post_save, pre_save
from location.models import Commune
class WareHouseManager(models.Manager):
    def principale(self):
        return WareHouse.objects.filter(is_default=True).first()

class Brand(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nom')
    actif = models.BooleanField(verbose_name='actif', default=True)
    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("inventoy:brand_detail", kwargs={"pk": self.pk})

class Category(MPTTModel):
    name  = models.CharField( max_length=150, verbose_name='Nom')
    slug  = models.SlugField( max_length=150, unique= True, verbose_name='URL')
    order  = models.IntegerField(verbose_name='ordre', null=True, blank=True)
    actif = models.BooleanField(verbose_name='actif', default=True)
    icon  = models.ImageField(upload_to='images/categories', null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("inventoy:category_detail", kwargs={"pk": self.pk})

class Product(models.Model):
    name         = models.CharField( max_length=200, verbose_name='Nom')
    upc           = models.CharField( max_length=200, verbose_name='code article')
    slug         = models.SlugField( max_length=150, unique= True, verbose_name='URL')
    reference    = models.CharField( max_length=200, verbose_name='Référence / code a bar', unique=True, blank=True, null=True)
    category     = TreeForeignKey(Category, verbose_name="Catégorie",related_name="products" ,on_delete=models.CASCADE, blank=True, null=True)
    brand        = models.ForeignKey(Brand, related_name="brand_products", on_delete=models.CASCADE, blank=True, null=True)
    text         = models.TextField(verbose_name='petit text', blank=True, null=True)
    price        = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    old_price    = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Ancien prix",blank=True, null=True)
    buy_price    = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="prix d'achat",blank=True, null=True)
    actif        = models.BooleanField(verbose_name='actif', default=True) 
    new          = models.BooleanField(verbose_name='Nouveau', default=False)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("inventoy:product_detail", kwargs={"pk": self.pk})


class WareHouse(models.Model):
    name         = models.CharField( max_length=200, verbose_name='Nom du revendeur/point de stockage')
    address      = models.CharField( max_length=200, verbose_name='address')
    actif        = models.BooleanField(verbose_name='actif', default=False)
    is_default   = models.BooleanField(verbose_name='Dépot principale', default=False)
    commune      = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True, blank=True)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)

    objects     = models.Manager()
    centrale     = WareHouseManager()

    class Meta:
        verbose_name = _("WareHouse")
        verbose_name_plural = _("WareHouses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("inventoy:wareHouse_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.is_default = True
        update_default = WareHouse.objects.all().exclude(id=self.id).update(is_default=False)
        super(WareHouse, self).save(*args, **kwargs)


class WareHouseItem(models.Model):
    product   = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE, blank=True, null=True)
    quantity  = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    location = models.ForeignKey(WareHouse, related_name="depot", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _("WareHouseItem")
        verbose_name_plural = _("WareHouseItems")

    def __str__(self):
        return  str(self.product)

    def get_absolute_url(self):
        return reverse("inventoy:wareHouseItem_detail", kwargs={"pk": self.pk})




def product_created_signal(sender, instance, created,**kwargs):
    if created:
        warehouses = WareHouse.objects.all()
        for warehouse in warehouses:
            item = WareHouseItem.objects.get_or_create(product= instance, location=warehouse, quantity=0)
        instance.save()
post_save.connect(product_created_signal, sender=Product)
