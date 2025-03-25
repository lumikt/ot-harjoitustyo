# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on tarkoitettu opiskelun tehostamiseen. Sovellus kokoaa yhteen paikkaan kurssimuistiinpanot .md tiedostoina, joita voi halutessaan selata kursseittain tai aihepiireittäin. Lisäksi, sovellukseen voi koota käsitepankin joka automaattisesti lisää linkit muistiinpanoihin käsitteiden selityksiin. Lisäksi sovelluksen on määrä toimia kertausapurina joka tarjoaa kysmyspatterin käsitteistä opiskelijalle.



## Käyttöliittymäluonnos
![UI hahmotelma](kuvat/ot%20harjoitustyo%20ui%20draft.png)
Sovelluksen päänäkymässä käyttäjä voi lukea tekemänsä muistiinpanot ja luoda uusia muistiinpanoja. Käsitepankkinäkymässä käyttäjä voi selata käsitteitä kursseittain tai aiheittain. Tietovisassa käyttäjä valitsee aihepiirin tai kurssin jonka käsitteistä muodostuu tietovista.
## Perusversion toiminnallisuudet

Perusversiossa käyttäjä kykenee lisäämään muistiinpanoja sekä käsitteitä käsitepankkiin. Sovellus lisää automaattisesti käsitteisiin linkit opiskelija kirjoittamissa muistiinpanoissa. Sovellus tukee oppimista tarjoamalla tietovisoja pankkiin lisätyistä käsitteistä.

### Muistiinpanot
* Sovelluksessa on mahdollista jakaa muistiinpanot kursseittain ja aihepiireittäin itse määritetyllä logiikalla (tagaamalle muistiinpanot)
* Muistiinpanoja voi asetella tärkeysjärjestykseen omatoimisesti ja niitä voi järjestää ajan, nimen tai teeman mukaan
* Käyttäjä voi suodattaa muistiinpanoja kursseittain tai aihepiireittäin

### Käsitepankki
* Käyttäjä voi lisätä käsitteitä käsitepankkiin suoraan pankin käyttöliittymän kautta
* Käyttäjä voi lisätä käsitteen suoraan kirjoittamastaan tekstistä
* Käsitteet lisätään automaattisesti käyttäjän muistiinpanoihin sanahaulla kun muistiinpano luodaan ensimmäisen kerran.
* Käyttäjä voi manuaalisesti lisätä käsitelinkin tai poistaa sen muistiinpanoistaan
* Käyttäjä voi myöhemmin suorittaa automaattisen haun lisätäkseen käsite-linkkejä vanhoihin muistiinpanoihin
* Käyttäjä voi tarkastella käsitteitä erikseen muistiinpanoista
* Käyttäjä voi järjestää tai suodattaa käsitteitä kursseittain tai aihepiireittäin

### Kertaus
* Käyttäjä voi kerratta käsitteitä tietovisan avulla jossa käyttäjää vastaa ensin vapaamuotoisesti ja sen jälkeen saa oikean vastauksen



## Jatkokehitysideoita
* Käyttäjä voi kerratta käsitteitä tietovisan avulla jossa käyttäjä yhdistää käsitteen oikeaan selitykseen
* Käyttäjä voi itse luoda muistipelin käsitteistä
* Käyttäjä voi suunnitella opintojaan ja kertaamistaan sovelluksen kautta (to do / aikataulutus / aikaseuranta)
* Käyttäjä voi tarkastella onnistumisprosenttiaan käsitetietovisoissa ajan myötä
