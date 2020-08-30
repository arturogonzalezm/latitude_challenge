import csv
import datetime
from faker import Faker

RECORD_COUNT = 1000000
fake = Faker()


def create_csv_file():
    with open('data/people.csv', 'w', newline='') as csv_file:
        field_names = ['first_name', 'last_name', 'email', 'address', 'city', 'state', 'country', 'date_of_birth']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'first_name': fake.name(),
                    'last_name': fake.name(),
                    'email': fake.email(),
                    'address': fake.street_address(),
                    'city': fake.city(),
                    'state': fake.state(),
                    'country': fake.country(),
                    'date_of_birth': fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1, 1))
                }
            )
