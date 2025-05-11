import secrets
import os
from PIL import Image
from flask import url_for
import smtplib
from flask import current_app
from dotenv import load_dotenv
from pathlib import Path
from email.mime.text import MIMEText

def save_picture(form_picture):
    random = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fnn = random + f_ext
    picture_path = os.path.join(current_app.root_path,'static/assets',picture_fnn)

    #RESIZE
    resize = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(resize)

    i.save(picture_path)
    return picture_fnn


def send_reset_email(user):
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)
    token = user.get_reset_token()
    receiver = user.email
    subject = "PASSWORD RESET"
    message = f"""\
To reset your password 😶‍🌫️, visit the following link:🌚

{url_for('users.reset_token', token=token, _external=True)}

✨🫂

If you did not make this request then simply ignore this email 🤣 and no changes will be made.
"""
    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = os.getenv('EMAIL')
    msg["To"] = receiver
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(os.getenv('EMAIL'),os.getenv('PASS'))
    server.sendmail(os.getenv('EMAIL'),receiver,msg.as_string())
    server.quit()
    print("EMAIL SENT")

