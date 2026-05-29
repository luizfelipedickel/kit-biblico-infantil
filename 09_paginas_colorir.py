import math
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black

OUTPUT_PATH = r"C:\Users\hp\Documents\kit-biblico-infantil\09_Paginas_para_Colorear.pdf"

BLUE_DARK = HexColor("#1e3a5f")
BLUE_MED = HexColor("#2563eb")
BLUE_LIGHT = HexColor("#bfdbfe")
BLUE_BG = HexColor("#eff6ff")
AMBER = HexColor("#d97706")
GRAY_LIGHT = HexColor("#e0e0e0")
LINE_COLOR = HexColor("#333333")

SCENES = [
    {"title": "Noé Construyendo el Arca", "category": "Antiguo Testamento"},
    {"title": "David contra Goliat", "category": "Antiguo Testamento"},
    {"title": "Jonás y la Ballena", "category": "Antiguo Testamento"},
    {"title": "Moisés y el Mar Rojo", "category": "Antiguo Testamento"},
    {"title": "El Nacimiento de Jesús", "category": "Nuevo Testamento"},
    {"title": "Daniel y los Leones", "category": "Antiguo Testamento"},
    {"title": "Adán y Eva en el Edén", "category": "Antiguo Testamento"},
    {"title": "La Torre de Babel", "category": "Antiguo Testamento"},
    {"title": "Abraham y las Estrellas", "category": "Antiguo Testamento"},
    {"title": "José y su Túnica de Colores", "category": "Antiguo Testamento"},
    {"title": "Moisés y la Zarza Ardiente", "category": "Antiguo Testamento"},
    {"title": "Los Israelitas Cruzando el Mar", "category": "Antiguo Testamento"},
    {"title": "Jesús Calma la Tormenta", "category": "Nuevo Testamento"},
    {"title": "Los Panes y los Peces", "category": "Nuevo Testamento"},
    {"title": "El Buen Samaritano", "category": "Nuevo Testamento"},
    {"title": "Zaqueo en el Árbol", "category": "Nuevo Testamento"},
    {"title": "Jesús con los Niños", "category": "Nuevo Testamento"},
    {"title": "Los Reyes Magos", "category": "Nuevo Testamento"},
    {"title": "El Arca de Noé con Arcoíris", "category": "Antiguo Testamento"},
    {"title": "Sansón el Fuerte", "category": "Antiguo Testamento"},
    {"title": "Ester ante el Rey", "category": "Antiguo Testamento"},
    {"title": "Rut en el Campo de Trigo", "category": "Antiguo Testamento"},
    {"title": "Elías y el Carro de Fuego", "category": "Antiguo Testamento"},
    {"title": "La Oveja Perdida", "category": "Nuevo Testamento"},
    {"title": "Pedro Pescando con Jesús", "category": "Nuevo Testamento"},
    {"title": "Pablo Predicando", "category": "Nuevo Testamento"},
    {"title": "La Última Cena", "category": "Nuevo Testamento"},
    {"title": "Jesús Resucitado", "category": "Nuevo Testamento"},
    {"title": "Los Pastores de Belén", "category": "Nuevo Testamento"},
    {"title": "María y el Ángel Gabriel", "category": "Nuevo Testamento"},
    {"title": "El Hijo Pródigo", "category": "Nuevo Testamento"},
    {"title": "La Paloma de Noé", "category": "Antiguo Testamento"},
    {"title": "Salomón el Rey Sabio", "category": "Antiguo Testamento"},
    {"title": "Gedeón y las Antorchas", "category": "Antiguo Testamento"},
    {"title": "Samuel en el Templo", "category": "Antiguo Testamento"},
    {"title": "Nehemías y el Muro", "category": "Antiguo Testamento"},
    {"title": "Jesús Bautizado en el Jordán", "category": "Nuevo Testamento"},
    {"title": "Jacob y la Escalera al Cielo", "category": "Antiguo Testamento"},
    {"title": "Rebeca en el Pozo", "category": "Antiguo Testamento"},
    {"title": "Josué en Jericó", "category": "Antiguo Testamento"},
    {"title": "Débora la Jueza", "category": "Antiguo Testamento"},
    {"title": "Timoteo Estudiando", "category": "Nuevo Testamento"},
    # Versiculos decorados
    {"title": "Dios es Amor — 1 Juan 4:8", "category": "Versículo Decorado"},
    {"title": "Todo lo Puedo en Cristo — Fil. 4:13", "category": "Versículo Decorado"},
    {"title": "El Señor es mi Pastor — Salmo 23:1", "category": "Versículo Decorado"},
    {"title": "No Temas, Yo Estoy Contigo — Is. 41:10", "category": "Versículo Decorado"},
    # Mandalas
    {"title": "Mandala de la Creación", "category": "Mandala Bíblico"},
    {"title": "Mandala del Arca de Noé", "category": "Mandala Bíblico"},
    {"title": "Mandala de Navidad", "category": "Mandala Bíblico"},
    {"title": "Mandala de la Cruz", "category": "Mandala Bíblico"},
]


def draw_scene_elements(c, cx, cy, area_w, area_h, scene_idx):
    """Draw line-art coloring scene based on the scene index"""
    c.setStrokeColor(LINE_COLOR)
    c.setLineWidth(1.8)
    c.setFillColor(white)

    if scene_idx % 50 == 0:  # Noé y el Arca
        # Boat
        bx, by = cx - 2*inch, cy - 1*inch
        path = c.beginPath()
        path.moveTo(bx, by + 0.8*inch)
        path.lineTo(bx + 0.3*inch, by)
        path.lineTo(bx + 3.7*inch, by)
        path.lineTo(bx + 4*inch, by + 0.8*inch)
        path.close()
        c.drawPath(path, fill=0, stroke=1)
        # Cabin
        c.rect(bx + 0.5*inch, by + 0.8*inch, 3*inch, 1.5*inch, fill=0, stroke=1)
        c.rect(bx + 0.8*inch, by + 1.0*inch, 0.6*inch, 0.5*inch, fill=0, stroke=1)
        c.rect(bx + 1.8*inch, by + 1.0*inch, 0.6*inch, 0.5*inch, fill=0, stroke=1)
        c.rect(bx + 2.8*inch, by + 1.0*inch, 0.6*inch, 0.5*inch, fill=0, stroke=1)
        # Roof
        path = c.beginPath()
        path.moveTo(bx + 0.3*inch, by + 2.3*inch)
        path.lineTo(bx + 2*inch, by + 3*inch)
        path.lineTo(bx + 3.7*inch, by + 2.3*inch)
        c.drawPath(path, fill=0, stroke=1)
        # Water waves
        for i in range(8):
            wx = bx - 0.5*inch + i * 0.6*inch
            path = c.beginPath()
            path.moveTo(wx, by - 0.3*inch)
            path.curveTo(wx + 0.15*inch, by - 0.1*inch, wx + 0.3*inch, by - 0.5*inch, wx + 0.45*inch, by - 0.3*inch)
            c.drawPath(path, fill=0, stroke=1)
        # Animals peeking
        # Giraffe neck
        c.rect(bx + 3.2*inch, by + 2.3*inch, 0.15*inch, 0.8*inch, fill=0, stroke=1)
        c.circle(bx + 3.27*inch, by + 3.2*inch, 0.12*inch, fill=0, stroke=1)
        # Elephant trunk
        path = c.beginPath()
        path.moveTo(bx + 0.5*inch, by + 2.3*inch)
        path.curveTo(bx + 0.3*inch, by + 2.8*inch, bx + 0.6*inch, by + 2.9*inch, bx + 0.5*inch, by + 2.5*inch)
        c.drawPath(path, fill=0, stroke=1)

    elif scene_idx % 50 == 1:  # David contra Goliat
        # David (small)
        dx, dy = cx - 1.5*inch, cy - 0.5*inch
        c.circle(dx, dy + 1.2*inch, 0.3*inch, fill=0, stroke=1)  # head
        c.line(dx, dy + 0.9*inch, dx, dy + 0.2*inch)  # body
        c.line(dx, dy + 0.7*inch, dx - 0.3*inch, dy + 0.4*inch)  # arm back
        c.line(dx, dy + 0.7*inch, dx + 0.4*inch, dy + 0.9*inch)  # arm sling
        c.circle(dx + 0.5*inch, dy + 0.95*inch, 0.08*inch, fill=0, stroke=1)  # stone
        c.line(dx, dy + 0.2*inch, dx - 0.2*inch, dy - 0.3*inch)  # legs
        c.line(dx, dy + 0.2*inch, dx + 0.2*inch, dy - 0.3*inch)
        # Goliat (big)
        gx, gy = cx + 1.2*inch, cy - 1*inch
        c.circle(gx, gy + 2.8*inch, 0.5*inch, fill=0, stroke=1)  # head
        c.line(gx, gy + 2.3*inch, gx, gy + 0.5*inch)  # body
        c.setLineWidth(2.5)
        c.line(gx, gy + 1.8*inch, gx - 0.5*inch, gy + 1.2*inch)
        c.line(gx, gy + 1.8*inch, gx + 0.5*inch, gy + 1.2*inch)
        c.line(gx, gy + 0.5*inch, gx - 0.3*inch, gy - 0.3*inch)
        c.line(gx, gy + 0.5*inch, gx + 0.3*inch, gy - 0.3*inch)
        c.setLineWidth(1.8)
        # Shield
        c.ellipse(gx + 0.5*inch, gy + 1.0*inch, gx + 1.0*inch, gy + 1.8*inch, fill=0, stroke=1)
        # Spear
        c.line(gx - 0.6*inch, gy + 1.0*inch, gx - 0.6*inch, gy + 3.2*inch)

    elif scene_idx % 50 == 2:  # Jonás y la Ballena
        # Whale
        wx, wy = cx, cy - 0.5*inch
        path = c.beginPath()
        path.moveTo(wx - 2.5*inch, wy)
        path.curveTo(wx - 2.5*inch, wy + 2*inch, wx + 1.5*inch, wy + 2*inch, wx + 2*inch, wy + 0.5*inch)
        path.curveTo(wx + 2.5*inch, wy - 0.2*inch, wx + 2*inch, wy - 1*inch, wx + 1.5*inch, wy - 0.8*inch)
        path.curveTo(wx, wy - 1.5*inch, wx - 2*inch, wy - 1*inch, wx - 2.5*inch, wy)
        c.drawPath(path, fill=0, stroke=1)
        # Eye
        c.circle(wx + 1.2*inch, wy + 0.5*inch, 0.15*inch, fill=0, stroke=1)
        c.circle(wx + 1.25*inch, wy + 0.53*inch, 0.05*inch, fill=1, stroke=0)
        # Mouth
        c.line(wx - 1*inch, wy - 0.2*inch, wx + 0.5*inch, wy - 0.2*inch)
        # Jonás inside (small figure)
        jx = wx - 0.3*inch
        jy = wy - 0.1*inch
        c.circle(jx, jy + 0.3*inch, 0.12*inch, fill=0, stroke=1)
        c.line(jx, jy + 0.18*inch, jx, jy - 0.15*inch)
        c.line(jx, jy + 0.1*inch, jx - 0.15*inch, jy)
        c.line(jx, jy + 0.1*inch, jx + 0.15*inch, jy + 0.2*inch)
        # Water
        for i in range(10):
            wwx = cx - 3*inch + i * 0.7*inch
            path = c.beginPath()
            path.moveTo(wwx, wy - 1.5*inch)
            path.curveTo(wwx + 0.15*inch, wy - 1.3*inch, wwx + 0.25*inch, wy - 1.7*inch, wwx + 0.4*inch, wy - 1.5*inch)
            c.drawPath(path, fill=0, stroke=1)
        # Tail
        path = c.beginPath()
        path.moveTo(wx - 2.5*inch, wy)
        path.curveTo(wx - 3*inch, wy + 0.5*inch, wx - 3.2*inch, wy + 0.8*inch, wx - 2.8*inch, wy + 1*inch)
        c.drawPath(path, fill=0, stroke=1)
        path = c.beginPath()
        path.moveTo(wx - 2.5*inch, wy)
        path.curveTo(wx - 3*inch, wy - 0.5*inch, wx - 3.2*inch, wy - 0.8*inch, wx - 2.8*inch, wy - 1*inch)
        c.drawPath(path, fill=0, stroke=1)

    elif scene_idx % 50 == 4:  # Nacimiento de Jesús
        # Stable roof
        path = c.beginPath()
        path.moveTo(cx - 2.5*inch, cy + 0.5*inch)
        path.lineTo(cx, cy + 2*inch)
        path.lineTo(cx + 2.5*inch, cy + 0.5*inch)
        c.drawPath(path, fill=0, stroke=1)
        # Manger
        c.rect(cx - 0.5*inch, cy - 0.8*inch, 1*inch, 0.6*inch, fill=0, stroke=1)
        # Baby
        c.ellipse(cx - 0.3*inch, cy - 0.6*inch, cx + 0.3*inch, cy - 0.3*inch, fill=0, stroke=1)
        # Star
        star_x, star_y = cx, cy + 1.8*inch
        for i in range(5):
            angle1 = math.radians(90 + i * 72)
            angle2 = math.radians(90 + i * 72 + 36)
            x1 = star_x + 0.25*inch * math.cos(angle1)
            y1 = star_y + 0.25*inch * math.sin(angle1)
            x2 = star_x + 0.12*inch * math.cos(angle2)
            y2 = star_y + 0.12*inch * math.sin(angle2)
            angle3 = math.radians(90 + (i+1) * 72)
            x3 = star_x + 0.25*inch * math.cos(angle3)
            y3 = star_y + 0.25*inch * math.sin(angle3)
            c.line(x1, y1, x2, y2)
            c.line(x2, y2, x3, y3)
        # Mary
        mx, my = cx - 1*inch, cy - 0.3*inch
        c.circle(mx, my + 0.8*inch, 0.2*inch, fill=0, stroke=1)
        c.line(mx, my + 0.6*inch, mx, my)
        path = c.beginPath()
        path.moveTo(mx - 0.3*inch, my + 0.9*inch)
        path.curveTo(mx - 0.4*inch, my + 1.2*inch, mx + 0.4*inch, my + 1.2*inch, mx + 0.3*inch, my + 0.9*inch)
        c.drawPath(path, fill=0, stroke=1)
        # Joseph
        jx, jy = cx + 1*inch, cy - 0.3*inch
        c.circle(jx, jy + 0.8*inch, 0.2*inch, fill=0, stroke=1)
        c.line(jx, jy + 0.6*inch, jx, jy)
        c.line(jx + 0.15*inch, jy, jx + 0.15*inch, jy + 1.2*inch)  # staff
        # Animals
        # Donkey
        c.ellipse(cx + 1.8*inch, cy - 0.6*inch, cx + 2.3*inch, cy - 0.2*inch, fill=0, stroke=1)
        c.circle(cx + 2.4*inch, cy - 0.1*inch, 0.1*inch, fill=0, stroke=1)

    else:
        # Generic scene with decorative border and large central figure
        # Decorative border
        margin = 0.8*inch
        c.setLineWidth(1.2)
        c.roundRect(margin, cy - area_h/2 + 0.3*inch, area_w - 0.2*inch, area_h - 0.4*inch, 15, fill=0, stroke=1)

        # Draw a cross in center
        cross_cx = cx
        cross_cy = cy + 0.3*inch
        cross_h = 1.8*inch
        cross_w = 1.2*inch
        bar_thick = 0.25*inch

        # Vertical bar
        c.rect(cross_cx - bar_thick/2, cross_cy - cross_h/2, bar_thick, cross_h, fill=0, stroke=1)
        # Horizontal bar
        c.rect(cross_cx - cross_w/2, cross_cy + cross_h*0.1, cross_w, bar_thick, fill=0, stroke=1)

        # Decorative elements around
        for i in range(8):
            angle = math.radians(i * 45)
            r = 2.2*inch
            sx = cross_cx + r * math.cos(angle)
            sy = cross_cy + r * math.sin(angle)

            if i % 3 == 0:
                # Star
                for j in range(5):
                    a1 = math.radians(90 + j * 72)
                    a2 = math.radians(90 + j * 72 + 36)
                    x1 = sx + 0.15*inch * math.cos(a1)
                    y1 = sy + 0.15*inch * math.sin(a1)
                    x2 = sx + 0.07*inch * math.cos(a2)
                    y2 = sy + 0.07*inch * math.sin(a2)
                    c.line(x1, y1, x2, y2)
                    a3 = math.radians(90 + (j+1) * 72)
                    x3 = sx + 0.15*inch * math.cos(a3)
                    y3 = sy + 0.15*inch * math.sin(a3)
                    c.line(x2, y2, x3, y3)
            elif i % 3 == 1:
                # Heart
                c.circle(sx - 0.06*inch, sy + 0.04*inch, 0.06*inch, fill=0, stroke=1)
                c.circle(sx + 0.06*inch, sy + 0.04*inch, 0.06*inch, fill=0, stroke=1)
                path = c.beginPath()
                path.moveTo(sx - 0.12*inch, sy + 0.02*inch)
                path.lineTo(sx, sy - 0.12*inch)
                path.lineTo(sx + 0.12*inch, sy + 0.02*inch)
                c.drawPath(path, fill=0, stroke=1)
            else:
                # Flower
                for j in range(5):
                    a = math.radians(j * 72)
                    px = sx + 0.08*inch * math.cos(a)
                    py = sy + 0.08*inch * math.sin(a)
                    c.circle(px, py, 0.04*inch, fill=0, stroke=1)
                c.circle(sx, sy, 0.03*inch, fill=0, stroke=1)

        # Scene title in decorative banner
        c.setLineWidth(1.5)
        banner_y = cy - area_h/2 + 0.5*inch
        c.roundRect(cx - 1.5*inch, banner_y, 3*inch, 0.35*inch, 5, fill=0, stroke=1)


def draw_coloring_page(c, w, h, scene, page_num):
    c.setFillColor(white)
    c.rect(0, 0, w, h, fill=1)

    # Header
    c.setFillColor(BLUE_DARK)
    c.rect(0, h - 0.55*inch, w, 0.55*inch, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(w/2, h - 0.37*inch, f"¡COLOREA! — {scene['title']}")
    c.setFillColor(AMBER)
    c.setFont("Helvetica", 8)
    c.drawRightString(w - 0.4*inch, h - 0.37*inch, f"{page_num}/50")
    c.drawString(0.4*inch, h - 0.37*inch, scene["category"])

    # Drawing area
    area_x = 0.5*inch
    area_y = 0.8*inch
    area_w = w - 1*inch
    area_h = h - 1.6*inch
    cx = w / 2
    cy = area_y + area_h / 2

    # Thin decorative border
    c.setStrokeColor(GRAY_LIGHT)
    c.setLineWidth(0.5)
    c.rect(area_x, area_y, area_w, area_h, fill=0, stroke=1)

    # Scene art
    draw_scene_elements(c, cx, cy, area_w, area_h, page_num - 1)

    # Footer
    c.setFillColor(AMBER)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w/2, 0.45*inch, "Mega Kit Bíblico Infantil — Páginas para Colorear")
    c.setFillColor(BLUE_MED)
    c.setFont("Helvetica", 8)
    c.drawCentredString(w/2, 0.6*inch, "¡Usa tus colores favoritos!")


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
    c.setFont("Helvetica-Bold", 32)
    c.drawCentredString(w/2, h/2 + 1.8*inch, "PÁGINAS PARA")

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 32)
    c.drawCentredString(w/2, h/2 + 1.1*inch, "COLOREAR")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(w/2, h/2 + 0.4*inch, "BÍBLICAS")

    c.setFillColor(BLUE_LIGHT)
    c.setFont("Helvetica", 16)
    c.drawCentredString(w/2, h/2 - 0.3*inch, "50 Dibujos · Escenas, Versículos y Mandalas")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h/2 - 1.0*inch, "¡Colorea la Biblia!")

    c.setFillColor(GRAY_LIGHT)
    c.setFont("Helvetica", 11)
    c.drawCentredString(w/2, 1.5*inch, "Para niños de 4 a 10 años")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(w/2, 0.8*inch, "www.kitbiblicoinfantil.com")


def main():
    w, h = letter
    c = canvas.Canvas(OUTPUT_PATH, pagesize=letter)

    draw_cover(c, w, h)
    c.showPage()

    for i, scene in enumerate(SCENES):
        print(f"  Colorear {i+1}/50: {scene['title']}")
        draw_coloring_page(c, w, h, scene, i + 1)
        c.showPage()

    c.save()
    print(f"\n PDF generado: {OUTPUT_PATH}")
    print(f" Total: {len(SCENES)} páginas para colorear")


if __name__ == "__main__":
    main()
