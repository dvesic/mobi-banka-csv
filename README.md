# mobi-banka-csv
Processing CSV export from https://online.mobibanka.rs to get better overview of spending

## Eksport podataka

Savetujem da prilikom eksporta podataka izaberete samo RSD i samo izlaze (isplate):

![Mobi-Banka-filtriranje-transakcija](https://user-images.githubusercontent.com/17367063/212486892-31ee4d5d-b83c-4819-a5dd-c88d741bf248.jpg)

Tako će cifre biti tačne - trenutno program ne procesira tip valute (mada, ako bude zahteva, zašto da ne :-) )

Kada se završi generisanje transakcija (da, da, Mobi banka nije šampion brzine), izaberite CSV tip eksporta:

![Mobi-Banka-eksport-u-CSV](https://user-images.githubusercontent.com/17367063/212487052-8685040a-05d2-4e23-87bc-7448f36b111d.jpg)

Time je ulazni podatak (obično imena *PrintList.csv*) spreman - ili zapamtite stazu do njega, ili ga prebacite u folder aplikacije.

