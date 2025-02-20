import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load environment variables
load_dotenv()

# Email Credentials
EMAIL_SENDER = os.getenv("EMAIL_SENDER")  # Your email (e.g., Gmail)
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # App Password for Gmail SMTP

def generate_calendar_link(destination, start_date, end_date, duration):
    """
    Generates a Google Calendar event link for the trip.
    """
    calendar_title = f"Trip to {destination}"
    calendar_description = f"Plan your {duration}-day trip to {destination}."
    start_date_str = start_date.strftime("%Y%m%d")
    end_date_str = end_date.strftime("%Y%m%d")

    return f"https://www.google.com/calendar/render?action=TEMPLATE&text={quote_plus(calendar_title)}&dates={start_date_str}/{end_date_str}&details={quote_plus(calendar_description)}"

def send_travel_email(user_email, name, itinerary, destination, start_date, end_date, duration):
    """
    Sends an email with the generated travel itinerary and calendar booking link.
    """
    try:
        # Generate Calendar Booking Link
        calendar_link = generate_calendar_link(destination, start_date, end_date, duration)

        subject = f"Your Travel Itinerary for {destination} ✈️"
        body = f"""
        Hi {name},

        Your AI-powered travel itinerary is ready! Here are your trip details:

        {itinerary}

        📅 **Click below to add this trip to your calendar:**
        👉 [Book Your Trip on Google Calendar]({calendar_link})

        Safe travels! ✈️🌍  

        Regards,  
        AI Travel Planner
        """

        # Setup email message
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = user_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to SMTP Server
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # Using SSL
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, user_email, msg.as_string())
        server.quit()

        print(f"✅ Email sent successfully to {user_email}")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False
