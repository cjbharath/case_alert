import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time

# Twilio credentials (replace with your actual credentials)
TWILIO_SID = "AC9c9c9abfb6eebc30f225267fc171ceaf"
TWILIO_AUTH_TOKEN = "f7edebe581889976389563add99d32ba"
TWILIO_PHONE_NUMBER = "+17014078299"
YOUR_PHONE_NUMBER = "+919443589239"

# Your case number to check
YOUR_CASE_NUMBER = "WP.6725/2025"

def send_sms(message):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=YOUR_PHONE_NUMBER
    )

def check_case():
    url = "https://hcmadras.tn.gov.in/display_board_mhc.php"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    content = soup.get_text()

    if YOUR_CASE_NUMBER in content:
        send_sms(f"Your case {YOUR_CASE_NUMBER} is displayed on the website!")
        return True
    return False

# Run the script every minutes
while True:
    found = check_case()
    if found:
        break
    time.sleep(60)  # Check every minutes
