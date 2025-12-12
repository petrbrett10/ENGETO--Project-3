"""
main.py: Třetí projekt do Engeto Online Python Akademie
author: Petr Brettschneider
email: petrbrettschneider@gmail.com
description: Elections Scraper
"""

import requests
from bs4 import BeautifulSoup as bs
import csv
import argparse

def bs_get(url):
    """Načte HTML obsah a vrátí objekt BeautifulSoup."""
    print(f"Stahuji data z vybraného URL:", url)
    return bs(requests.get(url).text, features="html.parser")

def get_muni_links(base_url):
    """Načte kódy obcí a odkazy na detailní výsledky."""
    soup = bs_get(base_url)
    links = {
        td.a.text: f"https://www.volby.cz/pls/ps2017nss/{td.a['href']}"
        for td in soup.find_all("td", class_="cislo") if td.a
    }
    return links

def parse_muni_results(url):
    def parse_muni_results(url):
        """Načte výsledky voleb pro každou obec."""
    soup = bs_get(url)
    header_txt = soup.select_one("h3:nth-child(4)").get_text(strip=True).replace("Obec: ", "")
    muni_code = url.split("xobec=")[1].split("&")[0]
    
    data = {
        "kód obce": muni_code,
        "název obce": header_txt,
        "voliči v seznamu": int((soup.find("td", headers="sa2").get_text(strip=True)).replace("\xa0", "").replace(" ", "")),
        "vydané obálky": int((soup.find("td", headers="sa3").get_text(strip=True)).replace("\xa0", "").replace(" ", "")),
        "platné hlasy": int((soup.find("td", headers="sa6").get_text(strip=True)).replace("\xa0", "").replace(" ", "")),
    }

    for i in range(1, 3):
        for row in soup.find_all("table")[i].find_all("tr")[2:]:
            cols = row.find_all("td")
            if len(cols) >= 2:
                data[cols[1].text.strip()] = (cols[2].text.strip()).replace("\xa0", "").replace(" ", "")
    
    return data

def save_to_csv(data, filename):
    """Uloží výsledky do CSV souboru oddělené čárkou."""
    if data:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

def main():
    """Hlavní funkce pro získání vstupu od uživatele a uložení výsledků voleb do CSV souboru."""
    parser = argparse.ArgumentParser(description="Scraper volebních výsledků pro daný územní celek.")
    parser.add_argument("url", help="URL stránky s výpisem obcí")
    parser.add_argument("output", help="Název výstupního CSV souboru")
    args = parser.parse_args()

    if not args.url.startswith("https://www.volby.cz/pls/ps2017nss/"):
        parser.error("Špatně zadaná URL. URL musí začínat 'https://www.volby.cz/pls/ps2017nss/'.")
    if not args.output.lower().endswith(".csv"):
        parser.error("Výstupní soubor musí mít příponu .csv.")

    try:
        municip_link = get_muni_links(args.url)
        if not municip_link:
            parser.error("Nebyla nalezena žádná obec na zadané URL.")

        results = [parse_muni_results(url) for url in municip_link.values()]
        save_to_csv(results, args.output)
        print(f"Hotovo! Výsledky jsou zapsány do souboru {args.output}")
    except Exception as e:
        parser.error(f"Nalezena chyba: {e}")

if __name__ == "__main__":
    main()