# Italia Sport
## Project Description
Il portale Italia Sport è stato sviluppato come progetto finale del corso "Applicazioni Web e Cloud" tenuto dal Prof. Claudio Ardagna @Università degli studi di Milano.
Questo progetto ha come scopo quello di esplorare ed imparare ad utilizzare le più moderne tecnologie, linguaggi e costrutti utilizzati nella costruzine di applicazioni web moderne; di seguito un breve elenco delle princiali tecnologie utilizzate:
- HTML5
- CSS3
- LocalStorage
- JavaScript
- AngularJS
- NodeJS
- Django REST Framework
- SQLite
- JSON

### Requisiti
Il progetto si pone l’obiettivo di costruire un’applicazione REST per supportare lo sviluppo dell’applicazione web per l’associazione sportiva Italia Sport; quest'ultima raggruppa un insieme di 11 sportivi ognuno con il nome di un/a grande sportivo/sportiva del passato.
L’applicazione deve considerare:
– gestione degli sportivi;
- gestione delle attività dell’Italia Sport.

Di seguito sono analizzate in dettaglio le caratteristiche dei due macro-scenari introdotti.
Il primo scenario consiste nella gestione degli sportivi e delle attivita` dell’associazione sportiva giorno per giorno. Le attivita` sono gestite in finestre temporali di una settimana e contengono l’associazione tra sportivo, attivita`, e programma delle attivita` future. Per ogni sportivo si vogliono gestire informazioni quali altezza, peso, età, statistiche, carriera, etc.
Ogni attività contiene informazioni quali ad esempio titolo, breve descrizione, avversario, statistiche avversario, luogo e orario. In base al tipo di attivita` vengono associate informazioni sul prezzo, su eventuali sconti o facilitazioni. Infine, si vogliono gestire informazioni relative ai risultati e ai punteggi per ogni singola attivita`, incluso classifica e statistiche.

### Scelte Implementative
Per "imparare" il più possibile si è scelto di non utilizzare template predefiniti es. Bootstrap durante lo sviluppo della parte di front-end e di creare un portale sicuramente non accantivante dal punto di vista grafico ma che potesse mettere in risalto le varie tecnologie studiate durante il corso.

## Technical Details
Il backend dell'applicativo è stato realizzato utilizzando il paradigma REST (Representational state transfer) ed il linguaggio di programmazione python, sul quale, per l'appunto, si basa il Framework Django REST.

'''
"REST (REpresentational State Transfer) is an architectural style to build services on top of the Web. REST simplifies interaction with a web-based system via simplified URLs, instead of complex HTTP requests."  
'''
### Main Features