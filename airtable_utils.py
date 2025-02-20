import os
from pyairtable import Api
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Airtable credentials
AIRTABLE_ACCESS_TOKEN = os.getenv("AIRTABLE_ACCESS_TOKEN")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

# Initialize Airtable API
api = Api(AIRTABLE_ACCESS_TOKEN)
table = api.table(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME)

# Add this debug code before the add_travel_data function
try:
    # Get the first record to see field names
    first_record = table.first()
    if first_record:
        print("Available fields:", list(first_record['fields'].keys()))
except Exception as e:
    print(f"Debug error: {e}")

def add_travel_data(name, email, destination, start_date, end_date, duration, budget, travel_style):
    """
    Adds travel details to Airtable.
    """
    try:
        # Ensure Travel Style is passed as a list of strings
        travel_style_formatted = travel_style if isinstance(travel_style, list) else [travel_style]

        # Format dates for Airtable (YYYY-MM-DD format)
        formatted_start_date = start_date.strftime('%Y-%m-%d') if start_date else None
        formatted_end_date = end_date.strftime('%Y-%m-%d') if end_date else None

        record = {
            "Name": name,
            "email": email,
            "Destination": destination,
            "Start Date": formatted_start_date,
            "End Date": formatted_end_date,
            "Duration": float(duration),
            "Budget Level": budget,
            "Travel Style": travel_style_formatted
        }

        # Debug print to see what we're sending
        print("Attempting to create record:", record)

        response = table.create(record)
        print(f"✅ Data saved to Airtable: {response}")
        return True
    except Exception as e:
        print(f"❌ Error saving to Airtable: {e}")
        return False
