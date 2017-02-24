from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator



class Sportivo(models.Model):
    #id = models.SmallIntegerField(primary_key=True)
    nome = models.CharField(blank=False, max_length=20)
    cognome = models.CharField(blank=False, max_length=20)
    sport = models.CharField(blank=False, max_length=20)
    data_nascita = models.DateField(blank=True, default='01/01/1900')
    luogo_nascita = models.CharField(max_length=100, blank=True, default='')
    paese_nascita = models.CharField(max_length=100, blank=True, default='')
    #eta = int((datetime.date.today() - annonascita).days / 365.25)
    altezza = models.FloatField(max_length=3, blank=True)
    peso = models.FloatField(max_length=3, blank=True)
    #foto = models.ImageField(upload_to='img', blank=True)
    foto = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='sportivi', null=False, default='0')

    def __unicode__(self):
        return u"%s %s" % (self.nome, self.cognome)

    class Meta:
        verbose_name_plural = "Sportivi"
        ordering = ('created',)

class Attivita(models.Model):
    #id = models.SmallIntegerField(primary_key=True)
    nome = models.CharField(max_length=20)
    descrizione = models.CharField(max_length=10000)
    data = models.DateTimeField(null=True, blank=True, help_text='formato YYYY-MM-DDThh:mm:ss')
    prezzo = models.FloatField(max_length=5)
    sconto = models.FloatField(max_length=2, blank=True)
    facilitazioni = models.CharField(max_length=10000, blank=True)
    organizzatore = models.ForeignKey(Sportivo,  blank=False, default='0')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='attivita', null=False, default='0')
    #impostare sportivo in modo tale che si veda come lorenzo comi

    def __unicode__(self):
        return u"%s %s" % (self.titolo)

    class Meta:
        verbose_name_plural = "Attivita'"
        ordering = ('created',)

class Risultato(models.Model):
    attivita = models.OneToOneField(Attivita)
    vincitore = models.ForeignKey(Sportivo, blank=False)
    risultato = models.CharField(max_length=10000, blank=True)
    classifica = models.CharField(max_length=10000, blank=True)
    note = models.CharField(max_length=10000, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"Risultato %s" % (self.attivita)

    class Meta:
        verbose_name_plural = "Risultati"
        ordering = ('created',)