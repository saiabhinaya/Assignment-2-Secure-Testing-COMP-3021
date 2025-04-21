import os
import pymysql
import smtplib
from email.mime.text import MIMEText
from urllib.request import urlopen

# Database configuration
db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123',
    'database': 'mydb'  # Assuming the database name is 'mydb'
}

def get_user_input():
    """Get user input securely"""
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    """Send email using SMTP"""
    from_email = "your-email@example.com"  # Your email address
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to

    try:
        # Set up the SMTP server and send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(from_email, 'your-email-password')  # Login credentials for the email account
            server.sendmail(from_email, to, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

def get_data():
    """Get data from an insecure API"""
    url = 'http://insecure-api.com/get-data'
    try:
        data = urlopen(url).read().decode()
        return data
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return None

def save_to_db(data):
    """Save the fetched data to the database securely"""
    if data is None:
        print("No data to save.")
        return

    query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    try:
        # Establish the connection using 'with' to ensure proper resource management
        with pymysql.connect(**db_config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (data, 'Another Value'))
                connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error saving data to database: {e}")

if __name__ == '__main__':
    # Get user input
    user_input = get_user_input()
    
    # Fetch data from the API
    data = get_data()

    # Save the data to the database
    save_to_db(data)

    # Send an email with the user input
    send_email('admin@example.com', 'User Input', user_input)
