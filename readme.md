# Opis
Projekt służy do pobierania ogłoszeń o pracę z portali Just Join IT oraz Pracuj.pl, zapisywania ich do plików CSV, a następnie przetwarzania (m.in. czyszczenie danych, analiza statystyczna) w języku Python.

# Struktura
* scraper_just_join.py – Skrypt Selenium + BeautifulSoup do pobierania i zapisu ofert z justjoin.it
* scraper_pracuj_pl.py – Skrypt Selenium + BeautifulSoup do pobierania i zapisu ofert z it.pracuj.pl
* analizaDanych.ipynb – Notebook z przykładami obróbki, wizualizacji i analizy danych (np. korelacje, statystyki opisowe)


# Kroki działania

1. Uruchom skrypty scraperów (scraper_just_join.py oraz scraper_pracuj_pl.py) – dane trafią do plików CSV (np. job_offers_just_join.csv, job_offers.csv).
2. Otwórz plik analizaDanych.ipynb w środowisku Jupyter/VS Code, by przeprowadzić dalszą analizę (np. wykresy, korelacje, testy).


# Wymagania
Python 3
Biblioteki: requests, BeautifulSoup, pandas, NumPy, Selenium, Matplotlib, re (oraz inne użyte w notebooku)
Zainstalowany web driver do Selenium (np. ChromeDriver)

# Uruchamianie 
1. Zainstaluj wymagane pakiety: 
``` bash
pip install -r requirements.txt
```

2. Upewnij się, że masz zainstalowany i skonfigurowany ChromeDriver.
3. Uruchom terminal i wykonaj:

``` bash
python scraper_just_join.py
python scraper_pracuj_pl.py
```

4. Zaimportuj lub otwórz plik analizaDanych.ipynb w swoimi ulubionym edytorze (np. VS Code) i uruchom kolejne komórki.

# Uwagi
* W skryptach używany jest mechanizm porównywania rekordów, by unikać duplikatów – sprawdzaj klucze unikalności (np. (Tytuł, Firma, Link)).
* W plikach CSV przechowywane są m.in. tytuł oferty, firma, data, wynagrodzenie, technologie oraz link.
* Plik convert_to_tidy_data.py nie jest potrzebny do prawidłowego działania programu (Jest w trakcie rozwoju)


