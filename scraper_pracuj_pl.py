from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime
import requests

url = "https://it.pracuj.pl/praca?et=1%2C3%2C17&itth=37"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
response = requests.get(url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.content, 'html.parser')

with open('parsed_page.html', 'w', encoding='utf-8') as file:
            file.write(soup.prettify())

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
                existing_records.add((row[0], row[1], row[4]))  # Tytuł, Firma, Link

# Wczytanie pliku HTML
with open('parsed_page.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Przygotowanie listy na nowe dane
new_data = []

# Wyszukiwanie ofert pracy
offers = soup.find_all('div', class_='tiles_cobg3mp')  # Klasa grupująca każdą ofertę pracy

for offer in offers:
    # Pobranie tytułu oferty
    title_tag = offer.find('h2', class_='tiles_h1p4o5k6')
    title = title_tag.get_text(strip=True) if title_tag else 'Brak tytułu'

    # Pobranie nazwy firmy
    company_tag = offer.find('h3', class_='tiles_chl8gsf')
    company = company_tag.get_text(strip=True) if company_tag else 'Brak nazwy firmy'

    # Pobranie daty opublikowania i konwersja na format ISO 8601
    date_tag = offer.find('p', class_='tiles_arxx4s5')
    date = convert_to_iso(date_tag.get_text(strip=True).replace('Opublikowana:', '').strip()) if date_tag else 'Brak daty'

    # Pobranie wynagrodzenia
    salary_tag = offer.find('span', class_='tiles_s1x1fda3')
    salary = salary_tag.get_text(strip=True).replace(' zł / mies. (zal. od umowy)', '') if salary_tag else 'Brak wynagrodzenia'

    # Pobranie linku do oferty
    link_tag = offer.find('a', class_='tiles_o1859gd9')
    link = link_tag['href'] if link_tag else 'Brak linku'

    # Sprawdzenie, czy oferta już istnieje w pliku
    record = (title, company, link)
    if record not in existing_records:
        new_data.append([title, company, date, salary, link])
        existing_records.add(record)  # Dodaj do zbioru, aby uniknąć duplikatów

# Zapisanie nowych danych do pliku CSV (dodawanie do istniejących)
with open(csv_file_path, 'a', encoding='utf-8', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Dodanie nagłówka tylko w przypadku tworzenia nowego pliku
    if os.stat(csv_file_path).st_size == 0:
        csvwriter.writerow(['Tytuł', 'Firma', 'Data opublikowania', 'Wynagrodzenie', 'Link'])
    csvwriter.writerows(new_data)

print("Dane zostały zapisane do pliku job_offers.csv.")