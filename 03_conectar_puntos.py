import random
import math
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black

OUTPUT_PATH = r"C:\Users\hp\Documents\kit-biblico-infantil\03_Conectar_los_Puntos.pdf"

BLUE_DARK = HexColor("#1e3a5f")
BLUE_MED = HexColor("#2563eb")
BLUE_LIGHT = HexColor("#bfdbfe")
BLUE_BG = HexColor("#eff6ff")
AMBER = HexColor("#d97706")
GRAY_LIGHT = HexColor("#e0e0e0")
DOT_COLOR = HexColor("#2563eb")
NUM_COLOR = HexColor("#1e3a5f")


def star_points(cx, cy, outer_r, inner_r, n_points):
    pts = []
    for i in range(n_points * 2):
        angle = math.radians(90 + i * 360 / (n_points * 2))
        r = outer_r if i % 2 == 0 else inner_r
        pts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    return pts

def cross_points(cx, cy, size):
    s = size
    t = size * 0.35
    return [
        (cx - t, cy + s), (cx + t, cy + s),
        (cx + t, cy + t), (cx + s, cy + t),
        (cx + s, cy - t), (cx + t, cy - t),
        (cx + t, cy - s), (cx - t, cy - s),
        (cx - t, cy - t), (cx - s, cy - t),
        (cx - s, cy + t), (cx - t, cy + t),
    ]

def heart_points(cx, cy, size, n=30):
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        x = 16 * math.sin(t)**3
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        pts.append((cx + x * size / 17, cy + y * size / 17))
    return pts

def fish_points(cx, cy, size, n=30):
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        r = size * (1 + 0.3 * math.cos(2 * t))
        x = cx + r * math.cos(t) * 1.3
        y = cy + r * math.sin(t) * 0.6
        pts.append((x, y))
    return pts

def dove_points(cx, cy, size, n=25):
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        r = size * (1 + 0.4 * math.cos(t) + 0.15 * math.cos(3*t))
        pts.append((cx + r * math.cos(t), cy + r * math.sin(t) * 0.7))
    return pts

def house_points(cx, cy, size):
    s = size
    return [
        (cx - s, cy - s), (cx + s, cy - s),
        (cx + s, cy + s*0.3), (cx, cy + s),
        (cx - s, cy + s*0.3),
    ]

def boat_points(cx, cy, size):
    s = size
    return [
        (cx - s, cy), (cx - s*0.7, cy - s*0.5),
        (cx + s*0.7, cy - s*0.5), (cx + s, cy),
        (cx + s*0.3, cy), (cx + s*0.3, cy + s*0.8),
        (cx - s*0.3, cy + s*0.8), (cx - s*0.3, cy),
    ]

def crown_points(cx, cy, size):
    s = size
    return [
        (cx - s, cy - s*0.3), (cx - s, cy + s*0.2),
        (cx - s*0.5, cy), (cx, cy + s*0.5),
        (cx + s*0.5, cy), (cx + s, cy + s*0.2),
        (cx + s, cy - s*0.3),
    ]

def chalice_points(cx, cy, size, n=20):
    pts = []
    for i in range(n):
        t = math.pi * i / (n - 1)
        x = cx + size * 0.7 * math.cos(t)
        y = cy + size * 0.5 * math.sin(t)
        pts.append((x, y))
    pts.append((cx + size*0.15, cy - size*0.5))
    pts.append((cx + size*0.4, cy - size*0.7))
    pts.append((cx - size*0.4, cy - size*0.7))
    pts.append((cx - size*0.15, cy - size*0.5))
    return pts

def circle_points(cx, cy, size, n=20):
    return [(cx + size * math.cos(2*math.pi*i/n), cy + size * math.sin(2*math.pi*i/n)) for i in range(n)]

def triangle_points(cx, cy, size, n=15):
    vertices = [
        (cx, cy + size),
        (cx - size * 0.87, cy - size * 0.5),
        (cx + size * 0.87, cy - size * 0.5),
    ]
    pts = []
    per_side = n // 3
    for s in range(3):
        x1, y1 = vertices[s]
        x2, y2 = vertices[(s+1) % 3]
        for i in range(per_side):
            t = i / per_side
            pts.append((x1 + t*(x2-x1), y1 + t*(y2-y1)))
    return pts

def diamond_points(cx, cy, size):
    return [
        (cx, cy + size), (cx + size*0.6, cy),
        (cx, cy - size), (cx - size*0.6, cy),
    ]

def scroll_points(cx, cy, size, n=24):
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        rx = size * (0.4 + 0.15 * math.cos(2*t))
        ry = size * (1 + 0.1 * math.cos(2*t))
        pts.append((cx + rx * math.cos(t), cy + ry * math.sin(t) * 0.5))
    return pts


SHAPES = [
    {"title": "Estrella de Belén", "func": lambda cx, cy, s: star_points(cx, cy, s, s*0.4, 5), "n_points": 20},
    {"title": "La Cruz de Jesús", "func": lambda cx, cy, s: cross_points(cx, cy, s), "n_points": 12},
    {"title": "Corazón de Dios", "func": lambda cx, cy, s: heart_points(cx, cy, s, 25), "n_points": 25},
    {"title": "El Pez Cristiano", "func": lambda cx, cy, s: fish_points(cx, cy, s, 25), "n_points": 25},
    {"title": "La Paloma de Noé", "func": lambda cx, cy, s: dove_points(cx, cy, s, 25), "n_points": 25},
    {"title": "La Casa de Dios", "func": lambda cx, cy, s: house_points(cx, cy, s), "n_points": 5},
    {"title": "El Arca de Noé", "func": lambda cx, cy, s: boat_points(cx, cy, s), "n_points": 8},
    {"title": "Corona del Rey", "func": lambda cx, cy, s: crown_points(cx, cy, s), "n_points": 7},
    {"title": "El Cáliz Sagrado", "func": lambda cx, cy, s: chalice_points(cx, cy, s, 15), "n_points": 19},
    {"title": "Estrella Grande", "func": lambda cx, cy, s: star_points(cx, cy, s, s*0.5, 6), "n_points": 24},
    {"title": "El Sol de Justicia", "func": lambda cx, cy, s: circle_points(cx, cy, s, 20), "n_points": 20},
    {"title": "La Trinidad", "func": lambda cx, cy, s: triangle_points(cx, cy, s, 15), "n_points": 15},
    {"title": "La Piedra Preciosa", "func": lambda cx, cy, s: diamond_points(cx, cy, s), "n_points": 4},
    {"title": "El Pergamino Sagrado", "func": lambda cx, cy, s: scroll_points(cx, cy, s, 20), "n_points": 20},
    {"title": "Estrella de David", "func": lambda cx, cy, s: star_points(cx, cy, s, s*0.45, 6), "n_points": 24},
]

DOT_THEMES = []
bible_titles = [
    "La Creación — Estrella", "Noé — El Arca", "Moisés — Estrella de Esperanza",
    "David — Corona del Rey", "Daniel — Corazón Valiente", "Jonás — El Pez",
    "Jesús — La Cruz", "María — Corazón de Madre", "José — La Casa",
    "Los Magos — Estrella de Belén", "Pedro — La Barca", "Pablo — El Pergamino",
    "Abraham — Estrella de Promesa", "Rut — Corazón Fiel", "Ester — Corona Real",
    "Sansón — Estrella de Fuerza", "Elías — El Sol", "Eliseo — La Paloma",
    "Samuel — El Cáliz", "Isaías — El Pergamino", "Jeremías — Corazón de Profeta",
    "Ezequiel — Estrella del Cielo", "Josué — La Cruz de Victoria", "Gedeón — Estrella Guerrera",
    "Salomón — Corona de Sabiduría", "Nehemías — La Casa de Dios", "Job — Corazón de Paciencia",
    "Adán — La Estrella Primera", "Eva — Corazón del Edén", "Caín y Abel — El Triángulo",
    "La Torre de Babel — La Casa", "Jacob — La Piedra Preciosa", "Raquel — Estrella de Amor",
    "Rebeca — El Cáliz de Bondad", "Isaac — La Cruz de Fe", "Lot — La Paloma de Escape",
    "Sara — Corona de Madre", "Marta — La Casa de Servicio", "María Magdalena — El Corazón",
    "Lázaro — La Cruz de Vida", "Zaqueo — Estrella de Cambio", "Bartimeo — El Sol de Luz",
    "Timoteo — El Pergamino Joven", "Felipe — El Pez del Bautismo", "Andrés — La Barca",
    "Santiago — La Cruz del Apóstol", "Juan — Corazón del Amado", "Mateo — El Pergamino del Escriba",
    "Tomás — Estrella de Fe", "Bernabé — Corazón de Consuelo",
]

for i, title in enumerate(bible_titles):
    shape = SHAPES[i % len(SHAPES)]
    DOT_THEMES.append({"title": title, "shape_idx": i % len(SHAPES)})


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
    c.drawCentredString(w/2, h/2 + 1.5*inch, "CONECTAR LOS PUNTOS")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(w/2, h/2 + 0.7*inch, "BÍBLICOS")
    c.setFillColor(BLUE_LIGHT)
    c.setFont("Helvetica", 16)
    c.drawCentredString(w/2, h/2, "50 Figuras · Une los Puntos y Descubre")
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h/2 - 0.8*inch, "¡Conecta, descubre y colorea!")
    c.setFillColor(GRAY_LIGHT)
    c.setFont("Helvetica", 11)
    c.drawCentredString(w/2, 1.5*inch, "Para niños de 4 a 10 años")
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(w/2, 0.8*inch, "www.kitbiblicoinfantil.com")


def draw_dot_page(c, w, h, theme, page_num):
    c.setFillColor(BLUE_BG)
    c.rect(0, 0, w, h, fill=1)

    c.setFillColor(BLUE_DARK)
    c.rect(0, h - 0.7*inch, w, 0.7*inch, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h - 0.45*inch, f"✏️ {theme['title']}")

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 9)
    c.drawRightString(w - 0.4*inch, h - 0.45*inch, f"Página {page_num}")

    shape = SHAPES[theme["shape_idx"]]
    cx = w / 2
    cy = h / 2 - 0.2*inch
    size = 2.5 * inch

    points = shape["func"](cx, cy, size)

    for i, (x, y) in enumerate(points):
        c.setFillColor(DOT_COLOR)
        c.circle(x, y, 4, fill=1)

        c.setFillColor(NUM_COLOR)
        c.setFont("Helvetica-Bold", 10)
        offset_x = 10
        offset_y = 10
        angle = math.atan2(y - cy, x - cx)
        offset_x = 12 * math.cos(angle)
        offset_y = 12 * math.sin(angle)
        c.drawCentredString(x + offset_x, y + offset_y - 3, str(i + 1))

    c.setFillColor(BLUE_MED)
    c.setFont("Helvetica", 10)
    c.drawCentredString(w/2, 1.0*inch, "¡Une los puntos del 1 al " + str(len(points)) + " y descubre la figura!")
    c.setFont("Helvetica", 9)
    c.drawCentredString(w/2, 0.7*inch, "Después puedes colorearla con tus colores favoritos")

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w/2, 0.35*inch, "Mega Kit Bíblico Infantil — Conectar los Puntos")


def main():
    w, h = letter
    c = canvas.Canvas(OUTPUT_PATH, pagesize=letter)

    draw_cover(c, w, h)
    c.showPage()

    for i, theme in enumerate(DOT_THEMES):
        print(f"  Generando puntos {i+1}/50: {theme['title']}")
        draw_dot_page(c, w, h, theme, i + 1)
        c.showPage()

    c.save()
    print(f"\n PDF generado: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
