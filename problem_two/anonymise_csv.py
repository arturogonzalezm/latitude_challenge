import unicodecsv as csv

from faker import Factory
from collections import defaultdict


def anonymize_rows(rows):
    """
    Rows is an iterable of dictionaries that contain name and
    email fields that need to be anonymised.
    """
    # Load faker
    faker = Factory.create()

    # Create mappings of names, emails, social security numbers, and phone numbers to faked names & emails.
    names = defaultdict(faker.name)
    emails = defaultdict(faker.email)
    ssns = defaultdict(faker.ssn)
    phone_numbers = defaultdict(faker.phone_number)

    # Iterate over the rows from the file and yield anonymised rows.
    for row in rows:
        # Replace name and email fields with faked fields.
        row["name"] = names[row["name"]]
        row["email"] = emails[row["email"]]
        row["ssn"] = ssns[row["ssn"]]
        row["phone_number"] = phone_numbers[row["phone_number"]]

        # Yield the row back to the caller
        yield row


def anonymize(source, target):
    """
    The source argument is a path to a CSV file containing data to anonymize,
    while target is a path to write the anonymised CSV data to.
    """
    with open(source, 'rU') as f:
        with open(target, 'w') as o:
            # Use the DictReader to easily extract fields
            reader = csv.DictReader(f)
            writer = csv.DictWriter(o, reader.fieldnames)

            # Read and anonymize data, writing to target file.
            for row in anonymize_rows(reader):
                writer.writerow(row)

