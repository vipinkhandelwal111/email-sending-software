import smtplib ,webbrowser
def get_mail():
    servicesAvailable=['hotmail','gmail','yahoo','outlook']
    while True:
        mail_id=input("E-mail: ")
        if '@' in mail_id and '.com' in mail_id:
            #xyz@gmail.com
            symbol_pos=mail_id.find("@")
            dotcom_pos=mail_id.find(".com")
            sp=mail_id[symbol_pos+1:dotcom_pos]
            if sp in servicesAvailable:
                return mail_id,sp
                #tuple
                #(xyz@gmail.com,gmail)
                break
            else:
                print("we don't provide services for"+sp)
                print("we provide services only for :gmail,yahoo,outlook,hotmail")
                continue
        else:
             print("invalid e-mail retype again")
             continue


def set_smtp_domain(serviceProvider):
    if serviceProvider=="gmail":
        return 'smtp.gmail.com'
    elif serviceProvider=="outlook" or serviceProvider=="hotmail":
        return 'smtp-mail.outlook.com'
    elif serviceProvider=="yahoo":
        return 'smtp.mail.yahoo.com'

print("welcome you can send an email through this program")
print("please enter your email and password : ")


e_mail,serviceProvider=get_mail()
password=input("Password : ")

while True:
    try:
        smtpDomain=set_smtp_domain(serviceProvider)
        connection=smtplib.SMTP(smtpDomain,587)
        connection.ehlo()
        connection.starttls()
        connection.login(e_mail,password)

    except:
        if serviceProvider=='gmail':
            print("login unsuccessful,there are 2 possible reasons : ")
            print("1.)you have typed wrong username or password")
            print("2.)you are using gmail there is an option in gmail 'allow lesssecure apps'")
            print("3.)do you want to open a webpage from where you can enable this option")
            answer=input("yes or no? : ")
            if answer=="yes":
                webbrowser.open("http://myaccount.google.com/lesssecureapps")
            else:
                print("unable to open")
                print("visit http://myaccount.google.com/lesssecureapps")

            print("retype your email or password")
            e_mail,serviceProvider=get_mail()
            password = input("password : ")
            continue
    else:
            print("login successful")
            break
print("please, type reciever's email address")
recieverAddress,recieverSP=get_mail()
print("enter the subject and message")
subject=input("Subject:")
message=input("Message:")
connection.sendmail(e_mail,recieverAddress,("Subject: "+str(subject)+"\n\n"+str(message)))
print("e-mail sent successfully")
connection.quit()
