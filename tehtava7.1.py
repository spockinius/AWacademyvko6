from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

fromaddr = "testi@gmail.com"
toaddr = "spockteroo@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Minäpäs testailen mailailua"

body = "Täältä tämä tulee!"
msg.attach(MIMEText(body, 'plain'))

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("spockteroo", "Tosisalainen1!")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)