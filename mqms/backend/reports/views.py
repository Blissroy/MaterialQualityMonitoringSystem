from django.core.mail import EmailMessage
from .utils.pdf_generator import generate_test_report_pdf

def send_test_report_email(test, recipient_email):
    pdf_path = generate_test_report_pdf(test)

    email = EmailMessage(
        subject="Material Test Report",
        body="Please find attached the test report.",
        from_email="noreply@qualitysystem.com",
        to=[recipient_email]
    )
    email.attach_file(pdf_path)
    email.send()
from django.http import HttpResponse

def reports_home(request):
    return HttpResponse("Reports API Home 📊")
