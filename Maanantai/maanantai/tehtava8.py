import requests
r = requests.get("http://104.47.143.222")

while True:
    r = requests.get("http://104.47.143.222")
    print(r.status_code)

    if r.status_code == 200:
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        fromaddr = "testi@gmail.com"
        toaddr = "spockteroo@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Health check"

        body = "Kaikki koneella ok!"
        msg.attach(MIMEText(body, 'plain'))

        import smtplib
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("spockteroo", "Tosisalainen1!")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
    else:
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        fromaddr = "testi@gmail.com"
        toaddr = "spockteroo@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Kone rikki"

        body = "Kone on alhaalla"
        msg.attach(MIMEText(body, 'plain'))

        import smtplib
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("spockteroo", "Tosisalainen1!")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
