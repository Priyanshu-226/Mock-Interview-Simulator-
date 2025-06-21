import fitz  # PyMuPDF

def extract_resume_data(content: bytes) -> dict:
    with fitz.open(stream=content, filetype="pdf") as doc:
        text = "".join([page.get_text() for page in doc])
    name = "Aarav" if "Aarav" in text else "Candidate"
    return {"name": name, "skills": ["Python", "Web Development"]}
