# Birthday Wisher #
Automatically send birthday wishes to your friends and family

## Setup ##

- Rename samplebirthdays.csv to secretebirthdays.csv with your friends & family's birthday details. 
    - YourName,your_own@email.com,today_year,today_month,today_da
       - e.g.name,email,year,month,day
    - Make sure one of the entries matches today's date for testing purposes.

- Create a secret.json file with the following key-value pairs

    - from_email: The email you want to send the message from.
    - from_password: The app password not your email password. Generate app password from your email provider.

        ```
        {
            "from_email": "example@gmail.com",
            "from_password": "",
        }
        ```

- Non Gmail Accounts:
    - If your 'from email' is not gmail, please edit and add the correct SMTP server and port. 
   