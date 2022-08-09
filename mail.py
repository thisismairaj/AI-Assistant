import smtplib 

smtpServer = "smtp.gmail.com"
smtpPort = 587
smtpUsername = "thehamzak@gmail.com"
smtpPassword = "2Security*Hamzak.com"
toAddress = "thisismairaj@gmail.com"
fromAddress = "thehamzak@gmail.com"

body = """From: From Pepipost <thehamzak@gmail.com>
To: MrRobot <thisismairaj@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP test email
This is an e-mail message to be sent in HTML format using smtplib.
This is HTML message.
This is headline.

"""

mailServer = smtplib.SMTP(smtpServer , smtpPort)
mailServer.starttls()
mailServer.login(smtpUsername , smtpPassword)
mailServer.sendmail(fromAddress, toAddress , body)
print(" \n Sent!")
mailServer.quit()