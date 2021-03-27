from django.db import models

# Create your models here.
class Accord(models.Model):
    nom = models.CharField(default="", max_length=100)
    accords_proche = models.ManyToManyField("self", blank=True)

    class Meta:
        verbose_name = "Accord"
        verbose_name_plural = "Accords"
        ordering = ['id']

    def __str__(self):
        return self.nom


class Message_facebook(models.Model):
    facebook_id = models.CharField(default="", max_length=200)
    message = models.TextField(default="", blank=True, null=True)
    date_envoie = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = "Message facebook"
        verbose_name_plural = "Messages facebook"
        ordering = ['id']

    def __str__(self):
        return self.facebook_id