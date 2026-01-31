import os
import csv
import json

def load_csv(file_path):
    """Load data from a CSV file and return a list of rows."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def clean_data(data):
    """Remove empty fields and trim whitespace."""
    cleaned = []
    for row in data:
        cleaned_row = {key: value.strip() for key, value in row.items() if value}
        cleaned.append(cleaned_row)
    return cleaned


def filter_data(data, key, value):
    """Filter rows where a specific key matches a value."""
    return [row for row in data if row.get(key) == value]


def save_to_json(data, output_path):
    """Save processed data to a JSON file."""
    with open(output_path, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {output_path}")


def main():
    csv_file = "input_data.csv"
    json_output = "processed_data.json"

    try:
        print("Loading CSV...")
        data = load_csv(csv_file)

        print("Cleaning data...")
        cleaned = clean_data(data)

        print("Filtering data (example: role == 'student')...")
        filtered = filter_data(cleaned, "role", "student")

        print("Saving to JSON...")
        save_to_json(filtered, json_output)

        print("Processing complete!")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
