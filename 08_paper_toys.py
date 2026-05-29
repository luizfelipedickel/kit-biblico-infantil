import math
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, cm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black, Color

OUTPUT_PATH = r"C:\Users\hp\Documents\kit-biblico-infantil\08_Paper_Toys_Biblicos.pdf"

BLUE_DARK = HexColor("#1e3a5f")
BLUE_MED = HexColor("#2563eb")
BLUE_LIGHT = HexColor("#bfdbfe")
BLUE_BG = HexColor("#eff6ff")
AMBER = HexColor("#d97706")
GRAY_LIGHT = HexColor("#e0e0e0")

# ─── Character definitions ───
# Each character: name, skin, hair, eye, tunic_main, tunic_accent, detail_text, accessories
CHARACTERS = [
    {
        "name": "JESÚS",
        "skin": "#F4C7A0", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#FFFFFF", "tunic2": "#E8E0D0", "belt": "#8B7355",
        "detail": "Túnica blanca, sandalias",
        "category": "Personaje Principal"
    },
    {
        "name": "MARÍA",
        "skin": "#F4C7A0", "hair": "#3B2F2F", "eye": "#3B2F2F",
        "tunic": "#4169E1", "tunic2": "#87CEEB", "belt": "#1E3A5F",
        "detail": "Manto azul",
        "category": "Personaje Principal"
    },
    {
        "name": "JOSÉ",
        "skin": "#D2A77B", "hair": "#3B2F2F", "eye": "#3B2F2F",
        "tunic": "#8B6914", "tunic2": "#DAA520", "belt": "#5C3317",
        "detail": "Túnica marrón, carpintero",
        "category": "Personaje Principal"
    },
    {
        "name": "NOÉ",
        "skin": "#D2A77B", "hair": "#CCCCCC", "eye": "#3B2F2F",
        "tunic": "#2E8B57", "tunic2": "#3CB371", "belt": "#8B4513",
        "detail": "Barba blanca, bastón",
        "category": "Antiguo Testamento"
    },
    {
        "name": "MOISÉS",
        "skin": "#D2A77B", "hair": "#AAAAAA", "eye": "#3B2F2F",
        "tunic": "#8B0000", "tunic2": "#CD5C5C", "belt": "#DAA520",
        "detail": "Tablas de la Ley",
        "category": "Antiguo Testamento"
    },
    {
        "name": "DAVID",
        "skin": "#F4C7A0", "hair": "#B8530A", "eye": "#3B2F2F",
        "tunic": "#DEB887", "tunic2": "#D2B48C", "belt": "#8B4513",
        "detail": "Niño pastor, honda",
        "category": "Antiguo Testamento"
    },
    {
        "name": "ABRAHAM",
        "skin": "#D2A77B", "hair": "#CCCCCC", "eye": "#3B2F2F",
        "tunic": "#704214", "tunic2": "#A0522D", "belt": "#5C3317",
        "detail": "Túnica, barba larga",
        "category": "Antiguo Testamento"
    },
    {
        "name": "EVA",
        "skin": "#F4C7A0", "hair": "#8B4513", "eye": "#3B2F2F",
        "tunic": "#228B22", "tunic2": "#32CD32", "belt": "#006400",
        "detail": "Vestido de hojas verdes",
        "category": "Antiguo Testamento"
    },
    {
        "name": "DANIEL",
        "skin": "#D2A77B", "hair": "#3B2F2F", "eye": "#3B2F2F",
        "tunic": "#4B0082", "tunic2": "#6A5ACD", "belt": "#DAA520",
        "detail": "Túnica, leones",
        "category": "Antiguo Testamento"
    },
    {
        "name": "JONÁS",
        "skin": "#F4C7A0", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#2F4F4F", "tunic2": "#5F9EA0", "belt": "#8B7355",
        "detail": "Túnica, ballena",
        "category": "Antiguo Testamento"
    },
    {
        "name": "SANSÓN",
        "skin": "#D2A77B", "hair": "#1C1C1C", "eye": "#3B2F2F",
        "tunic": "#B8860B", "tunic2": "#DAA520", "belt": "#8B4513",
        "detail": "Cabello largo, fuerte",
        "category": "Antiguo Testamento"
    },
    {
        "name": "RUT",
        "skin": "#D2A77B", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#DB7093", "tunic2": "#FFB6C1", "belt": "#C71585",
        "detail": "Espigas de trigo",
        "category": "Antiguo Testamento"
    },
    {
        "name": "ESTER",
        "skin": "#F4C7A0", "hair": "#1C1C1C", "eye": "#3B2F2F",
        "tunic": "#800080", "tunic2": "#DA70D6", "belt": "#DAA520",
        "detail": "Corona de reina",
        "category": "Antiguo Testamento"
    },
    {
        "name": "SALOMÓN",
        "skin": "#D2A77B", "hair": "#3B2F2F", "eye": "#3B2F2F",
        "tunic": "#DAA520", "tunic2": "#FFD700", "belt": "#B8860B",
        "detail": "Corona dorada, rey sabio",
        "category": "Antiguo Testamento"
    },
    {
        "name": "ELÍAS",
        "skin": "#D2A77B", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#8B4513", "tunic2": "#A0522D", "belt": "#704214",
        "detail": "Manto de profeta",
        "category": "Antiguo Testamento"
    },
    {
        "name": "SAMUEL",
        "skin": "#F4C7A0", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#F5F5DC", "tunic2": "#FFFACD", "belt": "#B8860B",
        "detail": "Niño, túnica del templo",
        "category": "Antiguo Testamento"
    },
    {
        "name": "PEDRO",
        "skin": "#D2A77B", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#4682B4", "tunic2": "#87CEEB", "belt": "#2F4F4F",
        "detail": "Pescador, red de pesca",
        "category": "Nuevo Testamento"
    },
    {
        "name": "PABLO",
        "skin": "#D2A77B", "hair": "#3B2F2F", "eye": "#3B2F2F",
        "tunic": "#696969", "tunic2": "#A9A9A9", "belt": "#4B0082",
        "detail": "Pergamino en mano",
        "category": "Nuevo Testamento"
    },
    {
        "name": "ZAQUEO",
        "skin": "#F4C7A0", "hair": "#3B2F2F", "eye": "#3B2F2F",
        "tunic": "#006400", "tunic2": "#228B22", "belt": "#DAA520",
        "detail": "Bajito, bolsa de monedas",
        "category": "Nuevo Testamento"
    },
    {
        "name": "MARÍA MAGDALENA",
        "skin": "#F4C7A0", "hair": "#8B0000", "eye": "#3B2F2F",
        "tunic": "#C71585", "tunic2": "#FF69B4", "belt": "#8B008B",
        "detail": "Frasco de perfume",
        "category": "Nuevo Testamento"
    },
    {
        "name": "ÁNGEL GABRIEL",
        "skin": "#FFE4C4", "hair": "#DAA520", "eye": "#4169E1",
        "tunic": "#FFFFF0", "tunic2": "#FFD700", "belt": "#FFD700",
        "detail": "Alas blancas, aureola",
        "category": "Celestial"
    },
    {
        "name": "PASTOR DE BELÉN",
        "skin": "#D2A77B", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#D2B48C", "tunic2": "#C4A882", "belt": "#8B4513",
        "detail": "Ovejita en brazos",
        "category": "Nuevo Testamento"
    },
    {
        "name": "REY MAGO MELCHOR",
        "skin": "#D2A77B", "hair": "#CCCCCC", "eye": "#3B2F2F",
        "tunic": "#8B0000", "tunic2": "#DC143C", "belt": "#DAA520",
        "detail": "Corona, cofre de oro",
        "category": "Nuevo Testamento"
    },
    {
        "name": "REY MAGO GASPAR",
        "skin": "#F4C7A0", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#006400", "tunic2": "#228B22", "belt": "#DAA520",
        "detail": "Turbante, incienso",
        "category": "Nuevo Testamento"
    },
    {
        "name": "REY MAGO BALTASAR",
        "skin": "#8B5E3C", "hair": "#1C1C1C", "eye": "#3B2F2F",
        "tunic": "#4B0082", "tunic2": "#8A2BE2", "belt": "#DAA520",
        "detail": "Capa púrpura, mirra",
        "category": "Nuevo Testamento"
    },
    {
        "name": "GOLIAT",
        "skin": "#D2A77B", "hair": "#1C1C1C", "eye": "#3B2F2F",
        "tunic": "#696969", "tunic2": "#808080", "belt": "#2F4F4F",
        "detail": "Gigante, armadura",
        "category": "Antiguo Testamento"
    },
    {
        "name": "REBECA",
        "skin": "#F4C7A0", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#DA70D6", "tunic2": "#EE82EE", "belt": "#8B008B",
        "detail": "Cántaro de agua",
        "category": "Antiguo Testamento"
    },
    {
        "name": "ISAAC",
        "skin": "#F4C7A0", "hair": "#8B4513", "eye": "#3B2F2F",
        "tunic": "#F5DEB3", "tunic2": "#DEB887", "belt": "#8B7355",
        "detail": "Niño, leña",
        "category": "Antiguo Testamento"
    },
    {
        "name": "JACOB",
        "skin": "#D2A77B", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#B22222", "tunic2": "#CD5C5C", "belt": "#8B4513",
        "detail": "Túnica de colores",
        "category": "Antiguo Testamento"
    },
    {
        "name": "JOSUÉ",
        "skin": "#D2A77B", "hair": "#3B2F2F", "eye": "#3B2F2F",
        "tunic": "#8B4513", "tunic2": "#A0522D", "belt": "#696969",
        "detail": "Espada, casco guerrero",
        "category": "Antiguo Testamento"
    },
    {
        "name": "GEDEÓN",
        "skin": "#D2A77B", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#B8860B", "tunic2": "#CD853F", "belt": "#8B4513",
        "detail": "Antorcha y trompeta",
        "category": "Antiguo Testamento"
    },
    {
        "name": "DÉBORA",
        "skin": "#D2A77B", "hair": "#1C1C1C", "eye": "#3B2F2F",
        "tunic": "#8B008B", "tunic2": "#BA55D3", "belt": "#DAA520",
        "detail": "Jueza, palmera",
        "category": "Antiguo Testamento"
    },
    {
        "name": "ADÁN",
        "skin": "#D2A77B", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#228B22", "tunic2": "#32CD32", "belt": "#006400",
        "detail": "Hojas verdes, jardín",
        "category": "Antiguo Testamento"
    },
    {
        "name": "SARA",
        "skin": "#F4C7A0", "hair": "#CCCCCC", "eye": "#3B2F2F",
        "tunic": "#DDA0DD", "tunic2": "#EE82EE", "belt": "#8B008B",
        "detail": "Anciana sonriente",
        "category": "Antiguo Testamento"
    },
    {
        "name": "NEHEMÍAS",
        "skin": "#D2A77B", "hair": "#3B2F2F", "eye": "#3B2F2F",
        "tunic": "#A0522D", "tunic2": "#CD853F", "belt": "#696969",
        "detail": "Constructor, ladrillos",
        "category": "Antiguo Testamento"
    },
    {
        "name": "JOB",
        "skin": "#D2A77B", "hair": "#8B7355", "eye": "#3B2F2F",
        "tunic": "#808080", "tunic2": "#A9A9A9", "belt": "#696969",
        "detail": "Paciente, sentado",
        "category": "Antiguo Testamento"
    },
    {
        "name": "TIMOTEO",
        "skin": "#F4C7A0", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#4682B4", "tunic2": "#87CEEB", "belt": "#2F4F4F",
        "detail": "Joven, pergamino",
        "category": "Nuevo Testamento"
    },
    {
        "name": "RAQUEL",
        "skin": "#F4C7A0", "hair": "#8B4513", "eye": "#3B2F2F",
        "tunic": "#FF6347", "tunic2": "#FA8072", "belt": "#CD5C5C",
        "detail": "Pastora, ovejas",
        "category": "Antiguo Testamento"
    },
    {
        "name": "BARTIMEO",
        "skin": "#D2A77B", "hair": "#3B2F2F", "eye": "#808080",
        "tunic": "#8B8682", "tunic2": "#A9A9A9", "belt": "#696969",
        "detail": "Ciego, bastón",
        "category": "Nuevo Testamento"
    },
    {
        "name": "MARTA",
        "skin": "#F4C7A0", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#D2691E", "tunic2": "#F4A460", "belt": "#8B4513",
        "detail": "Delantal, pan",
        "category": "Nuevo Testamento"
    },
    {
        "name": "LÁZARO",
        "skin": "#D2A77B", "hair": "#3B2F2F", "eye": "#3B2F2F",
        "tunic": "#F5F5DC", "tunic2": "#FAEBD7", "belt": "#D2B48C",
        "detail": "Vendas, resucitado",
        "category": "Nuevo Testamento"
    },
    {
        "name": "ANDRÉS",
        "skin": "#D2A77B", "hair": "#8B4513", "eye": "#3B2F2F",
        "tunic": "#2E8B57", "tunic2": "#3CB371", "belt": "#2F4F4F",
        "detail": "Pescador, red",
        "category": "Nuevo Testamento"
    },
    {
        "name": "SANTIAGO",
        "skin": "#D2A77B", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#8B0000", "tunic2": "#CD5C5C", "belt": "#704214",
        "detail": "Apóstol, bastón",
        "category": "Nuevo Testamento"
    },
    {
        "name": "JUAN",
        "skin": "#F4C7A0", "hair": "#B8530A", "eye": "#3B2F2F",
        "tunic": "#FF4500", "tunic2": "#FF6347", "belt": "#8B4513",
        "detail": "El discípulo amado",
        "category": "Nuevo Testamento"
    },
    {
        "name": "MATEO",
        "skin": "#D2A77B", "hair": "#3B2F2F", "eye": "#3B2F2F",
        "tunic": "#2F4F4F", "tunic2": "#5F9EA0", "belt": "#696969",
        "detail": "Escriba, pergamino",
        "category": "Nuevo Testamento"
    },
    {
        "name": "TOMÁS",
        "skin": "#D2A77B", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#556B2F", "tunic2": "#6B8E23", "belt": "#8B7355",
        "detail": "Manos extendidas",
        "category": "Nuevo Testamento"
    },
    {
        "name": "FELIPE",
        "skin": "#F4C7A0", "hair": "#3B2F2F", "eye": "#3B2F2F",
        "tunic": "#4682B4", "tunic2": "#5F9EA0", "belt": "#2F4F4F",
        "detail": "Carro del etíope",
        "category": "Nuevo Testamento"
    },
    {
        "name": "LOT",
        "skin": "#D2A77B", "hair": "#8B7355", "eye": "#3B2F2F",
        "tunic": "#DAA520", "tunic2": "#F0E68C", "belt": "#B8860B",
        "detail": "Viajero, mochila",
        "category": "Antiguo Testamento"
    },
    {
        "name": "BERNABÉ",
        "skin": "#D2A77B", "hair": "#5C3317", "eye": "#3B2F2F",
        "tunic": "#2E8B57", "tunic2": "#66CDAA", "belt": "#006400",
        "detail": "Consolador, amigo",
        "category": "Nuevo Testamento"
    },
    {
        "name": "ELÍSEO",
        "skin": "#D2A77B", "hair": "#8B7355", "eye": "#3B2F2F",
        "tunic": "#704214", "tunic2": "#8B6914", "belt": "#5C3317",
        "detail": "Manto de profeta, río",
        "category": "Antiguo Testamento"
    },
    {
        "name": "JOSÍAS",
        "skin": "#F4C7A0", "hair": "#3B2F2F", "eye": "#3B2F2F",
        "tunic": "#B8860B", "tunic2": "#DAA520", "belt": "#FFD700",
        "detail": "Rey niño, libro de la Ley",
        "category": "Antiguo Testamento"
    },
]


def draw_cubecraft_face(c, x, y, w, h, color, border_color=None):
    """Draw a single face of the cubecraft template"""
    c.setFillColor(HexColor(color) if isinstance(color, str) else color)
    c.rect(x, y, w, h, fill=1, stroke=0)
    if border_color:
        c.setStrokeColor(HexColor(border_color) if isinstance(border_color, str) else border_color)
    else:
        c.setStrokeColor(black)
    c.setLineWidth(1.2)
    c.rect(x, y, w, h, fill=0, stroke=1)


def draw_tab(c, x, y, w, h, direction="right"):
    """Draw a glue tab"""
    tab_w = 0.25 * inch
    c.setFillColor(HexColor("#E8E8E8"))
    c.setStrokeColor(black)
    c.setLineWidth(0.8)
    c.setDash(3, 2)

    if direction == "right":
        path = c.beginPath()
        path.moveTo(x + w, y)
        path.lineTo(x + w + tab_w, y + h * 0.15)
        path.lineTo(x + w + tab_w, y + h * 0.85)
        path.lineTo(x + w, y + h)
        path.close()
        c.drawPath(path, fill=1, stroke=1)
    elif direction == "left":
        path = c.beginPath()
        path.moveTo(x, y)
        path.lineTo(x - tab_w, y + h * 0.15)
        path.lineTo(x - tab_w, y + h * 0.85)
        path.lineTo(x, y + h)
        path.close()
        c.drawPath(path, fill=1, stroke=1)
    elif direction == "up":
        path = c.beginPath()
        path.moveTo(x, y + h)
        path.lineTo(x + w * 0.15, y + h + tab_w)
        path.lineTo(x + w * 0.85, y + h + tab_w)
        path.lineTo(x + w, y + h)
        path.close()
        c.drawPath(path, fill=1, stroke=1)
    elif direction == "down":
        path = c.beginPath()
        path.moveTo(x, y)
        path.lineTo(x + w * 0.15, y - tab_w)
        path.lineTo(x + w * 0.85, y - tab_w)
        path.lineTo(x + w, y)
        path.close()
        c.drawPath(path, fill=1, stroke=1)

    c.setDash()

    c.setFillColor(HexColor("#999999"))
    c.setFont("Helvetica", 5)
    if direction == "right":
        c.drawCentredString(x + w + tab_w/2, y + h/2 - 2, "PEGAR")
    elif direction == "left":
        c.drawCentredString(x - tab_w/2, y + h/2 - 2, "PEGAR")
    elif direction == "up":
        c.drawCentredString(x + w/2, y + h + tab_w/2 - 2, "PEGAR")
    elif direction == "down":
        c.drawCentredString(x + w/2, y - tab_w/2 - 2, "PEGAR")


def draw_kawaii_face(c, cx, cy, size, char_data):
    """Draw a cute kawaii face on the front of the head"""
    skin = HexColor(char_data["skin"])
    hair = HexColor(char_data["hair"])
    eye_color = HexColor(char_data["eye"])

    eye_r = size * 0.09
    eye_y = cy + size * 0.05
    eye_spacing = size * 0.18

    c.setFillColor(eye_color)
    c.circle(cx - eye_spacing, eye_y, eye_r, fill=1, stroke=0)
    c.circle(cx + eye_spacing, eye_y, eye_r, fill=1, stroke=0)

    c.setFillColor(white)
    c.circle(cx - eye_spacing + eye_r*0.3, eye_y + eye_r*0.3, eye_r*0.35, fill=1, stroke=0)
    c.circle(cx + eye_spacing + eye_r*0.3, eye_y + eye_r*0.3, eye_r*0.35, fill=1, stroke=0)

    c.setStrokeColor(HexColor("#333333"))
    c.setLineWidth(1)
    smile_y = cy - size * 0.12
    path = c.beginPath()
    path.moveTo(cx - size*0.1, smile_y)
    path.curveTo(cx - size*0.05, smile_y - size*0.08,
                 cx + size*0.05, smile_y - size*0.08,
                 cx + size*0.1, smile_y)
    c.drawPath(path, fill=0, stroke=1)

    c.setFillColor(HexColor("#FFB6C1"))
    c.circle(cx - size*0.25, cy - size*0.06, size*0.06, fill=1, stroke=0)
    c.circle(cx + size*0.25, cy - size*0.06, size*0.06, fill=1, stroke=0)


def draw_hair_top(c, x, y, w, h, hair_color):
    """Draw hair on top face"""
    c.setFillColor(HexColor(hair_color))
    c.rect(x, y, w, h, fill=1, stroke=0)
    c.setStrokeColor(black)
    c.setLineWidth(1.2)
    c.rect(x, y, w, h, fill=0, stroke=1)


def draw_tunic_front(c, cx, cy, size, char_data):
    """Draw tunic details on body front"""
    belt_color = HexColor(char_data["belt"])
    c.setFillColor(belt_color)
    c.rect(cx - size*0.45, cy + size*0.25, size*0.9, size*0.1, fill=1, stroke=0)

    c.setStrokeColor(HexColor(char_data["tunic2"]))
    c.setLineWidth(1)
    c.line(cx, cy + size*0.45, cx, cy - size*0.35)


def draw_paper_toy_page(c, w, h, char_data, page_num):
    """Draw a complete cubecraft paper toy template for one character"""

    c.setFillColor(white)
    c.rect(0, 0, w, h, fill=1)

    c.setFillColor(BLUE_DARK)
    c.rect(0, h - 0.55*inch, w, 0.55*inch, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(w/2, h - 0.38*inch, f"PAPER TOY — {char_data['name']}")
    c.setFillColor(AMBER)
    c.setFont("Helvetica", 8)
    c.drawRightString(w - 0.4*inch, h - 0.38*inch, f"{page_num}/50")
    c.drawString(0.4*inch, h - 0.38*inch, char_data["category"])

    face_size = 1.4 * inch

    # ─── HEAD CROSS (centered upper area) ───
    head_cx = w / 2
    head_start_y = h - 1.0*inch

    skin_color = char_data["skin"]
    hair_color = char_data["hair"]

    # Top face (hair)
    draw_hair_top(c, head_cx - face_size/2, head_start_y, face_size, face_size, hair_color)
    draw_tab(c, head_cx - face_size/2, head_start_y, face_size, face_size, "up")

    # Front face (below top)
    front_y = head_start_y - face_size
    draw_cubecraft_face(c, head_cx - face_size/2, front_y, face_size, face_size, skin_color)
    draw_kawaii_face(c, head_cx, front_y + face_size/2, face_size/2, char_data)

    c.setFillColor(HexColor("#333333"))
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(head_cx, front_y + 3, "FRENTE")

    # Left face
    left_x = head_cx - face_size/2 - face_size
    draw_cubecraft_face(c, left_x, front_y, face_size, face_size, skin_color)
    draw_tab(c, left_x, front_y, face_size, face_size, "left")

    c.setFillColor(HexColor(hair_color))
    c.rect(left_x, front_y + face_size*0.6, face_size*0.3, face_size*0.4, fill=1, stroke=0)

    c.setFillColor(HexColor("#333333"))
    c.setFont("Helvetica", 6)
    c.drawCentredString(left_x + face_size/2, front_y + 3, "IZQUIERDA")

    # Right face
    right_x = head_cx + face_size/2
    draw_cubecraft_face(c, right_x, front_y, face_size, face_size, skin_color)
    draw_tab(c, right_x, front_y, face_size, face_size, "right")

    c.setFillColor(HexColor(hair_color))
    c.rect(right_x + face_size*0.7, front_y + face_size*0.6, face_size*0.3, face_size*0.4, fill=1, stroke=0)

    c.setFillColor(HexColor("#333333"))
    c.setFont("Helvetica", 6)
    c.drawCentredString(right_x + face_size/2, front_y + 3, "DERECHA")

    # Back face (below front)
    back_y = front_y - face_size
    draw_cubecraft_face(c, head_cx - face_size/2, back_y, face_size, face_size, hair_color)
    draw_tab(c, head_cx - face_size/2, back_y, face_size, face_size, "down")

    c.setFillColor(white)
    c.setFont("Helvetica", 6)
    c.drawCentredString(head_cx, back_y + face_size/2, "ATRÁS")

    # Bottom face (below back)
    bottom_y = back_y - face_size
    draw_cubecraft_face(c, head_cx - face_size/2, bottom_y, face_size, face_size, skin_color)
    c.setFillColor(HexColor("#333333"))
    c.setFont("Helvetica", 6)
    c.drawCentredString(head_cx, bottom_y + face_size/2, "ABAJO")

    # ─── BODY (below head section) ───
    body_w = face_size
    body_h = face_size * 1.2
    body_start_y = bottom_y - 0.3*inch

    tunic1 = char_data["tunic"]
    tunic2 = char_data["tunic2"]

    # Body top
    draw_cubecraft_face(c, head_cx - body_w/2, body_start_y, body_w, body_w, tunic2)
    draw_tab(c, head_cx - body_w/2, body_start_y, body_w, body_w, "up")
    c.setFillColor(HexColor("#333333"))
    c.setFont("Helvetica", 5)
    c.drawCentredString(head_cx, body_start_y + body_w/2, "ARRIBA")

    # Body front
    body_front_y = body_start_y - body_h
    draw_cubecraft_face(c, head_cx - body_w/2, body_front_y, body_w, body_h, tunic1)
    draw_tunic_front(c, head_cx, body_front_y + body_h/2, body_w/2, char_data)
    c.setFillColor(HexColor("#333333"))
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(head_cx, body_front_y + 3, "FRENTE")

    # Body left
    body_left_x = head_cx - body_w/2 - body_w
    draw_cubecraft_face(c, body_left_x, body_front_y, body_w, body_h, tunic2)
    draw_tab(c, body_left_x, body_front_y, body_w, body_h, "left")

    # Body right
    body_right_x = head_cx + body_w/2
    draw_cubecraft_face(c, body_right_x, body_front_y, body_w, body_h, tunic2)
    draw_tab(c, body_right_x, body_front_y, body_w, body_h, "right")

    # Body back
    body_back_y = body_front_y - body_h
    draw_cubecraft_face(c, head_cx - body_w/2, body_back_y, body_w, body_h, tunic1)
    draw_tab(c, head_cx - body_w/2, body_back_y, body_w, body_h, "down")

    c.setFillColor(white if tunic1 in ["#1C1C1C", "#2F4F4F", "#4B0082", "#006400", "#8B0000"] else HexColor("#333333"))
    c.setFont("Helvetica", 6)
    c.drawCentredString(head_cx, body_back_y + body_h/2, "ATRÁS")

    # Body bottom
    body_bottom_y = body_back_y - body_w
    draw_cubecraft_face(c, head_cx - body_w/2, body_bottom_y, body_w, body_w, tunic2)
    c.setFillColor(HexColor("#333333"))
    c.setFont("Helvetica", 5)
    c.drawCentredString(head_cx, body_bottom_y + body_w/2, "BASE")

    # ─── FOLD LINES ───
    c.setStrokeColor(HexColor("#CCCCCC"))
    c.setLineWidth(0.5)
    c.setDash(4, 3)

    # head fold lines
    c.line(head_cx - face_size/2, head_start_y, head_cx + face_size/2, head_start_y)
    c.line(head_cx - face_size/2, front_y, head_cx + face_size/2, front_y)
    c.line(head_cx - face_size/2, back_y, head_cx + face_size/2, back_y)
    c.line(head_cx - face_size/2, bottom_y, head_cx + face_size/2, bottom_y)

    c.line(head_cx - face_size/2, front_y, head_cx - face_size/2, front_y + face_size)
    c.line(head_cx + face_size/2, front_y, head_cx + face_size/2, front_y + face_size)

    c.setDash()

    # ─── INSTRUCTIONS ───
    inst_y = 0.7*inch
    c.setFillColor(BLUE_DARK)
    c.roundRect(0.4*inch, inst_y - 0.15*inch, w - 0.8*inch, 0.4*inch, 4, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(0.55*inch, inst_y + 0.07*inch, "✂ RECORTAR por las líneas continuas")
    c.drawString(2.8*inch, inst_y + 0.07*inch, "- - - DOBLAR por las líneas punteadas")
    c.drawString(5.2*inch, inst_y + 0.07*inch, "🧴 PEGAR las pestañas")

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w/2, 0.35*inch, f"Mega Kit Bíblico Infantil — Paper Toy: {char_data['name']} — {char_data['detail']}")


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
    c.drawCentredString(w/2, h/2 + 1.8*inch, "PAPER TOYS")

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 32)
    c.drawCentredString(w/2, h/2 + 1.1*inch, "BÍBLICOS")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(w/2, h/2 + 0.4*inch, "RECORTABLES 3D")

    c.setFillColor(BLUE_LIGHT)
    c.setFont("Helvetica", 16)
    c.drawCentredString(w/2, h/2 - 0.3*inch, "50 Personajes · Recorta, Dobla y Pega")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h/2 - 1.0*inch, "¡Crea tus propios muñecos bíblicos!")

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

    for i, char_data in enumerate(CHARACTERS):
        print(f"  Paper Toy {i+1}/50: {char_data['name']}")
        draw_paper_toy_page(c, w, h, char_data, i + 1)
        c.showPage()

    c.save()
    print(f"\n PDF generado: {OUTPUT_PATH}")
    print(f" Total: {len(CHARACTERS)} paper toys")


if __name__ == "__main__":
    main()
