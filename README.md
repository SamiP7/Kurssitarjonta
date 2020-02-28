# Kurssitarjonta
## Aihe

Sovellus pitää yllä kuvitteellisen oppilaitoksen kurssitarjontaa. Jokainen kurssi kuuluu tiettyyn aihepiiriin ja näitä voidaan järjestää useampaan kertaan vuodessa. Kurssilla on oma esitteensä, jossa mainitaan esim. aika, paikka, sisältö ja opettajat. Kuka tahansa voi osallistua kurssille ja tutkia esitteitä kursseista. Osallistumista varten on henkilön maksettava varausmaksu. Halunnut osallistuja laittaa varauslomakkeeseen tili-, viitenumeron ja maksun määrän. Kun varaus on maksettu, on henkilö osa kyseistä kurssia. Maksutus ei ole osa tätä sovellusta.

## Hahmotelma tietokannasta


![](https://github.com/SamiP7/Kurssitarjonta/blob/master/documentation/pictures/kaavio.png)

[**Sovellukseen toteutettu tietokanta**](https://github.com/SamiP7/Kurssitarjonta/blob/master/documentation/pictures/toteutettu_tietokanta.png)

### Käyttötapaukset, create table-lauseet ja sql-kyselyitä

[Löytyy painamalla tätä linkkiä](https://github.com/SamiP7/Kurssitarjonta/blob/master/documentation/toiminnallisuuksia.md)


### Heroku-linkki

https://kurssitarjonta-7.herokuapp.com/

Valmis käyttäjä ohjelmaan(omankin voi luoda admin tunnuksilla): 
* sähköposti: **admin@admin.com**
* salasana: **admin**

Jos haluat välttämättä asentaa ohjelman omalle koneellesi, niin sen pitäisi onnistua helposti vain lataamalla githubista master-branch painamalla etusivulta vihreää clone or download nappulaa. Ohjelman ajamiseksi joudut ensin terminaalista menemään kohdekansioon, jonka jälkeen ajat komennon `pip install -r requirements.txt`, jonka jälkeen joudut vielä ajamaan komennon `source venv/bin/activate` (`venv\scripts\activate`-Windows käyttöjärjestelmässä). Sitten ohjelman voi käynnistää komennolla `python run.py` ja ohjelma voi sitten löytyä osoitteesta [http://localhost:5000/](http://localhost:5000/).
### Käyttöohje

Jos et halua käyttää tarjottua järjestelmänvalvoja käyttäjää voit helposti luoda omasi painamalla **Register** nappulaa. Tässä sinun pitää vain pistää sähköpostiosoite oikeassa muodossa, kuinka tahansa lyhyt nimi, salasana joka on vähintään 5 merkkiä pitkä ja puhelinnumero jonka voi pitää täysin tyhjänä. Kun sinulla on tunnukset voit kirjautua sisään painamalla **Login** nappulaa. Tästä olet sitten päässyt etusivulle, jossa voit valita aiheen laatikosta, jos valikko on tyhjä voit luoda uuden järjestelmänvalvoja käyttäjällä painamalla **Add a new topic**. Kun olet valinnut aiheen, painamalla search:ia näet kaikki tällä hetkellä olevat kurssit kyseisestä aiheesta. Tästä voit vielä katsoa tarkemmin kurssin tietoja painamalla nappia **Info about the course**, joka on kurssin vieressä. Näiden aikana voit helposti palata etusivulle painalla joko vasemassa yläkulmassa CourseSelection tai nappuloita hakujen yläpuolella. Kurssin voit luoda painamalla **Add a new course** nappia. Kurssia luodessasi täytyy sinun valita kurssin aihe, joten katso että sinulla on tämä jo luotuna ennen kurssin luontia. Kurssille on myös annettava nimi, alku-, loppupäivämäärä(muodossa yyyy-mm-dd), opettajat ja opetuspaikka. Kuvauksen voi halutessaan jättää tyhjäksi. Kun sovelluksessa on kursseja, voit ilmoittautua niille, joko etusivulla olevan haun kautta tai **List courses** nappulan kautta, jonka takana näet kaikki kurssit. Kun ilmottaudut kurssille, on sinun annettava tilinumero, viitenumero ja maksun määrä lomakkeeseen. Tämä ei varsinaisesti ole osa projektia, joten syötteeksi kelpaa mikä tahansa. Jos käyttäjä yrittää ilmoittautua uudestaan kurssiin, johon hänellä on jo varaus, niin vanha pysyy edelleen voimassa. Myös jos käyttäjä yrittää tehdä varauksen kurssille jossa hän on jo, ja on poistanut varauksensa, ei uutta varausta enää tehdä. Kun ilmoittautuminen on tehty, menee se varauksiin, joihin pääset napista **Reservations**. Täällä voit poistaa tai maksaa varauksen. Kun maksat tämän, olet ilmoittatunut kyseiselle kurssille. Voit nähdä kaikki kurssit joihin olet ilmoittautunut napista **My courses**. Täällä voit poistua kurssilta, jolloin myös kurssin varaus poistuu samalla, sekä nähdä montako varausta sinulla on maksamatta, jos olet ilmoittautunut ainakin yhdelle kursille. Huom. ilmoittautuminen ei poistu jos poistat varauksen.

Vain järjestelmänvalvoja voi lisätä aiheita ja kursseja. Järjestelmänvalvoja voi myös selata keitä käyttäjiä on ilmoittatunut kurssille ja tarpeen vaatiessa myös poistaa henkilön ilmoittautumisen, jolloin myös hänen varauksensa poistuu. Tämä onnistuu painamalla **Delete attendance**, kun järjestelmänvalvoja on selannut kurssin, josta hän tahtoo käyttäjän poistaa.
