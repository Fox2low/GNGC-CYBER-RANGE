import smtplib

sender = "Private Person <from@example.com>"
receiver = "A Test User <ante882005@gmail.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.login("dcafb75baa74ff", "2821f41f5e0c24")
    server.sendmail(sender, receiver, message)