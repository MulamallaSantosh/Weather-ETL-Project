import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
load_dotenv()

# CONFIGURATION

API_KEY = os.getenv("API_KEY")

cities = ["Munich", "Berlin", "Paris", "London", "Rome"]

# PostgreSQL connection
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Email configuration
sender_email = os.getenv("EMAIL_SENDER")
receiver_email = os.getenv("EMAIL_RECEIVER")
app_password = os.getenv("EMAIL_PASSWORD")


# STEP 1: EXTRACT

data = []

print("Starting ETL pipeline...")

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)

    if response.status_code == 200:
        weather = response.json()
        
        data.append({
            "city": city,
            "temperature": weather["main"]["temp"],
            "humidity": weather["main"]["humidity"],
            "pressure": weather["main"]["pressure"],
            "description": weather["weather"][0]["description"],
            "timestamp": datetime.now()
        })
    else:
        print(f"Error fetching data for {city}")


# STEP 2: TRANSFORM

df = pd.DataFrame(data)

if df.empty:
    print("No data extracted ")
    exit()

# Clean timestamp
df['timestamp'] = pd.to_datetime(df['timestamp']).dt.floor('s')

# Add temperature category
df['temp_category'] = df['temperature'].apply(
    lambda x: 'Cold' if x < 10 else 'Moderate' if x < 25 else 'Hot'
)

print("Data transformed successfully ")
print(df.head())


# STEP 3: LOAD (PostgreSQL)

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

df.to_sql("weather_data", engine, if_exists="append", index=False)

print(f"{len(df)} rows inserted into database")


# STEP 4: DATA-DRIVEN ALERTS

alerts = []

for index, row in df.iterrows():
    if row["temperature"] > 30:
        alerts.append(f"🔥 High Temperature in {row['city']}: {row['temperature']}°C")

    if row["temperature"] < 5:
        alerts.append(f"❄️ Low Temperature in {row['city']}: {row['temperature']}°C")

    if row["humidity"] > 80:
        alerts.append(f"🌧️ High Humidity in {row['city']}: {row['humidity']}%")


# STEP 5: EMAIL ALERT SYSTEM

if alerts:
    subject = "⚠️ Weather Alert Notification"
    message = "\n".join(alerts)
else:
    subject = "ETL Success"
    message = "ETL executed successfully. No critical alerts."

# Send email
msg = MIMEText(message)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)

    print("Email alert sent")

except Exception as e:
    print("Email failed :", e)
print("ETL pipeline executed successfully")