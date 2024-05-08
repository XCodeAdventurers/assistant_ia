from pypdf import PdfReader 
from django.conf import settings


def extract_text_to_pdf(file_path):
    reader = PdfReader(file_path) 
    result_path = settings.BASE_DIR / "media/documents/plan_comptable_syscoada.txt"
    with open(result_path, 'w') as f:
        for page in reader.pages:
            f.write(page.extract_text() )
    return ""

def run():
    extract_text_to_pdf('media/plan_comptable.pdf')