import smtplib
email = "jatinsinghmehras@gmail.com"
receiver = "mehrajatinsingh@gmail.com"

subject = "HEllo"
messgae = "MEOW MOEWMMMMMOEMWOMEOWE"

text = f"Subject: {subject}\n\n{messgae}"

server = smtplib.SMTP("smtp.gmail.com")
server.starttls()

server.login(email,"wayjezumbmweegnt")

server.sendmail(email,receiver,text)

print("EMAIL SENT !")