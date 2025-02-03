import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

AIRTABLE_API_URL = os.getenv("AIRTABLE_API_URL")
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")

HEADERS = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}

def get_records():
    """Fetch all records from the Airtable table."""
    try:
        response = requests.get(AIRTABLE_API_URL, headers=HEADERS)
        response.raise_for_status()
        records = response.json().get("records", [])
        return records
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch records: {str(e)}"}

def add_record(record_data):
    """Add a new record to the Airtable table."""
    try:
        response = requests.post(AIRTABLE_API_URL, headers=HEADERS, json={"fields": record_data})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to add record: {str(e)}"}

def update_record(record_id, record_data):
    """Update an existing record in the Airtable table."""
    try:
        url = f"{AIRTABLE_API_URL}/{record_id}"
        response = requests.patch(url, headers=HEADERS, json={"fields": record_data})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to update record: {str(e)}"}

def delete_record(record_id):
    """Delete a record from the Airtable table."""
    try:
        url = f"{AIRTABLE_API_URL}/{record_id}"
        response = requests.delete(url, headers=HEADERS)
        response.raise_for_status()
        return {"message": "Record deleted successfully"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to delete record: {str(e)}"}


# Example Usage
if __name__ == "__main__":
    # Example record data
    sample_data = {"Name": "John Doe", "Company": "Prixite"}

    # Add a new record
    print(add_record(sample_data))

    # Fetch all records
    print(get_records())
