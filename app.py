import streamlit as st
import PyPDF2
import io
import docx2txt
import pyperclip

st.title("Document Viewer")

# File uploader
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # Read file contents
    file_contents = uploaded_file.read()

    # Extract text from PDF
    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_contents))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

    # Extract text from Word document
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = docx2txt.process(io.BytesIO(file_contents))

    # Copy text from clipboard
    elif uploaded_file.type == "application/octet-stream":
        text = pyperclip.paste()

    # Display text
    st.text_area("Text", value=text, height=400)