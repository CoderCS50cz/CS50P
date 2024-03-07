from fpdf import FPDF


name = input("Name: ")


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 40)
        self.set_text_color(0, 0, 0)
        self.cell(200, 75, "CS50 Shitrificate", align = "C")


pdf = PDF(orientation = "P", unit = "mm", format = "A4")
pdf.add_page()
pdf.image("shirtificate.png", x = 10, y = 80, w = 190)
pdf.set_font("helvetica", "B", 23)
pdf.set_text_color(255, 255, 255)
pdf.set_y(pdf.eph/2)
pdf.cell(190, 30, f"{name} took CS50", align = "C")
pdf.output("shirtificate.pdf")
