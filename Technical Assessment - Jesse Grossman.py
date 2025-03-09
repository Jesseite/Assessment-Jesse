import csv
from faker import Faker

# Initialize the Faker object
fake = Faker()

# Function to generate random data
def fake_data_maker(rows):
    data = []
    for i in range(rows):
        record = [
            fake.first_name(),
            fake.last_name(),
            fake.date_of_birth().isoformat(),
            fake.address()
        ]
        # Add records to the list
        data.append(record)
    return data

print("data added")

# Number of fake records
rows = 1000
fake_data = fake_data_maker(rows)

# Write the data to a CSV file
with open('unfiltered_file.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['first_name', 'last_name', 'date_of_birth', 'address'])
    for record in fake_data:
        writer.writerow(record)

print("CSV file 'unfiltered_file.csv' created successfully")

# List of column names to anonymize
columns_to_anonymize = ['first_name', 'last_name', 'address']

# Placeholder values to use for anonymization
placeholder_values = ['Anonymized_fname', 'Anonymized_lname', 'Anonymized_address']

# Anonymize the CSV file
try:
    # Read in the CSV file
    with open('unfiltered_file.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        field_names = reader.fieldnames
        
        # Create a new CSV file for the anonymized data
        with open('anonymized_file.csv', 'w', newline='') as anonymized_file:
            writer = csv.DictWriter(anonymized_file, fieldnames=field_names)
            writer.writeheader()

            # Iterate over the rows in the original CSV file
            for row in reader:
                # Anonymize the values in the specified columns
                for column, placeholder in zip(columns_to_anonymize, placeholder_values):
                    if column in row:
                        row[column] = placeholder
                # Write the anonymized row to the new CSV file
                writer.writerow(row)

    print("CSV file 'anonymized_file.csv' created successfully")

except FileNotFoundError:
    print('Error: "unfiltered_file.csv" not found.')