from flask import Flask, render_template, request
import smtplib
import os

MY_EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

app = Flask(__name__)

def send_mail(email, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  
        connection.starttls()  
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:New Message\n\nEmail:{email}\nMessage:{message}")

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Contact page 
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sendemail', methods=['POST'])
def sendemail():
    email = request.form['email_box']
    message = request.form['text_box']
    send_mail(email=email, message=message)
    return render_template('/email_send.html')

if __name__ == "__main__":
    app.run(debug=False)