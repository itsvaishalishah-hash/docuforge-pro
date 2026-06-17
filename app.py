"""
Language: Python 3.14.5
Key Libraries: streamlit, pypdf, reportlab, Pillow, pdf2image, pytesseract
Purpose: Execute optical character recognition alongside structural document manipulation.
Book: Build a Smart Document Operations Center with Python
"""

import streamlit as st
from pypdf import PdfReader, PdfWriter
import io
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from PIL import Image
import pdf2image
import pytesseract

# Explicit fallback for Windows users if the system path fails.
# Uncomment and update the line below ONLY if TesseractNotFoundError occurs.
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.set_page_config(page_title="DocuForge Pro", layout="wide")


def create_watermark(text, opacity_percent):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=(595, 842))
    c.translate(300, 400)
    c.rotate(45)
    c.setFont("Helvetica-Bold", 60)
    opacity_value = opacity_percent / 100.0
    c.setFillColor(Color(0.5, 0.5, 0.5, alpha=opacity_value))
    c.drawCentredString(0, 0, text)
    c.save()
    packet.seek(0)
    return packet


def parse_page_ranges(range_string, max_pages):
    pages_to_extract = []
    if not range_string:
        return pages_to_extract
    parts = range_string.split(",")
    for part in parts:
        part = part.strip()
        if "-" in part:
            start_str, end_str = part.split("-")
            start = int(start_str) - 1
            end = int(end_str) - 1
            start = max(0, start)
            end = min(max_pages - 1, end)
            for i in range(start, end + 1):
                if i not in pages_to_extract:
                    pages_to_extract.append(i)
        else:
            if part.isdigit():
                page_num = int(part) - 1
                if 0 <= page_num < max_pages and page_num not in pages_to_extract:
                    pages_to_extract.append(page_num)
    return sorted(pages_to_extract)


with st.sidebar:
    st.title("DocuForge Pro")
    st.caption("Zero-Cost Local Processing")
    st.divider()

    operation = st.radio(
        "Select Operation",
        ["Merge", "Split", "Watermark", "Secure & Optimize", "OCR Scanner"],
    )

    st.divider()
    st.subheader("Configuration")

    page_ranges = ""
    watermark_text = "CONFIDENTIAL"
    opacity_level = 50
    encryption_password = ""

    if operation == "Split":
        page_ranges = st.text_input("Page Ranges", placeholder="e.g., 1-5, 8, 11-13")
    elif operation == "Watermark":
        watermark_text = st.text_input("Watermark Text", value="CONFIDENTIAL")
        opacity_level = st.slider("Opacity (%)", 10, 100, 50)
    elif operation == "Secure & Optimize":
        encryption_password = st.text_input("Encryption Password", type="password")
    elif operation == "OCR Scanner":
        st.caption(
            "Note: OCR is highly CPU intensive. Please process one file at a time."
        )
    elif operation == "Merge":
        st.caption(
            "No additional configuration required. Files will merge in top-to-bottom order."
        )

st.title("Batch Execution Zone")
st.caption("All operations execute securely in local volatile memory.")

uploaded_files = st.file_uploader(
    "Drag and drop documents or images here",
    accept_multiple_files=True,
    type=["pdf", "png", "jpg", "jpeg"],
)

if uploaded_files:
    st.write(f"Files in queue: {len(uploaded_files)}")
    for file in uploaded_files:
        st.text(f"- {file.name} ({round(file.size / 1024, 1)} KB)")

st.divider()
is_disabled = len(uploaded_files) == 0

if st.button("Execute Operation", disabled=is_disabled):
    with st.spinner("Executing secure local operation..."):
        try:
            if operation == "Merge":
                writer = PdfWriter()
                for file in uploaded_files:
                    reader = PdfReader(file)
                    for page in reader.pages:
                        writer.add_page(page)

                output_buffer = io.BytesIO()
                writer.write(output_buffer)
                output_buffer.seek(0)

                st.success("Merge complete! Artifact ready for secure download.")
                st.download_button(
                    label="Download Merged Document",
                    data=output_buffer,
                    file_name="merged_output.pdf",
                    mime="application/pdf",
                )

            elif operation == "Split":
                target_file = uploaded_files[0]
                reader = PdfReader(target_file)
                total_pages = len(reader.pages)
                pages_to_extract = parse_page_ranges(page_ranges, total_pages)

                if not pages_to_extract:
                    st.error("Please enter a valid page range.")
                else:
                    writer = PdfWriter()
                    for idx in pages_to_extract:
                        writer.add_page(reader.pages[idx])

                    output_buffer = io.BytesIO()
                    writer.write(output_buffer)
                    output_buffer.seek(0)

                    st.success("Split complete! Artifact ready for secure download.")
                    st.download_button(
                        label="Download Split Document",
                        data=output_buffer,
                        file_name="split_output.pdf",
                        mime="application/pdf",
                    )

            elif operation == "Watermark":
                target_file = uploaded_files[0]
                reader = PdfReader(target_file)
                writer = PdfWriter()

                stamp_buffer = create_watermark(watermark_text, opacity_level)
                stamp_reader = PdfReader(stamp_buffer)
                stamp_page = stamp_reader.pages[0]

                for page in reader.pages:
                    page.merge_page(stamp_page)
                    writer.add_page(page)

                output_buffer = io.BytesIO()
                writer.write(output_buffer)
                output_buffer.seek(0)

                st.success("Watermark applied! Artifact ready for secure download.")
                st.download_button(
                    label="Download Watermarked Document",
                    data=output_buffer,
                    file_name="watermarked_output.pdf",
                    mime="application/pdf",
                )

            elif operation == "Secure & Optimize":
                target_file = uploaded_files[0]
                reader = PdfReader(target_file)
                writer = PdfWriter()

                for page in reader.pages:
                    writable_page = writer.add_page(page)
                    writable_page.compress_content_streams()

                writer.add_metadata(
                    {"/Producer": "DocuForge Pro", "/Creator": "DocuForge Pro"}
                )

                if encryption_password:
                    writer.encrypt(encryption_password, algorithm="AES-256")
                else:
                    st.warning(
                        "No password provided. The file will be optimized but left unlocked."
                    )

                output_buffer = io.BytesIO()
                writer.write(output_buffer)
                output_buffer.seek(0)

                st.success(
                    "File secured, scrubbed, and compressed! Ready for download."
                )
                st.download_button(
                    label="Download Secured Document",
                    data=output_buffer,
                    file_name="secured_output.pdf",
                    mime="application/pdf",
                )

            elif operation == "OCR Scanner":
                target_file = uploaded_files[0]
                file_extension = target_file.name.split(".")[-1].lower()
                extracted_text = ""

                if file_extension in ["png", "jpg", "jpeg"]:
                    img = Image.open(target_file)
                    extracted_text = pytesseract.image_to_string(img)
                else:
                    raw_bytes = target_file.read()
                    images = pdf2image.convert_from_bytes(raw_bytes, dpi=300)
                    for img in images:
                        page_text = pytesseract.image_to_string(img)
                        extracted_text += page_text + "\n\n--- Page Break ---\n\n"

                if extracted_text.strip():
                    st.success("Text successfully extracted from image arrays.")
                    st.text_area(
                        "Extracted Text Payload", value=extracted_text, height=400
                    )

                    st.download_button(
                        label="Download Raw Text File",
                        data=extracted_text,
                        file_name="extracted_data.txt",
                        mime="text/plain",
                    )
                else:
                    st.warning(
                        "The vision engine could not detect any readable text in this file."
                    )

        except Exception as e:
            st.error(
                f"Execution failed. Ensure your file is not corrupted. System message: {e}"
            )

# Inject the custom application footer
st.markdown(
    """
    <div style='text-align: center; margin-top: 50px; color: #888888; font-size: 14px;'>
        Build a Smart Document Operations Center with Python<br>
        &copy; 2026 Sharanam and Vaishali Shah
    </div>
    """,
    unsafe_allow_html=True,
)
