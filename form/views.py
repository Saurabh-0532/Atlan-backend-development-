from django.core.mail import send_mail
def mailing(request):
            send_mail(
                "Subject here",
                "Here is the message.",
                "enddev02@gmail.com",
                ["saurabhyadav1280@gmail.com"],
                fail_silently=False,
                )