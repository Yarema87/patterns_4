import csv


def read_csv(file_path: str) -> list[dict]:
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
