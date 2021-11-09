import smtplib
to = input('Enter the email of recipent:\n')
content = input('Enter the msg that u want to send:\n')

def sendmail(to ,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('arunmadhopur750@gmail.com' ,9116016932)
    server.sendmail('arunmadhopur750@gmail.com' ,to ,content)
    server.close()

sendmail(to, content)

