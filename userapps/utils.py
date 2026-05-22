from django.core.mail import send_mail
from django.conf import settings
def sendMail(fullname,email):
    subject = "Welcome to Elixir Application, please click link to complete registration"
    message = f'''
                Hi {fullname},
                Thank you for registering with us.
                
                '''
    
    send_mail(
    subject,
    message,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
)