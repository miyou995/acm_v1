from django.db import models



class Wilaya(models.Model):
    name           = models.CharField(max_length=40, verbose_name="Wilaya", unique=True)
    relai_delivery = models.DecimalField( max_digits=8, verbose_name="Livraison point de Relais", decimal_places=2, default=0)
    home_delivery  = models.DecimalField( max_digits=10, verbose_name="Livraison à domicile", decimal_places=2, default=0)
    active         = models.BooleanField(default=True, verbose_name="Livraison Active")
    created        = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated        = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    class Meta:
        verbose_name = "Wilaya"
        verbose_name_plural = "1. Wilayas"

    def __str__(self):
        return self.name

class Commune(models.Model):
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, verbose_name="Wilaya")
    name = models.CharField(max_length=30, verbose_name="Commune")
    # active = models.BooleanField(default=True, verbose_name="Livraison Active")
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    class Meta:
        verbose_name = "Commune"
        verbose_name_plural = "2. Communes"        

    def __str__(self):
        return self.name
