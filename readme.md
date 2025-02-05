# 📌 Automatyczny Web Scraper Ofert Pracy IT

## 📌 Opis projektu
Ten projekt zawiera **automatyczny scraper** do pobierania ofert pracy IT z dwóch popularnych portali:
- **Pracuj.pl**
- **JustJoin.it**

Dane są przetwarzane, filtrowane i zapisywane do plików CSV, aby umożliwić późniejszą analizę.

---

## 🚀 Funkcje projektu
- ✅ **Obsługa dynamicznych stron** - Selenium w tle przewija stronę, aby pobrać wszystkie dostępne oferty. 
- ✅ **Automatyczne pobieranie ofert pracy** - skrypty mogą automatycznie uruchamiać się przy każdym starcie komputera, gdy plik BAT zostanie umieszczony w folderze autostartu.
- ✅ **Zapis do CSV** - pobrane dane są przechowywane w pliku `job_offerts.csv` oraz `job_offerts_just_join.csv`.   
- ✅ **Unikanie duplikatów** - w notebooku eliminuje się duplikaty oraz scala dane
- ✅ **Zapis do CSV** - ujednolicone dane są przechowywane w pliku `oferty_pracy_bez_duplikatow.csv`.  
- ✅ **Obsługa wynagrodzeń i technologii** - ekstrakcja technologii i widełek płacowych.  
- ✅ **Analiza danych** - statystyki, wykresy i analiza trendów.


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