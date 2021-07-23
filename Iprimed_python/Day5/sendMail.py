import smtplib
connection = smtplib.SMTP ("smtp.gmail.com",587)
connection.starttls()
connection.login("chedivya1998@gmail.com","Welcome@2169")
message = "Hi lusu,yen uyira vangura"
connection.sendmail("chedviya1998@gmail.com","amarthiga@gmail.com",message)
print("email has sent successfully")
connection.quit()
