import glob
from fpdf import FPDF
from pathlib import Path

# Create a list  of text  filepaths
filepaths = glob.glob("texts/*.txt")
# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    filename = Path(filepath).stem
    with open(filepath, "r") as file:
        content = file.read()
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{filename.title()}", ln=1)
    pdf.cell(w=50, h=8, txt="", ln=1)
    pdf.set_font(family="Times", size=14,)
    pdf.multi_cell(w=0, h=6, txt=content)


pdf.output(f"PDFs/texts.pdf")