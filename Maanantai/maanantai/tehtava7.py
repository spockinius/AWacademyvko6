import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()
server.ehlo()

server.login("spockteroo", "Tosisalainen1!")

msg = "\nHello!" # The /n separates the message from the headers (which we ignore for this example)
server.sendmail("katariinahava@gmail.com", "spocketroo@gmail.com", msg)
