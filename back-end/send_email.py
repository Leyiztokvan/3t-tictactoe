from email.mime.text import MIMEText
import smtplib

# This works but with security risk
def send_email(email__, pwd__, first_name, last_name,):
    # from_email="codedummyemail@gmail.com"
    # from_password="Fool-email1"
    from_email="tttinfomail@gmail.com"
    from_password="tictactoe"
    to_email=email__

    subject="TicTacToe Game Score"

        
    message="Dear <strong>%s</strong> <strong>%s</strong>  <br> Your score is <strong>%s</strong> points. <br> Thank you for participating. <br> Kind regards. <br> Developing Team. "  % (first_name, last_name, pwd__,)

    
    msg=MIMEText(message, "html")
    msg["Subject"]=subject
    msg["From"]=from_email
    msg["To"]=to_email
    
    
    gmail=smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo() 
    gmail.starttls() 
    gmail.login(from_email, from_password)
    gmail.send_message(msg)