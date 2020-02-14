# Kurssitarjonta
## Aihe

Sovellus pitää yllä kuvitteellisen oppilaitoksen kurssitarjontaa. Jokainen kurssi kuuluu tiettyyn aihepiiriin ja näitä voidaan järjestää useampaan kertaan vuodessa. Kurssilla on oma esitteensä, jossa mainitaan esim. aika, paikka, sisältö ja opettajat. Kuka tahansa voi osallistua kurssille ja tutkia esitteitä kursseista. Osallistumista varten on henkilön maksettava varausmaksu. Halunneille osallistujille ilmoitetaan tilinumero, viitenumero ja maksun määrä. Henkilö voi halutessaan pyytää laskua varausmaksusta. Maksutus ei ole osa tätä sovellusta.

## Hahmotelma tietokannasta


![](https://github.com/SamiP7/Kurssitarjonta/blob/master/documentation/pictures/kaavio.png)

### Käyttötapaukset

[Löytyy painamalla tätä linkkiä](https://github.com/SamiP7/Kurssitarjonta/blob/master/documentation/toiminnallisuuksia.md)


### Heroku-linkki

https://kurssitarjonta-7.herokuapp.com/

Ohjelmassa on nykyään erillinen järjestelmänvalvoja käyttäjä, jonka kirjautumistunnukset ovat: 
* sähköposti: **admin@admin.com**
* salasana: **admin**

Jos haluat välttämättä asentaa ohjelman omalle koneellesi, niin sen pitäisi onnistua helposti vain lataamalla githubista master-branch painamalla etusivulta vihreää clone or download nappulaa. Ohjelman ajamiseksi joudut ensin terminaalista menemään kohdekansioon, jonka jälkeen ajat komennon `pip install -r requirements.txt`, jonka jälkeen joudut vielä ajamaan komennon `venv\scripts\activate`. Sitten ohjelman voi käynnistää komennolla `python run.py` ja ohjelma voi sitten löytyä osoitteesta [http://localhost:5000/](http://localhost:5000/).
### Käyttöohje

Jos et halua käyttää tarjottua järjestelmänvalvoja käyttäjää voit helposti luoda omasi painamalla **register** nappulaa. Tässä sinun pitää vain pistää sähköpostiosoite oikeassa muodossa, kuinka tahansa lyhyt nimi, salasana joka on vähintään 5 merkkiä pitkä ja puhelinnumero jonka voi pitää täysin tyhjänä. Kun sinulla on tunnukset voit kirjautua sisään painamalla **login** nappulaa. Tästä olet sitten päässyt etusivulle, jossa voit valita aiheen laatikosta, ja kun painat search:ia näet kaikki tällä hetkellä olevat kurssit kyseisestä aiheesta. Tästä voit vielä katsoa tarkemmin kurssin tietoja painamalla nappia kurssin vieressä. Näiden aikana voit helposti palata etusivulle painalla joko vasemassa yläkulmassa CourseSelection tai nappuloita hakujen yläpuolella. Sivun ylälaidassa olevat nappulat tekevät oikeastaan juuri siinä sanotunkin. Voit myös List coursesta ilmoittautua kursseille. My coursesta pääset katsomaan kursseja joille olet ilmoittautunut. Muut metodit ovatkin sitten järjestelmänvalvojan käytössä ja nämäkin oikeastaan itsestäänselvyyksiä.
