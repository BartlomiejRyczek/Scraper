import csv
import json
# Ścieżki do plików
input_csv_path = 'job_offers_just_join.csv'
output_csv_path = 'job_offers_just_join_tidy.csv'

def convert_to_tidy(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Pobranie nagłówka i dodanie nowych kolumn dla tidy data
        header = next(reader)
        tidy_header = header[:3] + ['salary_type', 'salary', 'currency'] + header[4:]
        writer.writerow(tidy_header)

        for row in reader:
            salary = row[3]
            currency = row[4]

            # Usuwanie wszelkich spacji, niełamliwych spacji, i jednostek waluty przed konwersją na int
            salary = salary.replace(' ', '').replace('\xa0', '').replace('zł', '').replace('pln', '').strip()

            if '–' in salary:  # Format "5 500–15 000"
                min_salary, max_salary = salary.split('–')
                min_salary = int(min_salary.strip())
                max_salary = int(max_salary.strip())
                
                # Dodanie wiersza dla min
                writer.writerow(row[:3] + ['min', min_salary, currency] + row[5:])
                # Dodanie wiersza dla max
                writer.writerow(row[:3] + ['max', max_salary, currency] + row[5:])
            elif '–' not in salary and '-' in salary:  # Format "14 000 - 20 000 pln"
                min_salary, max_salary = salary.split('-')
                min_salary = int(min_salary.strip())
                max_salary = int(max_salary.strip())
                
                # Dodanie wiersza dla min
                writer.writerow(row[:3] + ['min', min_salary, currency] + row[5:])
                # Dodanie wiersza dla max
                writer.writerow(row[:3] + ['max', max_salary, currency] + row[5:])
            else:
                # Jeśli wynagrodzenie nie zawiera przedziału, dodajemy "unknown"
                writer.writerow(row[:3] + ['unknown', None, currency] + row[5:])

def convert_technologies_to_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        # Zmieniamy nazwę kolumny na 'technologies_json'
        header[4] = 'technologies_json'  # Zakładając, że kolumna 'Technologie' znajduje się na 4. miejscu
        writer.writerow(header)

        for row in reader:
            technologies_col = row[4]  # Załóżmy, że kolumna 'Technologie' jest na pozycji 4
            if technologies_col.startswith('[') and technologies_col.endswith(']'):  # Sprawdzamy, czy jest to lista
                # Usunięcie nawiasów i cudzysłowów, konwersja na listę
                technologies_list = technologies_col.strip("[]").replace("'", "").split(',')
                # Usuwanie białych znaków przed zapisaniem
                technologies_json = json.dumps([tech.strip() for tech in technologies_list if tech.strip()])
            else:
                technologies_json = '[]'  # Jeśli nie jest to poprawna lista, przypisujemy pustą listę w formacie JSON
            row[4] = technologies_json  # Zmieniamy zawartość kolumny 'Technologie' na JSON
            writer.writerow(row)

convert_to_tidy(input_csv_path, output_csv_path)
convert_technologies_to_json(input_csv_path, output_csv_path)
print(f"Zapisano dane w formacie Tidy Data do {output_csv_path}")
