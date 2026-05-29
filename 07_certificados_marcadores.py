from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black

OUTPUT_PATH = r"C:\Users\hp\Documents\kit-biblico-infantil\07_Certificados_Marcadores_Calendario.pdf"

BLUE_DARK = HexColor("#1e3a5f")
BLUE_MED = HexColor("#2563eb")
BLUE_LIGHT = HexColor("#bfdbfe")
BLUE_BG = HexColor("#eff6ff")
AMBER = HexColor("#d97706")
GRAY_LIGHT = HexColor("#e0e0e0")
GRAY_MED = HexColor("#999999")

CERTIFICATES = [
    {"title": "Certificado de Lectura Bíblica", "subtitle": "Por completar las historias bíblicas", "icon": "📖"},
    {"title": "Certificado de Buen Comportamiento", "subtitle": "Por ser un niño ejemplar", "icon": "⭐"},
    {"title": "Certificado de Memorización", "subtitle": "Por memorizar versículos bíblicos", "icon": "🧠"},
    {"title": "Certificado de Asistencia", "subtitle": "Por asistir fielmente a la escuela dominical", "icon": "🏆"},
    {"title": "Certificado de Servicio", "subtitle": "Por servir con amor a los demás", "icon": "❤️"},
    {"title": "Certificado de Oración", "subtitle": "Por ser un guerrero de oración", "icon": "🙏"},
    {"title": "Certificado de Amistad", "subtitle": "Por ser un buen amigo como Jesús", "icon": "🤝"},
    {"title": "Certificado de Valentía", "subtitle": "Por ser valiente como David", "icon": "🦁"},
    {"title": "Certificado de Gratitud", "subtitle": "Por tener un corazón agradecido", "icon": "🌟"},
    {"title": "Certificado de Graduación Bíblica", "subtitle": "Por completar el Mega Kit Bíblico", "icon": "🎓"},
]

BOOKMARKS = [
    {"verse": "Porque de tal manera amó Dios al mundo...", "ref": "Juan 3:16", "theme": "Amor"},
    {"verse": "Todo lo puedo en Cristo que me fortalece.", "ref": "Filipenses 4:13", "theme": "Fuerza"},
    {"verse": "El Señor es mi pastor, nada me faltará.", "ref": "Salmo 23:1", "theme": "Confianza"},
    {"verse": "Lámpara es a mis pies tu palabra.", "ref": "Salmo 119:105", "theme": "Sabiduría"},
    {"verse": "Confía en el Señor con todo tu corazón.", "ref": "Proverbios 3:5", "theme": "Fe"},
    {"verse": "No temas, porque yo estoy contigo.", "ref": "Isaías 41:10", "theme": "Protección"},
    {"verse": "Den gracias al Señor porque Él es bueno.", "ref": "Salmo 136:1", "theme": "Gratitud"},
    {"verse": "Yo soy el camino, la verdad y la vida.", "ref": "Juan 14:6", "theme": "Jesús"},
    {"verse": "Esfuérzate y sé valiente.", "ref": "Josué 1:9", "theme": "Valentía"},
    {"verse": "Ama a tu prójimo como a ti mismo.", "ref": "Marcos 12:31", "theme": "Amor"},
    {"verse": "Dios es nuestro refugio y fortaleza.", "ref": "Salmo 46:1", "theme": "Refugio"},
    {"verse": "En el principio creó Dios los cielos.", "ref": "Génesis 1:1", "theme": "Creación"},
    {"verse": "Los que esperan en el Señor renovarán sus fuerzas.", "ref": "Isaías 40:31", "theme": "Esperanza"},
    {"verse": "Instruye al niño en su camino.", "ref": "Proverbios 22:6", "theme": "Enseñanza"},
    {"verse": "Sean bondadosos unos con otros.", "ref": "Efesios 4:32", "theme": "Bondad"},
    {"verse": "El gozo del Señor es mi fortaleza.", "ref": "Nehemías 8:10", "theme": "Gozo"},
    {"verse": "Busquen primero el reino de Dios.", "ref": "Mateo 6:33", "theme": "Prioridades"},
    {"verse": "La paz les dejo, mi paz les doy.", "ref": "Juan 14:27", "theme": "Paz"},
    {"verse": "Hagan todo con amor.", "ref": "1 Corintios 16:14", "theme": "Amor"},
    {"verse": "Yo estaré con ustedes todos los días.", "ref": "Mateo 28:20", "theme": "Compañía"},
]

MONTHS = [
    ("ENERO", 31, "Amor — Juan 3:16"),
    ("FEBRERO", 28, "Fe — Hebreos 11:1"),
    ("MARZO", 31, "Esperanza — Romanos 15:13"),
    ("ABRIL", 30, "Gratitud — Salmo 136:1"),
    ("MAYO", 31, "Valentía — Josué 1:9"),
    ("JUNIO", 30, "Bondad — Efesios 4:32"),
    ("JULIO", 31, "Paciencia — Santiago 5:7"),
    ("AGOSTO", 31, "Gozo — Filipenses 4:4"),
    ("SEPTIEMBRE", 30, "Paz — Juan 14:27"),
    ("OCTUBRE", 31, "Sabiduría — Proverbios 3:5"),
    ("NOVIEMBRE", 30, "Servicio — Gálatas 5:13"),
    ("DICIEMBRE", 31, "Adoración — Salmo 95:6"),
]

DAYS_HEADER = ["LUN", "MAR", "MIÉ", "JUE", "VIE", "SÁB", "DOM"]


def draw_cover(c, w, h):
    c.setFillColor(BLUE_DARK)
    c.rect(0, 0, w, h, fill=1)

    c.setFillColor(AMBER)
    c.rect(0.5*inch, h - 1.2*inch, w - 1*inch, 2, fill=1)
    c.rect(0.5*inch, 1.2*inch, w - 1*inch, 2, fill=1)

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h - 1*inch, "MEGA KIT BÍBLICO INFANTIL")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(w/2, h/2 + 1.8*inch, "CERTIFICADOS")

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(w/2, h/2 + 1.1*inch, "MARCADORES")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(w/2, h/2 + 0.4*inch, "Y CALENDARIO")

    c.setFillColor(BLUE_LIGHT)
    c.setFont("Helvetica", 14)
    c.drawCentredString(w/2, h/2 - 0.4*inch, "10 Certificados · 20 Marcadores · 12 Meses")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h/2 - 1.1*inch, "¡Imprime, recorta y personaliza!")

    c.setFillColor(GRAY_LIGHT)
    c.setFont("Helvetica", 11)
    c.drawCentredString(w/2, 1.5*inch, "Para niños de 4 a 10 años")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(w/2, 0.8*inch, "www.kitbiblicoinfantil.com")


def draw_certificate(c, w, h, cert, page_num):
    c.setFillColor(white)
    c.rect(0, 0, w, h, fill=1)

    border_margin = 0.4*inch
    c.setStrokeColor(AMBER)
    c.setLineWidth(3)
    c.rect(border_margin, border_margin, w - 2*border_margin, h - 2*border_margin, fill=0, stroke=1)

    c.setStrokeColor(BLUE_MED)
    c.setLineWidth(1)
    c.rect(border_margin + 0.15*inch, border_margin + 0.15*inch,
           w - 2*(border_margin + 0.15*inch), h - 2*(border_margin + 0.15*inch), fill=0, stroke=1)

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 40)
    c.drawCentredString(w/2, h - 1.5*inch, cert["icon"])

    c.setFillColor(BLUE_DARK)
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(w/2, h - 2.2*inch, cert["title"])

    c.setFillColor(BLUE_MED)
    c.setFont("Helvetica", 12)
    c.drawCentredString(w/2, h - 2.6*inch, cert["subtitle"])

    c.setFillColor(AMBER)
    c.rect(w/2 - 2*inch, h - 2.9*inch, 4*inch, 1.5, fill=1)

    c.setFillColor(BLUE_DARK)
    c.setFont("Helvetica", 14)
    c.drawCentredString(w/2, h - 3.4*inch, "Se otorga a:")

    c.setStrokeColor(GRAY_LIGHT)
    c.setLineWidth(1)
    c.line(w/2 - 2.5*inch, h - 3.9*inch, w/2 + 2.5*inch, h - 3.9*inch)

    c.setFillColor(GRAY_MED)
    c.setFont("Helvetica", 9)
    c.drawCentredString(w/2, h - 4.1*inch, "(Escribe tu nombre aquí)")

    c.setFillColor(BLUE_DARK)
    c.setFont("Helvetica", 12)
    c.drawCentredString(w/2, h - 4.7*inch, "Por su dedicación y esfuerzo en el estudio de la Palabra de Dios.")

    c.setFillColor(BLUE_DARK)
    c.setFont("Helvetica", 11)
    c.drawCentredString(w/2, h - 5.6*inch, "Fecha: _____ / _____ / _____")

    sig_y = 2.0*inch
    c.setStrokeColor(GRAY_LIGHT)
    c.line(w/2 - 2*inch, sig_y, w/2 - 0.3*inch, sig_y)
    c.line(w/2 + 0.3*inch, sig_y, w/2 + 2*inch, sig_y)

    c.setFillColor(GRAY_MED)
    c.setFont("Helvetica", 8)
    c.drawCentredString(w/2 - 1.15*inch, sig_y - 0.15*inch, "Firma del Maestro/a")
    c.drawCentredString(w/2 + 1.15*inch, sig_y - 0.15*inch, "Firma del Pastor/a")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(w/2, 1.2*inch, "Mega Kit Bíblico Infantil")

    c.setFillColor(BLUE_MED)
    c.setFont("Helvetica", 8)
    c.drawCentredString(w/2, 0.9*inch, "\"Instruye al niño en su camino\" — Proverbios 22:6")


def draw_bookmarks_page(c, w, h, bookmarks_set, page_num):
    c.setFillColor(BLUE_BG)
    c.rect(0, 0, w, h, fill=1)

    c.setFillColor(BLUE_DARK)
    c.rect(0, h - 0.5*inch, w, 0.5*inch, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(w/2, h - 0.35*inch, f"MARCADORES BÍBLICOS — Recorta por la línea punteada")

    bm_width = 2.0*inch
    bm_height = 7.0*inch
    gap = 0.25*inch
    cols = len(bookmarks_set)
    total_w = cols * bm_width + (cols - 1) * gap
    start_x = (w - total_w) / 2
    start_y = (h - 0.5*inch - bm_height) / 2

    for idx, bm in enumerate(bookmarks_set):
        x = start_x + idx * (bm_width + gap)
        y = start_y

        c.setStrokeColor(GRAY_MED)
        c.setDash(3, 3)
        c.setLineWidth(0.5)
        c.rect(x, y, bm_width, bm_height, fill=0, stroke=1)
        c.setDash()

        inner_m = 0.1*inch
        ix = x + inner_m
        iy = y + inner_m
        iw = bm_width - 2*inner_m
        ih = bm_height - 2*inner_m

        c.setFillColor(white)
        c.roundRect(ix, iy, iw, ih, 8, fill=1, stroke=0)

        c.setStrokeColor(BLUE_MED)
        c.setLineWidth(1.5)
        c.roundRect(ix, iy, iw, ih, 8, fill=0, stroke=1)

        c.setFillColor(BLUE_DARK)
        c.roundRect(ix, iy + ih - 0.7*inch, iw, 0.7*inch, 8, fill=1, stroke=0)

        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(ix + iw/2, iy + ih - 0.35*inch, bm["theme"].upper())

        c.setFillColor(AMBER)
        c.rect(ix + 0.2*inch, iy + ih - 0.85*inch, iw - 0.4*inch, 1, fill=1)

        text_x = ix + 0.15*inch
        text_w = iw - 0.3*inch
        c.setFillColor(BLUE_DARK)
        c.setFont("Helvetica", 8)

        words = bm["verse"].split()
        lines = []
        line = ""
        for word in words:
            test = f"{line} {word}".strip()
            if c.stringWidth(test, "Helvetica", 8) <= text_w:
                line = test
            else:
                lines.append(line)
                line = word
        if line:
            lines.append(line)

        text_y = iy + ih - 1.2*inch
        for ln in lines:
            c.drawCentredString(ix + iw/2, text_y, ln)
            text_y -= 12

        c.setFillColor(AMBER)
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(ix + iw/2, text_y - 8, bm["ref"])

        c.setFillColor(BLUE_MED)
        c.setFont("Helvetica", 6)
        c.drawCentredString(ix + iw/2, iy + 0.15*inch, "Mega Kit Bíblico Infantil")

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w/2, 0.25*inch, "Mega Kit Bíblico Infantil — Marcadores Bíblicos")


def draw_calendar_page(c, w, h, month_name, days_in_month, theme_verse, page_num):
    c.setFillColor(BLUE_BG)
    c.rect(0, 0, w, h, fill=1)

    c.setFillColor(BLUE_DARK)
    c.rect(0, h - 0.9*inch, w, 0.9*inch, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(w/2, h - 0.55*inch, month_name)
    c.setFillColor(AMBER)
    c.setFont("Helvetica", 10)
    c.drawCentredString(w/2, h - 0.78*inch, theme_verse)

    margin = 0.6*inch
    grid_w = w - 2*margin
    cell_w = grid_w / 7
    header_y = h - 1.2*inch

    rows_needed = 0
    day = 1
    start_dow = 0
    temp_dow = start_dow
    temp_day = 1
    while temp_day <= days_in_month:
        if temp_dow == 0:
            rows_needed += 1
        temp_dow = (temp_dow + 1) % 7
        temp_day += 1
    if rows_needed == 0:
        rows_needed = 1

    available_h = header_y - 0.3*inch - 1.0*inch
    cell_h = min(available_h / (rows_needed + 1), 1.0*inch)

    c.setFillColor(BLUE_MED)
    c.rect(margin, header_y - cell_h, grid_w, cell_h, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 10)
    for i, day_name in enumerate(DAYS_HEADER):
        cx = margin + i * cell_w + cell_w / 2
        cy = header_y - cell_h / 2 - 4
        c.drawCentredString(cx, cy, day_name)

    day = 1
    dow = 0
    row = 0
    while day <= days_in_month:
        x = margin + dow * cell_w
        y = header_y - cell_h - row * cell_h

        c.setStrokeColor(BLUE_LIGHT)
        c.setLineWidth(0.5)
        c.setFillColor(white)
        c.rect(x, y - cell_h, cell_w, cell_h, fill=1, stroke=1)

        c.setFillColor(BLUE_DARK)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x + 4, y - 16, str(day))

        day += 1
        dow += 1
        if dow >= 7:
            dow = 0
            row += 1

    notes_y = 1.0*inch
    c.setFillColor(BLUE_DARK)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(margin, notes_y + 0.15*inch, "Notas / Versículo del mes:")
    c.setStrokeColor(GRAY_LIGHT)
    c.setLineWidth(0.5)
    for i in range(2):
        c.line(margin, notes_y - i * 0.2*inch, w - margin, notes_y - i * 0.2*inch)

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w/2, 0.35*inch, "Mega Kit Bíblico Infantil — Calendario Bíblico")


def main():
    w, h = letter
    c = canvas.Canvas(OUTPUT_PATH, pagesize=letter)

    draw_cover(c, w, h)
    c.showPage()

    print("  Generando certificados...")
    for i, cert in enumerate(CERTIFICATES):
        print(f"    Certificado {i+1}/10: {cert['title']}")
        draw_certificate(c, w, h, cert, i + 1)
        c.showPage()

    section_page = canvas.Canvas.__class__
    c.setFillColor(BLUE_DARK)
    c.rect(0, 0, w, h, fill=1)
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(w/2, h/2 + 0.5*inch, "MARCADORES")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(w/2, h/2 - 0.2*inch, "BÍBLICOS")
    c.setFillColor(BLUE_LIGHT)
    c.setFont("Helvetica", 14)
    c.drawCentredString(w/2, h/2 - 0.8*inch, "20 Marcadores para Recortar")
    c.showPage()

    print("  Generando marcadores...")
    bm_pages = []
    for i in range(0, len(BOOKMARKS), 3):
        bm_pages.append(BOOKMARKS[i:i+3])

    for i, bm_set in enumerate(bm_pages):
        print(f"    Página de marcadores {i+1}/{len(bm_pages)}")
        draw_bookmarks_page(c, w, h, bm_set, i + 1)
        c.showPage()

    c.setFillColor(BLUE_DARK)
    c.rect(0, 0, w, h, fill=1)
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(w/2, h/2 + 0.5*inch, "CALENDARIO")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(w/2, h/2 - 0.2*inch, "BÍBLICO")
    c.setFillColor(BLUE_LIGHT)
    c.setFont("Helvetica", 14)
    c.drawCentredString(w/2, h/2 - 0.8*inch, "12 Meses con Versículos para Memorizar")
    c.showPage()

    print("  Generando calendario...")
    for i, (month_name, days, theme) in enumerate(MONTHS):
        print(f"    Mes {i+1}/12: {month_name}")
        draw_calendar_page(c, w, h, month_name, days, theme, i + 1)
        c.showPage()

    c.save()
    print(f"\n PDF generado: {OUTPUT_PATH}")
    print(f" Total: {len(CERTIFICATES)} certificados, {len(BOOKMARKS)} marcadores, {len(MONTHS)} meses")


if __name__ == "__main__":
    main()
