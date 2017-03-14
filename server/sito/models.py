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


class Student(models.Model):
    Gennaio = 'Gen'
    Febbraio = 'Feb'
    Marzo = 'Mar'
    Aprile = 'Apr'
    Maggio = 'Mag'
    Giugno = 'Giu'
    Luglio = 'Lug'
    Agosto = 'Ago'
    Settembre = 'Set'
    Ottobre = 'Ott'
    Novembre = 'Nov'
    Dicembre = 'Dic'
    scelta_mesi = (
        (Gennaio, 'Gennaio'),
        (Febbraio, 'Febbraio'),
        (Marzo, 'Marzo'),
        (Aprile, 'Aprile'),
        (Maggio, 'Maggio'),
        (Giugno, 'Giugno'),
        (Luglio, 'Luglio'),
        (Agosto, 'Gennaio'),
        (Settembre, 'Settembre'),
        (Ottobre, 'Ottobre'),
        (Novembre, 'Novembre'),
        (Dicembre, 'Dicembre'),
    )
    year_in_school = models.CharField(
        max_length=3,
        choices=scelta_mesi,
        null=False
    )

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)



class Attivita(models.Model):
    Gennaio = 'Gennaio'
    Febbraio = 'Febbraio'
    Marzo = 'Marzo'
    Aprile = 'Aprile'
    Maggio = 'Maggio'
    Giugno = 'Giugno'
    Luglio = 'Luglio'
    Agosto = 'Agosto'
    Settembre = 'Settembre'
    Ottobre = 'Ottobre'
    Novembre = 'Novembre'
    Dicembre = 'Dicembre'

    Lunedi = 'Lunedi'
    Martedi = 'Martedi'
    Mercoledi = 'Mercoledi'
    Giovedi = 'Giovedi'
    Venerdi = 'Venerdi'
    Sabato = 'Sabato'
    Domenica = 'Domenica'

    scelta_mesi = (
        (Gennaio, 'Gennaio'),
        (Febbraio, 'Febbraio'),
        (Marzo, 'Marzo'),
        (Aprile, 'Aprile'),
        (Maggio, 'Maggio'),
        (Giugno, 'Giugno'),
        (Luglio, 'Luglio'),
        (Agosto, 'Agosto'),
        (Settembre, 'Settembre'),
        (Ottobre, 'Ottobre'),
        (Novembre, 'Novembre'),
        (Dicembre, 'Dicembre'),
    )

    scelta_giorni = (
        (Lunedi, 'Lunedi'),
        (Martedi, 'Martedi'),
        (Mercoledi, 'Mercoledi'),
        (Giovedi, 'Giovedi'),
        (Venerdi, 'Venerdi'),
        (Sabato, 'Sabato'),
        (Domenica, 'Domenica'),
    )

    numEvento = models.IntegerField(null=False)
    giornoEvento = models.CharField(max_length=10, choices=scelta_giorni, null=False)
    meseEvento = models.CharField(max_length=10, choices=scelta_mesi, null=False)
    annoEvento = models.IntegerField(null=False)
    oraEvento = models.TimeField(null=True, blank=True)

    nome = models.CharField(max_length=20)
    descrizione = models.CharField(max_length=10000)
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
