from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime
import requests

url = "https://justjoin.it/job-offers/all-locations/python?with-salary=yes&orderBy=DESC&sortBy=newest"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
response = requests.get(url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.content, 'html.parser')

with open('parsed_page_just_join.html', 'w', encoding='utf-8') as file:
            file.write(soup.prettify())