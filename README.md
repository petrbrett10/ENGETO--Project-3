Projekt: Elections Scraper
Třetí projekt na kurzu od Engeto - Datový analytik s Pythonem.
Popis projektu
Tento projekt slouží k extrahování výsledků parlamentních voleb v roce 2017. Odkaz k prohlédnutí naleznete zde.
Instalace knihoven
Knihovny, které jsou použity v kódu, jsou uložené v souboru requirements.txt. Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:

pip --version              # overim verzi manazeru
pip install -r requirements.txt      # nainstaluji knihovnu
Spuštění projektu
Spuštění souboru main.py v rámci příkazového řádku vyžaduje dva povinné argumenty.
Prvním je url adresa s daty pro extrakci, druhým je název výstupního souboru.
python main.py <odkaz-uzemniho-celku> <vysledny-soubor>

Argumenty uveďte do uvozovek a oddělte mezerou.

Následně se stáhnou výsledky jako soubor s příponou .csv.
Ukázka projektu
Výsledky hlasování pro okres Nymburk:
1.	argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2108
2.	argument: vysledky_nymburk.csv
Spuštění programu:
Python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2108" "vysledky_nymburk.csv"

Průběh stahování (při správném chodu skriptu):
Stahuji data z vybraného URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2108
Stahuji data z vybraného URL: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=537021&xvyber=2108
Stahuji data z vybraného URL: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=537039&xvyber=2108
Stahuji data z vybraného URL: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=537047&xvyber=2108
…
Stahuji data z vybraného URL: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=534862&xvyber=2108
Stahuji data z vybraného URL: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=503410&xvyber=2108
Hotovo! Výsledky jsou zapsány do souboru vysledky_nymburk.csv 

Ukázka formátu výstupu v CSV souboru:
kód obce,název obce,voliči v seznamu,vydané obálky,platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Unie H.A.V.E.L.,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
537021,Běrunice,690,382,382,27,3,0,40,1,28,30,7,4,7,0,0,25,0,6,8,136,1,0,14,0,1,0,1,42,1
537039,Bobnice,666,389,387,37,0,0,33,0,42,31,5,2,3,0,0,27,0,0,23,124,0,1,7,0,0,1,1,50,0
537047,Bříství,268,193,190,26,1,0,18,0,13,12,2,2,1,0,0,16,1,0,3,66,0,0,4,0,3,0,0,22,0
...
…
…

<img width="454" height="710" alt="image" src="https://github.com/user-attachments/assets/00c4eddc-da6d-4608-aec7-5ec25aaa753e" />
