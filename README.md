# mobi-banka-csv
Processing CSV export from https://online.mobibanka.rs to get better overview of spending

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
 
 Program će generisati dve datoteke, *Merchants.csv* i *Troskovi.csv*. 
 
 U prvom prolazu će svi prodavci imati podrazumevanu kategoriju (*RAZNO*) - editujte fajl *Merchants.csv* i prilagodite kategorije. Za prodavce koji počinju na isti string (tipa ) možete napraviti jedan slog i to će pokriti te prodavce (radi se poređenje tipa *ako string počinje sa ...*).
 
 (u samoj arhivi je već primer dattoteke *Merchants.csv* iz mog eksporta; možete je promeniti ili skroz obrisati, svakako ne smeta)

