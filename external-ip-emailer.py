from requests import get
import smtplib
import ssl
import time
#IMPORTANT YOU MUST HAVE ALLOW LESS SECURE APPS ENABLED ON YOUR GMAIL ACCOUNT

def send_email(message):
    port = 465 
    password = #EMAIL PASSWORD
    context = ssl.create_default_context() #starts secure ssl context

              
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context = context) as server:
        server.login('ADDRESS TO SEND FROM', password)
        #connection established
    
        #send email
        server.sendmail('ADDRESS TO SEND FROM', 'ADDRESS TO SEND TO', message)


def get_ip():
    ip = ''
    ip_bad = get('https://api.ipify.org?format=json').text

    #removes extra shit in the ip (not neccasary just nice)
    for i in range(len(ip_bad)):
        if i > 6 and i < len(ip_bad) - 2:
            ip += ip_bad[i]
    return(ip)

#actually detects change in ip and emails new ip to me
def do_shit():
    #gets old ip address
    file = open('ip_address.txt', 'r')
    old_ip = file.read()
    file.close()

    #compares ip saved to file and current if ip has changed it will write the new one and email it
    if old_ip != get_ip():
        file = file = open('ip_address.txt', 'w')
        file.write(get_ip())
        file.close()
        send_email(get_ip())


#waits two hours then checks for change in ip if changed it will email me the new one
while True:
    do_shit()
    time.sleep(7200)
