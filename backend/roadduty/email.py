from django.core.mail import send_mail
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


def send_email_to_user(user_name, user_email, location, challan_id):
    subject = "You have a challan!"
    html_template = "core\email_template.html"
    to_email = user_email
    print(to_email, user_name)
    from_email = 'email.from.machine.here@gmail.com'
    context = {"rider_name": user_name, "location": location, "challan_id": challan_id}
    html_message = render_to_string(html_template, context)
    message = EmailMessage(subject, html_message, from_email, [to_email])
    message.content_subtype = "html"
    message.send()

    # send_mail(
    #     subject='Subject here',
    #     message='Here is the message.',
    #     from_email='email.from.machine.here@gmail.com',
    #     recipient_list=['shubh67676@gmail.com', '1245lazy@gmail.com'],
    #     fail_silently=False,
    # )
