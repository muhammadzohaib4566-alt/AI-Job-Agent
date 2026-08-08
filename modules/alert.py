import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_alert(job):
    company = job.get("Company", "")
    position = job.get("Position", "")
    location = job.get("Location", "")
    score = job.get("Score", 0)
    apply_link = job.get("Apply", "")

    sender = os.getenv("EMAIL_SENDER")
    app_password = os.getenv("EMAIL_APP_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    if not sender or not app_password or not receiver:
        print("Email settings are missing.")
        return

    msg = EmailMessage()

    msg["Subject"] = f"AI Job Alert: {position} - Score {score}"
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content(
        f"""HIGH MATCH JOB ALERT

Company: {company}
Position: {position}
Location: {location}
Score: {score}

Apply:
{apply_link}
"""
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, app_password)
            smtp.send_message(msg)

        print(f"Email alert sent: {position} | Score: {score}")

    except Exception as e:
        print(f"Email alert failed: {e}")