from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  
options.add_argument("--disable-gpu")  
options.add_argument("--window-size=1920,1080")  

driver = webdriver.Chrome(options=options)
driver.get('https://justjoin.it/job-offers/all-locations?with-salary=yes&orderBy=DESC&sortBy=newest')
body = driver.find_element(By.TAG_NAME, "body")
for _ in range(15):  # Przewiń stronę kilka razy
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.4)  # Czekaj chwilę na załadowanie nowych danych
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.quit()

base_dir = "C:\\Users\\brycz\\Downloads\\webScraper"
csv_file_path = os.path.join(base_dir, 'job_offers_just_join.csv')
existing_records = set()

# Sprawdzenie, czy plik CSV istnieje i wczytanie istniejących rekordów
if os.path.exists(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Pominięcie nagłówka
        for row in reader:
            if len(row) >= 5:  # Sprawdzamy kompletność wierszy
                existing_records.add((row[0], row[1], row[5]))  # Tytuł, Firma, Link

# Wyszukiwanie ofert pracy
offers = soup.find_all('div', class_='MuiBox-root css-ai36e1') 

# Debugowanie liczby znalezionych ofert
print(f"Liczba znalezionych ofert: {len(offers)}")

new_data = []

for offer in offers:
    # Pobranie tytułu oferty
    title_tag = offer.find('h3', class_='css-1gehlh0')
    title = title_tag.get_text(strip=True) if title_tag else 'Brak tytułu'

    # Pobranie nazwy firmy
    company_tag = offer.find('div', class_='MuiBox-root css-1kb0cuq')
    if company_tag:
        span = company_tag.find('span')
        company_name = span.get_text(strip=True)
    else:
        company_name = "Brak nazwy firmy"

    # Pobranie daty opublikowania
    date_tag = offer.find('div', class_='MuiBox-root css-jikuwi')
    if date_tag:
        date_text = date_tag.get_text(strip=True)
        if "New" in date_text:
            date = datetime.now().strftime('%Y-%m-%d')
        else:
            date = date_text
            if "d ago" in date:
                days_ago = int(date.replace("d ago", "").strip())
                result_date = datetime.today() - timedelta(days=days_ago)
                date = result_date.strftime('%Y-%m-%d')
    else:
        date = 'Brak daty'

    # Pobranie wynagrodzenia
    salary_tag = offer.find('div', class_='MuiBox-root css-18ypp16')
    if salary_tag:
        salary_spans = salary_tag.find_all('span')
        
        if len(salary_spans) >= 3:  # Upewniamy się, że lista ma przynajmniej 3 elementy
            salary_min = salary_spans[0].get_text(strip=True)
            salary_max = salary_spans[1].get_text(strip=True)
            currency = salary_spans[2].get_text(strip=True)
            salary = f"{salary_min} - {salary_max} {currency}"
        elif len(salary_spans) == 2:  # Jeśli są tylko dwa elementy, prawdopodobnie brakuje waluty
            salary_min = salary_spans[0].get_text(strip=True)
            salary_max = salary_spans[1].get_text(strip=True)
            salary = f"{salary_min} {salary_max}"
        elif len(salary_spans) == 1:  # Jeśli jest tylko jedno pole, to podajemy tylko minimalne wynagrodzenie
            salary = salary_spans[0].get_text(strip=True)
        else:
            salary = 'Brak wynagrodzenia'
    else:
        salary = 'Brak wynagrodzenia'
        
    # technologie wymagane przez pracodawcę
    tags_1 = offer.find_all('div', class_='MuiBox-root css-jikuwi')
    technologies = [element.get_text(strip=True) for element in tags_1]
    technologies = technologies[1:]

    # Pobranie linku do oferty
    link_tag = offer.find('a', target='_parent')
    link = 'https://justjoin.it' + link_tag['href'] if link_tag else 'Brak linku'

    # Dodanie danych do new_data
    record = (title, company_name, link)
    if record not in existing_records:
        new_data.append([title, company_name, date, salary, technologies, link])
        existing_records.add(record)
    else:
        print(f"Rekord już istnieje: {record}")

print(f"Ścieżka do pliku CSV: {csv_file_path}")
print(f"Nowe dane do zapisania: {new_data}")

with open(csv_file_path, 'a', encoding='utf-8', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Dodanie nagłówka tylko w przypadku tworzenia nowego pliku
    if os.stat(csv_file_path).st_size == 0:
        csvwriter.writerow(['Tytuł', 'Firma', 'Data opublikowania', 'Wynagrodzenie', 'Technologie', 'Link'])
    csvwriter.writerows(new_data)

print(f"Dodano {len(new_data)} nowych rekordów do pliku job_offers_just_join.csv.")