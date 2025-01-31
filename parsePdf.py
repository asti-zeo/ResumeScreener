import fitz

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])
    return text


# resume_text = extract_text_from_pdf('resume.pdf')
# print(resume_text)
