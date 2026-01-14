from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def gerar_pdf(numero, cliente):
    nome = f"orcamento_{numero}.pdf"
    c = canvas.Canvas(nome, pagesize=A4)

    c.drawString(50, 800, f"Orçamento Nº {numero}")
    c.drawString(50, 770, f"Cliente: {cliente}")

    c.save()
    return nome
