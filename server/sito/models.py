from django.db import models


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

#sportivo = Sportivo(nome= , cognome= , sport= , data_nascita= , luogo_nascita= , paese_nascita=  ,
    # altezza= , peso= , foto= )
#esempio: sportivo = Sportivo(nome="Roberto" , cognome="Baggio" , sport="calcio" , data_nascita="1977-02-18" ,
    # luogo_nascita="Caldogno" , paese_nascita="ITA"  , altezza=174 , peso=73 ,
    # foto="https://upload.wikimedia.org/wikipedia/it/1/1b/Roberto_Baggio_-_Italia_'90.jpg")

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

#attivita = Attivita(nome= , descrizione= , data= , prezzo= , sconto= , facilitazioni= , organizzatore= )
#esempio: attivita = Attivita(nome="Canestro Solidale" , descrizione="partita di basket amichevole" ,
    # data="2017-02-28T18:22:00" , prezzo=17.90 , sconto=0 , facilitazioni="accesso per disabili" , organizzatore=jordan)

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


class Test(models.Model):
    nome = models.CharField(max_length=10, blank=False)

    def __unicode__(self):
        return u"Test %s" % (self.nome)
