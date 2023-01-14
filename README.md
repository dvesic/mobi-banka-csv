# Mobi banka - pregled potrošnje po kategorijama na osnovu CSV eksporta

Jedan od mojih zadataka (u porodici) je da pratim potrošnju i u skladu sa tim [planiram budžet](https://www.vesic.org/blog/kucni-budzet-ili-plan-potrosnje-upravljanje-novcem/).

Sa druge strane, moja glavna banka je [Mobi banka](https://online.mobibanka.rs), koja na žalost nema podršku za
kategorizaciju potrošnje.

Šta će programer uraditi? :-) Pa naravno, napraviti program :-)

Ideja je jednostavna:

1. Uraditi eksport podataka u zadatom periodu u CSV formatu
2. Provući CSV eksport kroz python skript
3. On će izgenerisati inicijalnu listu prodavaca sa jednom kategorijom
4. Modifikovati listu (dodajući kategorije, grupišući prodavce i eventualno isključujući neke) i ići ponovo na (2.)
5. Kada smo zadovoljni, sačuvati listu prodavaca za sledeće eksporte

Gornji postupak je zahtevan samo prvi put; između dva eksporta, obično je jako mali broj novih prodavaca.

## Instalacija

Potrebno je imati instaliran python 3.6 ili noviji; predlažem najnoviju verziju sa [python.org](https://www.python.org/).

Napravite folder, i raspakujte release u njega. Otvorite CMD u tom folderu i pokrenite (jednom):

```python
pip install -r requirements.txt
```

To bi bilo to što se tiče instalacije :-) (mada, i bez ovog koraka će raditi - program isključivo koristi samo 
standardne biblioteke koje dolaze uz python

## Eksport podataka

Savetujem da prilikom eksporta podataka izaberete samo RSD i samo izlaze (isplate):

![Mobi-Banka-filtriranje-transakcija](https://user-images.githubusercontent.com/17367063/212486892-31ee4d5d-b83c-4819-a5dd-c88d741bf248.jpg)

Tako će cifre biti tačne - trenutno program ne procesira tip valute (mada, ako bude zahteva, zašto da ne :-) )

Kada se završi generisanje transakcija (da, da, Mobi banka nije šampion brzine), izaberite CSV tip eksporta:

![Mobi-Banka-eksport-u-CSV](https://user-images.githubusercontent.com/17367063/212487052-8685040a-05d2-4e23-87bc-7448f36b111d.jpg)

Time je ulazni podatak (obično imena *PrintList.csv*) spreman - ili zapamtite stazu do njega, ili ga prebacite u folder aplikacije.

## Izvršavanje programa

Ovo je jednostavno; pozicionirate se u folder, i:
```python
python main.py
```
### Opcije programa

Standardne opcije se nalaze u *config.ini* datoteci; ako tu sve podesite, parametri na ulaznoj liniji vam neće ni biti potrebni.

U protivnom:

```
usage: main.py [-h] [-i INPUT_FILE] [-o OUT_FILE] [-c DEFAULT_CAT]

Obrada transakcija u CSV formatu od Mobi banke, za bolje praćenje troškova

options:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input_file INPUT_FILE
                        Ime ulaznog CSV fajla (eksport sa banke), default je "PrintList.csv"
  -o OUT_FILE, --out_file OUT_FILE
                        Ime rezultujućeg CSV fajla, default je "Troskovi.csv"
  -c DEFAULT_CAT, --default_cat DEFAULT_CAT
                        Naziv podrazumevane kategorije, ako se ne nađe; default je "RAZNO"
 ```
 ## Rezultat rada
 
 Program će generisati tri datoteke, *Merchants.csv*, *Troskovi.csv* i *SUM_Troskovi.csv*. 
 
 U prvom prolazu će svi prodavci imati podrazumevanu kategoriju (*RAZNO*) - editujte fajl *Merchants.csv* i 
 prilagodite kategorije. Za prodavce koji počinju na isti string možete napraviti jedan slog i to će pokriti te 
 prodavce (radi se poređenje tipa *ako string počinje sa ...*).

 (u samoj arhivi je već primer datoteke *Merchants.csv* iz mog eksporta; možete je promeniti ili skroz obrisati, 
 svakako ne smeta)
 
### Struktura *Merchants.csv* fajla

| StartsWith | TranslateTo  | Category | Remove |
|---|--------------|----------|--------|
| BENU PHARMACIES | BENU Apoteka | APOTEKA | FALSE  |

* StartsWith - string koji se traži u nazivu prodavca, na početku naziva
* TranslateTo - string u koji će se zameniti naziv prodavca; generička imena su ponekad ružna
* Category - kategorija koja će se dodati u rezultujući fajl za sve prodavce koji počinju sa *StartsWith*
* Remove - ako je TRUE, prodavac će biti uklonjen iz rezultujućeg fajla

### *SUM_Troskovi.csv*

Naravno, možete uvući *Troskovi.csv* u Excel i da recimo pivot tabelom uradite analizu. Ali, ako želite da
dobijete samo sumu za svaku kategoriju, možete koristiti *SUM_Troskovi.csv* - tu su apsolutne sume i procenti
za svaku kategoriju, sortirane opadajuće po sumi.
