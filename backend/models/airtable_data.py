import requests
import os
from dotenv import load_dotenv

load_dotenv()

AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

BASE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
HEADERS = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}

def add_record(record_data):
    """Add a new record to Airtable."""
    response = requests.post(BASE_URL, headers=HEADERS, json={"fields": record_data})
    return response.json()

def get_records():
    """Fetch all records from Airtable."""
    response = requests.get(BASE_URL, headers=HEADERS)
    if response.status_code == 200:
        return response.json().get('records', [])
    return {"error": response.text}

def update_record(record_id, updated_data):
    """Update a record in Airtable by its record ID."""
    url = f"{BASE_URL}/{record_id}"
    response = requests.patch(url, headers=HEADERS, json={"fields": updated_data})
    return response.json()

def delete_record(record_id):
    """Delete a record from Airtable."""
    url = f"{BASE_URL}/{record_id}"
    response = requests.delete(url, headers=HEADERS)
    return response.status_code == 200

if __name__ == "__main__":
    # Example usage
    record = {"Name": "John Doe", "Company": "AI Solutions Inc"}
    print("Adding Record:", add_record(record))

    print("Fetching Records:", get_records())

    update_data = {"Company": "Updated AI Solutions"}
    print("Updating Record:", update_record("recXXXXXXXXXXX", update_data))

    print("Deleting Record:", delete_record("recXXXXXXXXXXX"))