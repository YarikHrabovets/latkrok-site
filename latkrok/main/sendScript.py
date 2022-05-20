import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version

def send_for_email(email, fn, ln, text):
    server = 'smtp.gmail.com'
    user = 'latkrokhelp@gmail.com'
    password = 'LatkrokHelp2901'

    sender = 'latkrokhelp@gmail.com'
    subject = f'Ваша заявка на заказ успешно отправлена'
    html = f'''<html>
                    <head>
                    </head>
                    <body>
                        <img src='https://latkrok.com.ua/image/catalog/latkrok-logo.png'>
                        <h1>Здравствуйте {fn} {ln}!</h1>
                        <h3>Мы получили вашу заявку и скоро свяжемся с вами</h3>
                        <br>
                        <br>
                        <h2>Информация про ваш заказ</h2>
                        <br>
                        <p style='font-size: 24px;'>{text.replace(',', '                                          ')}</>
                        <div style='margin-top: 30px; background-color: #000; color: #ccc; padding: 10px;'>
                            <p>Вы получили это письмо, поскольку на сайте</p><a href='https://latkrok.in.ua/'>latkrok.in.ua</a>
                            <p>было оформлено заказ на адрес {email}</p>
                            <p>С уважением, команда Latkrok</p>
                            <p>	07400, г. Бровары, бул. Независимости 26/2</p>
                        </div>
                    </body>
                </html>'''

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Latkrok Support <' + sender + '>'
    msg['To'] = email
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())

    part_text = MIMEText(text, 'plain')
    part_html = MIMEText(html, 'html')

    msg.attach(part_text)
    msg.attach(part_html)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, email, msg.as_string())
    mail.quit()