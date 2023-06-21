from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0) #else it generate more pages if use footer

df = pd.read_csv("topics.csv")
df = pd.read_csv("topics.csv")


def lines():
# def lines(y=21,r=26): #for blank lists need provide y=11 , r=27
    # pdf.line(10, y, 200, y)
    # for i in range(r):
    #     y += 10
    #     pdf.line(10, y, 200, y)
    #Author method by using range
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)



for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    lines()

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] -1):
        pdf.add_page()
        lines()

        #Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")