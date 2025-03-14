from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def text_to_pdf(txt_file, pdf_file):
    if not os.path.exists(txt_file):
        print("❌ ERROR: Text file not found.")
        return

    with open(txt_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.setFont("Helvetica", 12)

    y_position = 750  # Starting Y position for text

    for line in lines:
        c.drawString(100, y_position, line.strip())  # Draw each line of text
        y_position -= 20  # Move down for the next line

        # Create new page if text reaches bottom
        if y_position < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y_position = 750

    c.save()
    print(f"✅ Successfully converted {txt_file} to {pdf_file}")

if __name__ == "__main__":
    txt_file = input("Enter the path of the text file to convert: ").strip()
    pdf_file = txt_file.replace(".txt", ".pdf")  # Save as PDF with same name
    text_to_pdf(txt_file, pdf_file)
