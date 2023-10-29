import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP server details from cPanel
smtp_server = 'mail.xn--29ae4dgic.xn--y9a3aq'
smtp_port = 587  # or the appropriate port for your SMTP server
smtp_username = 'm_women@xn--29ae4dgic.xn--y9a3aq'
smtp_password = 'Women10201.'

# Sender and recipient addresses
sender_email = 'm_women@xn--29ae4dgic.xn--y9a3aq'
recipient_email = 'knersesk@gmail.com'

# Create a MIMEText object with the email content
subject = 'Test Email'
body = f"""
<html>
<body>

  <div>
    <p><strong>From:</strong> Nerses</p>
  </div>

  <div>
    <p><strong>Phone Number:</strong> 37498554100</p>
  </div>

  <div>
    <p><strong>Email Text:</strong></p>
    <p>some_email</p>
  </div>

</body>
</html>"""
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'html'))

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(smtp_username, smtp_password)
server.sendmail(sender_email, recipient_email, msg.as_bytes())
# Send the email

print('Email sent successfully.')