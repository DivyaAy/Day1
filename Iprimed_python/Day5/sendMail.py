import smtplib
connection = smtplib.SMTP ("smtp.gmail.com",587)
connection.starttls()
connection.login("chedivya1998@gmail.com","Welcome@2169")
message = "Hi Gulshan,how are you"
connection.sendmail("chedviya1998@gmail.com","gulshankumar060699@gmail.com",message)
print("email has sent successfully")
connection.quit()
