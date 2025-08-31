from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

def generate_test_report_pdf(test):
    html_string = render_to_string('pdf/test_report.html', {'test': test})
    html = HTML(string=html_string)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as output:
        html.write_pdf(output.name)
        return output.name
