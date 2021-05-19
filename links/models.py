from django.db import models

class Sistema(models.Model):
    """ Sistema para clasificar """

    sistema = models.CharField(max_length=200, verbose_name="Sistema")

    def __str__(self):
        return self.sistema

class Link(models.Model):
    """ Enlaces acortados """

    nombre = models.CharField(max_length=250, verbose_name="Título")
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE, verbose_name="Sistema")
    enlace = models.URLField(verbose_name="Enlace a acortar")

    def __str__(self):
        return self.nombre