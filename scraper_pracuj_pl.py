from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://it.pracuj.pl/praca?et=1%2C3%2C17"
driver = webdriver.Chrome()
driver.get(url)
body = driver.find_element(By.TAG_NAME, "body")
for _ in range(1):  # Przewiń stronę kilka razy
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)  # Czekaj chwilę na załadowanie nowych danych
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.quit()

# Funkcja do konwersji daty na format ISO 8601
def convert_to_iso(date_str):
    polish_months = {
        "stycznia": "01", "lutego": "02", "marca": "03", "kwietnia": "04",
        "maja": "05", "czerwca": "06", "lipca": "07", "sierpnia": "08",
        "września": "09", "października": "10", "listopada": "11", "grudnia": "12"
    }
    try:
        day, month_polish, year = date_str.split()
        month = polish_months[month_polish]
        return f"{year}-{month}-{day.zfill(2)}"
    except Exception:
        return "Brak daty"

# Ścieżka do pliku CSV
csv_file_path = 'job_offers.csv'

# Wczytanie istniejących danych, jeśli plik już istnieje
existing_records = set()
if os.path.exists(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Pominięcie nagłówka
        for row in reader:
            if len(row) >= 5:  # Sprawdzamy kompletność wierszy
                existing_records.add((row[0], row[1]))  # Tytuł, Firma

# Przygotowanie listy na nowe dane
new_data = []

# Wyszukiwanie ofert pracy
offers = soup.find_all('div', class_='gp-pp-reset tiles_b18pwp01 core_po9665q')  # Klasa grupująca każdą ofertę pracy

for offer in offers:
    # Pobranie tytułu oferty
    title_tag = offer.find('a', class_='tiles_o1859gd9 core_n194fgoq')
    title = title_tag.get_text(strip=True) if title_tag else 'Brak tytułu'

    # Pobranie nazwy firmy
    company_tag = offer.find('h3', class_='tiles_chl8gsf size-caption core_t1rst47b')
    company = company_tag.get_text(strip=True) if company_tag else 'Brak nazwy firmy'

    # Pobranie daty opublikowania i konwersja na format ISO 8601
    date_tag = offer.find('p', class_='tiles_a1nm2ekh tiles_s1pgzmte tiles_bg8mbli core_pk4iags size-caption core_t1rst47b')
    date = convert_to_iso(date_tag.get_text(strip=True).replace('Opublikowana:', '').strip()) if date_tag else 'Brak daty'

    # Pobranie wynagrodzenia
    salary_tag = offer.find('span', class_='tiles_s1x1fda3')
    salary = salary_tag.get_text(strip=True).replace(' zł / mies. (zal. od umowy)', '') if salary_tag else 'Brak wynagrodzenia'

    # Pobieranie wymaganej znajomosci technologii
    tech_tag = offer.find_all('span', class_='_chip_hmm6b_1 _chip--highlight_hmm6b_1 _chip--small_hmm6b_1 _chip--full-corner_hmm6b_1 tiles_c276mrm')
    technologies = [tag.get_text(strip=True) for tag in tech_tag] if tech_tag else 'Brak technologii'
    # Pobranie linku do oferty
    link_tag = offer.find('a', class_='tiles_cnb3rfy core_n194fgoq')
    link = link_tag['href'] if link_tag else 'Brak linku'
    
    
    record = (title, company)  # Uwzględniamy link jako unikalny identyfikator
    if record not in existing_records:
        new_data.append([title, company, date, salary, technologies, link])
        existing_records.add(record)  # Dodajemy pełny klucz do zbioru
        
        
# Zapisanie nowych danych do pliku CSV (dodawanie do istniejących)
print(f"Ścieżka do pliku CSV: {csv_file_path}")
#print(f"Nowe dane do zapisania: {new_data}")

with open(csv_file_path, 'a', encoding='utf-8', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Dodanie nagłówka tylko w przypadku tworzenia nowego pliku
    if os.stat(csv_file_path).st_size == 0:
        csvwriter.writerow(['Tytuł', 'Firma', 'Data opublikowania', 'Wynagrodzenie', 'Technologie', 'Link'])
    csvwriter.writerows(new_data)

print(f"Dodano {len(new_data)} nowych rekordów do pliku job_offers.csv.")