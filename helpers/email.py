from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from mybase import settings

def sendMail(message, recepiants, subject,template):  #template= 'filename.html'
    try:
        email_html_message = render_to_string(template, message)
        email = EmailMultiAlternatives(subject, email_html_message, settings.DEFAULT_FROM_EMAIL, [recepiants])
        email.attach_alternative(email_html_message, "text/html")
        email.send()
        return True
    except Exception as e:
        print(e)
        return False
        