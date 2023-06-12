import smtplib
import pandas
import datetime as dt
import random
from collections import defaultdict
import json

# Function to send email
def send_email(to_email):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=login_data["from_email"], password=login_data["from_password"])
        connection.sendmail(from_addr=login_data["from_email"], 
                            to_addrs=to_email, 
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
try:
    # Checking for files
    with open ("secret.json", mode='r') as login_data:
        login_data = json.load(login_data)
    data = pandas.read_csv("secretbirthdays.csv")
except:
    print("secret.json with login details or secretbirthdays.csv is missing.")
else:
    # Retrieve today's month and day
    now = dt.datetime.now()
    today = (now.month, now.day)
    birthday_dict = defaultdict(list)
    # Create birthday dictionary from the csv file
    for (index, data_row) in data.iterrows():
        key = (data_row.month, data_row.day)
        birthday_dict[key].append(data_row)
    # If there are any birthdays today, randomly select card text file, 
    # replace name and call send email function
    if today in birthday_dict:
        file_path = f"./letter_templates/card_{random.randint(1,3)}.txt"
        birthday_record = birthday_dict[today]
        for item in birthday_record:
            with open(file_path) as letter_file:
                contents = letter_file.read()
                contents = contents.replace("[NAME]", item["name"])
                to_email = item["email"]
                send_email(to_email)
