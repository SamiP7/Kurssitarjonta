### Nykyiset toiminnalisuudet

* Järjestelmänvalvoja voi lisätä aiheita, kursseja, sekä muokata, että poistaa niitä.
* Voi luoda uuden käyttäjän.
* Käyttäjä voi kirjautua sisään sovellukseen.
* Käyttäjä voi selata kursseja aihepiirien mukaan, sekä nähdä tietoja näistä hakujen yhteydessä.
* Käyttäjä ja kuka tahansa muukin voi katsoa kurssin tietoja.
* Käyttäjä voi liittyä kursseille ja katsoa kaikki kurssit joille hän on liittynyt.
* Ei voi olla käy useampaa käyttäjää samalla sähköpostilla.
* Käyttäjä voi varata paikan kursseille.
* Käyttäjä voi poistaa varauksensa kurssille.
* Järjestelmänvalvoja voi poistaa varauksen käyttäjältä.
* Järjestelmänvalvoja voi selata kursseille osallistuneita käyttäjiä.
* Kurssia ei voi poistaa, jos siinä on varauksia tai osallistujia.
* Aihetta ei voi poistaa, jos siihen liittyy kursseja.

### Toteuttamatta jääneet toiminnallisuudeet(sulkeissa vastaavuus jos on)

* Varauksen yhteydessä käyttäjälle ilmoitetaan tilinumero maksulle, kyseisen laskun viitenumero ja maksun määrä(Tällä hetkellä nämä syötetään itse).
* Käyttäjä voi halutessaan tallentaa laskunsa(Tallentuu sovelluksessa itsekseen).
* Virheviestien näyttäminen esim. tapauksissa joissa käyttäjä yrittää poistaa aiheen johon liittyy kursseja.
* Varmistus siitä, ettei kurssia luodessa ole alkupäivämäärä, loppupäivämäärää myöhemmin.
* Kurssien ja käyttäjien tietojen muokkaus.


### Tietorakenne

Sovellus luo ensin taulun Topic:

CREATE TABLE Topic (
    id int,
    name varchar(144),
    PRIMARY KEY(id)
);
 

Jonka jälkeen se luo käyttäjät:

CREATE TABLE Account (
    id int,
    name varchar(144),
    email varchar(144),
    phonenumber varchar(144),
    password varchar(144),
    urole varchar(144),
    PRIMARY KEY(id)
 );
 
 
 Kurssit:
 
 CREATE TABLE Course (
    id int,
    topic_id int,
    name varchar(144),
    date_start date,
    date_end date,
    place varchar(144),
    teachers varchar(144),
    desc varchar(144),
    FOREIGN KEY(topic_id) REFERENCES Topic(id),
    PRIMARY KEY(id)
  );
  
  
  Liitostaulu CourseStudent:
  
  CREATE TABLE CourseStudent (
      course_id int,
      account_id int,
      FOREIGN KEY(course_id) REFERENCES Course(id),
      FOREIGN KEY(account_id) REFERENCES Account(id)
  );
  
  
  Varaukset:
  
  CREATE TABLE Reservation (
      id int,
      accountnumber varchar(144),
      indexnumber int,
      amount int,
      haspaid boolean,
      PRIMARY KEY(id)
  );
  
  
  ### Sovelluksessa toimivia sql-kyselyitä
  
  Muutamia esimerkkejä sql-kyselyistä, joita sovellus tekee.
  
  #### Kurssien haku aiheiden mukaan:
  
    SELECT * FROM Course
    JOIN Topic ON Topic.id = Course.topic_id
    WHERE Topic.id = "annettu parametri";
   
   
  #### Oppilaiden haku kursseista:
   
    SELECT * FROM Course
    JOIN CourseStudent ON CourseStudent.course_id = Course.id"
    JOIN Account ON Account.id = CourseStudent.account_id"
    WHERE Course.id = "annettu parametri";
   
   
  #### Käyttäjällä jolla on varauksia kursseihin, joita hän ei vielä ole maksanut:
   
     SELECT Count(Reservation.id) FROM Course
     LEFT JOIN CourseStudent ON CourseStudent.course_id = Course.id
     LEFT JOIN Account ON Account.id = CourseStudent.account_id
     LEFT JOIN Reservation ON Account.id = Reservation.account_id
     WHERE Account.id = "nykyisen käyttäjän id" AND Reservation.haspaid = false
     GROUP BY CourseStudent.course_id;
    
    
  #### Uuden käyttäjän luonti(oletuksena, ettei annettu sähköposti ole jo tietokannassa):
    
    INSERT INTO Account (name, email, phonenumber, password, urole)
    VALUES ("- nimi", "- sähköposti", "- puhelinnumero", "- salasana", "lomakkeesta saatu rooli");
     
  Pääavaimen lisäys tapahtuu automaattisesti.
