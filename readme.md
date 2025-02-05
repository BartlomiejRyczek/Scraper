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



# 📌 Automatyczny Web Scraper Ofert Pracy IT

## 📌 Opis projektu
Ten projekt zawiera **automatyczny scraper** do pobierania ofert pracy IT z dwóch popularnych portali:
- **Pracuj.pl**
- **JustJoin.it**

Dane są przetwarzane, filtrowane i zapisywane do plików CSV, aby umożliwić późniejszą analizę.

---

## 🚀 Funkcje projektu
✅ **Obsługa dynamicznych stron** - Selenium w tle przewija stronę, aby pobrać wszystkie dostępne oferty. 
✅ **Automatyczne pobieranie ofert pracy** - skrypty mogą automatycznie uruchamiać się przy każdym starcie komputera, gdy plik BAT zostanie umieszczony w folderze autostartu.
✅ **Zapis do CSV** - pobrane dane są przechowywane w pliku `job_offerts.csv` oraz `job_offerts_just_join.csv`.   
✅ **Unikanie duplikatów** - w notebooku eliminuje się duplikaty oraz scala dane
✅ **Zapis do CSV** - ujednolicone dane są przechowywane w pliku `oferty_pracy_bez_duplikatow.csv`.  
✅ **Obsługa wynagrodzeń i technologii** - ekstrakcja technologii i widełek płacowych.  
✅ **Analiza danych** - statystyki, wykresy i analiza trendów.


---

## 🛠 Wymagania
🔹 **Python 3.x**  
🔹 **Selenium**  
🔹 **BeautifulSoup**  
🔹 **Pandas**  
🔹 **Matplotlib** 

Aby zainstalować wymagane biblioteki, uruchom:
```bash
pip install -r requirements.txt
```

---

## ⚙ Instalacja i uruchomienie
### **1️⃣ Uruchamianie ręczne skryptów**
Uruchom scraper dla Pracuj.pl:
```bash
python scraper_pracuj_pl.py
```
Uruchom scraper dla JustJoin.it:
```bash
python scraper_just_join.py
```

### **3️⃣ Automatyczne uruchamianie przy starcie systemu**
Uruchom plik `runScrapers.bat`, który automatycznie uruchomi oba skrypty (pamiętaj o zmienieniu ścieżki, by była poprawna)
Polecam dodać również ten plik do autostarty systemu, w celu automatycznego scrapowania danych przy kazdym starcie komputera. 

---

## 📊 Analiza danych
Dane są analizowane w pliku **analizaDanych.ipynb**, gdzie można:
- 🏆 **Zbadać średnie wynagrodzenie w różnych technologiach**
- 📈 **Wykonać analizę trendów ilości ofert w czasie**
- 📊 **Zwizualizować rozkład wynagrodzeń**
- 🔎 **Sprawdzić, które technologie są najczęściej wymagane**

---

## 🚀 Potencjalne ulepszenia projektu
🔹 **Użycie bazy danych (SQLite/PostgreSQL) zamiast CSV**  
🔹 **Lepsza obsługa błędów i logowanie (`logging`)**  
🔹 **Scrapowanie asynchroniczne dla lepszej wydajności (`Asyncio`, `Scrapy`)**  
🔹 **Dodanie analizy lokalizacji ofert i generowanie mapy (Folium)**  
🔹 **Wizualizacja trendów w czasie (np. popularność języków programowania)**  
🔹 **Integracja z AI (np. analiza treści ofert przez GPT)**


# ⚠️ Uwagi
* W skryptach używany jest mechanizm porównywania rekordów, by unikać duplikatów – sprawdza klucze unikalności (Tytuł, Firma, Link).
* W plikach CSV przechowywane są m.in. tytuł oferty, firma, data, wynagrodzenie, technologie oraz link.
* Plik convert_to_tidy_data.py nie jest potrzebny do prawidłowego działania programu (Jest w trakcie rozwoju)