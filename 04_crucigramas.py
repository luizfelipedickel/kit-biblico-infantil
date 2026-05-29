import random
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black

OUTPUT_PATH = r"C:\Users\hp\Documents\kit-biblico-infantil\04_Crucigramas_Biblicos.pdf"

BLUE_DARK = HexColor("#1e3a5f")
BLUE_MED = HexColor("#2563eb")
BLUE_LIGHT = HexColor("#bfdbfe")
BLUE_BG = HexColor("#eff6ff")
AMBER = HexColor("#d97706")
GRAY_LIGHT = HexColor("#e0e0e0")

CROSSWORDS = [
    {"title": "La Creación", "clues_h": [
        {"word": "LUZ", "clue": "Lo primero que Dios creó", "row": 0, "col": 0},
        {"word": "SOL", "clue": "Estrella que alumbra el día", "row": 2, "col": 1},
        {"word": "MAR", "clue": "Donde viven los peces", "row": 4, "col": 0},
        {"word": "EVA", "clue": "Primera mujer", "row": 6, "col": 2},
    ], "clues_v": [
        {"word": "LUNA", "clue": "Brilla en la noche", "row": 0, "col": 2},
        {"word": "ADAN", "clue": "Primer hombre", "row": 1, "col": 0},
        {"word": "DIOS", "clue": "Creador de todo", "row": 3, "col": 4},
    ]},
    {"title": "Noé y el Arca", "clues_h": [
        {"word": "NOE", "clue": "Construyó el arca", "row": 0, "col": 0},
        {"word": "ARCA", "clue": "Barco gigante de madera", "row": 2, "col": 0},
        {"word": "AGUA", "clue": "Cubrió toda la tierra", "row": 4, "col": 1},
    ], "clues_v": [
        {"word": "ARCO", "clue": "Promesa de Dios en el cielo", "row": 0, "col": 0},
        {"word": "PALOMA", "clue": "Trajo una rama de olivo", "row": 0, "col": 2},
    ]},
    {"title": "Moisés en Egipto", "clues_h": [
        {"word": "MOISES", "clue": "Liberó al pueblo de Israel", "row": 0, "col": 0},
        {"word": "PLAGA", "clue": "Castigo enviado a Egipto", "row": 2, "col": 0},
        {"word": "MAR", "clue": "Se abrió en dos partes", "row": 4, "col": 1},
    ], "clues_v": [
        {"word": "ZARZA", "clue": "Ardía pero no se quemaba", "row": 0, "col": 3},
        {"word": "LEY", "clue": "Los 10 mandamientos", "row": 1, "col": 0},
    ]},
    {"title": "David y Goliat", "clues_h": [
        {"word": "DAVID", "clue": "Pastor que venció al gigante", "row": 0, "col": 0},
        {"word": "HONDA", "clue": "Arma que usó David", "row": 2, "col": 0},
        {"word": "REY", "clue": "David llegó a ser...", "row": 4, "col": 1},
    ], "clues_v": [
        {"word": "DIOS", "clue": "Ayudó a David a vencer", "row": 0, "col": 0},
        {"word": "ARPA", "clue": "Instrumento que tocaba David", "row": 1, "col": 3},
    ]},
    {"title": "Daniel y los Leones", "clues_h": [
        {"word": "DANIEL", "clue": "Fue lanzado al foso", "row": 0, "col": 0},
        {"word": "LEON", "clue": "Animal del foso", "row": 2, "col": 0},
        {"word": "ANGEL", "clue": "Cerró la boca de los leones", "row": 4, "col": 0},
    ], "clues_v": [
        {"word": "ORAR", "clue": "Daniel lo hacía tres veces al día", "row": 0, "col": 3},
        {"word": "FE", "clue": "Daniel tenía mucha...", "row": 1, "col": 0},
    ]},
]

SIMPLE_CROSSWORDS = [
    {"title": "Jonás y la Ballena", "words": ["JONAS", "BALLENA", "MAR", "NINIVE", "PERDON"]},
    {"title": "El Nacimiento de Jesús", "words": ["JESUS", "MARIA", "JOSE", "BELEN", "ESTRELLA"]},
    {"title": "Los Discípulos", "words": ["PEDRO", "JUAN", "MATEO", "FELIPE", "TOMAS"]},
    {"title": "El Buen Pastor", "words": ["PASTOR", "OVEJA", "REBANO", "AMOR", "CUIDAR"]},
    {"title": "Abraham y Sara", "words": ["ABRAHAM", "SARA", "ISAAC", "PROMESA", "FE"]},
    {"title": "Los Frutos del Espíritu", "words": ["AMOR", "GOZO", "PAZ", "BONDAD", "FE"]},
    {"title": "La Última Cena", "words": ["PAN", "VINO", "CENA", "JESUS", "AMOR"]},
    {"title": "Sansón", "words": ["SANSON", "FUERZA", "DALILA", "LEON", "JUEZ"]},
    {"title": "La Torre de Babel", "words": ["TORRE", "BABEL", "CIELO", "LENGUAS", "ORGULLO"]},
    {"title": "Rut y Noemí", "words": ["RUT", "NOEMI", "BOOZ", "TRIGO", "LEALTAD"]},
    {"title": "El Buen Samaritano", "words": ["AYUDAR", "HERIDO", "CAMINO", "BONDAD", "AMOR"]},
    {"title": "La Reina Ester", "words": ["ESTER", "REINA", "CORONA", "VALIENTE", "PUEBLO"]},
    {"title": "José en Egipto", "words": ["JOSE", "TUNICA", "SUENO", "PERDON", "TRIGO"]},
    {"title": "El Mar Rojo", "words": ["MAR", "ROJO", "MOISES", "MILAGRO", "LIBERTAD"]},
    {"title": "El Rey Salomón", "words": ["SALOMON", "SABIO", "TEMPLO", "ORO", "PAZ"]},
    {"title": "Los Mandamientos", "words": ["AMAR", "HONRAR", "VERDAD", "RESPETAR", "DIOS"]},
    {"title": "Jesús sobre el Agua", "words": ["JESUS", "AGUA", "PEDRO", "BARCA", "FE"]},
    {"title": "Panes y Peces", "words": ["PAN", "PECES", "CINCO", "MILAGRO", "GRACIAS"]},
    {"title": "El Arca de Noé", "words": ["LEON", "PALOMA", "OVEJA", "AGUILA", "JIRAFA"]},
    {"title": "Nombres de Dios", "words": ["PADRE", "CREADOR", "ETERNO", "SANTO", "AMOR"]},
    {"title": "El Jardín del Edén", "words": ["EDEN", "JARDIN", "ARBOL", "FRUTO", "RIO"]},
    {"title": "La Resurrección", "words": ["JESUS", "TUMBA", "ANGEL", "VIDA", "GLORIA"]},
    {"title": "Animales Bíblicos", "words": ["CORDERO", "PALOMA", "LEON", "BURRO", "PEZ"]},
    {"title": "Mujeres de la Biblia", "words": ["MARIA", "EVA", "SARA", "RUT", "ESTER"]},
    {"title": "La Navidad", "words": ["NAVIDAD", "PESEBRE", "ESTRELLA", "MAGOS", "ANGEL"]},
    {"title": "El Bautismo", "words": ["BAUTISMO", "AGUA", "JORDAN", "PALOMA", "CIELO"]},
    {"title": "Ciudades Bíblicas", "words": ["BELEN", "NAZARET", "JERICO", "ROMA", "GALILEA"]},
    {"title": "Instrumentos de Alabanza", "words": ["ARPA", "PANDERO", "FLAUTA", "MUSICA", "CANCION"]},
    {"title": "El Sembrador", "words": ["SEMILLA", "TIERRA", "FRUTO", "SOL", "AGUA"]},
    {"title": "La Oración", "words": ["ORACION", "PADRE", "PERDON", "GRACIAS", "AMOR"]},
    {"title": "El Espíritu Santo", "words": ["ESPIRITU", "FUEGO", "PALOMA", "PODER", "VERDAD"]},
    {"title": "Elías Profeta", "words": ["ELIAS", "FUEGO", "ALTAR", "LLUVIA", "CIELO"]},
    {"title": "Valores Cristianos", "words": ["AMOR", "BONDAD", "PERDON", "PAZ", "HUMILDAD"]},
    {"title": "El Éxodo", "words": ["EXODO", "MOISES", "PLAGA", "PASCUA", "CORDERO"]},
    {"title": "La Armadura de Dios", "words": ["VERDAD", "ESCUDO", "ESPADA", "CASCO", "FE"]},
    {"title": "Milagros de Jesús", "words": ["SANAR", "CIEGO", "LAZARO", "AGUA", "VINO"]},
    {"title": "Profetas", "words": ["ISAIAS", "DANIEL", "JONAS", "ELIAS", "AMOS"]},
    {"title": "El Templo de Dios", "words": ["TEMPLO", "ALTAR", "SANTO", "ORO", "GLORIA"]},
    {"title": "Parábolas de Jesús", "words": ["PASTOR", "SEMILLA", "PERLA", "TESORO", "HIJO"]},
    {"title": "La Biblia", "words": ["BIBLIA", "PALABRA", "VERDAD", "VIDA", "LUZ"]},
    {"title": "Ángeles", "words": ["ANGEL", "GABRIEL", "MIGUEL", "CIELO", "ALAS"]},
    {"title": "El Cielo", "words": ["CIELO", "GLORIA", "ETERNO", "PAZ", "VIDA"]},
    {"title": "La Fe", "words": ["FE", "CREER", "ESPERANZA", "FIRME", "DIOS"]},
    {"title": "Jesús el Salvador", "words": ["JESUS", "SALVADOR", "CRUZ", "AMOR", "VIDA"]},
    {"title": "Dones del Espíritu", "words": ["SABIDURIA", "SANIDAD", "PROFECIA", "FE", "LENGUAS"]},
]


def clean_word(word):
    return word.replace(" ", "").replace("á", "A").replace("é", "E").replace("í", "I").replace("ó", "O").replace("ú", "U").replace("ñ", "N").upper()


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
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(w/2, h/2 + 1.5*inch, "CRUCIGRAMAS")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(w/2, h/2 + 0.7*inch, "BÍBLICOS")
    c.setFillColor(BLUE_LIGHT)
    c.setFont("Helvetica", 16)
    c.drawCentredString(w/2, h/2, "50 Crucigramas · Aprende Jugando")
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h/2 - 0.8*inch, "¡Descubre las palabras de la Biblia!")
    c.setFillColor(GRAY_LIGHT)
    c.setFont("Helvetica", 11)
    c.drawCentredString(w/2, 1.5*inch, "Para niños de 4 a 10 años")
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(w/2, 0.8*inch, "www.kitbiblicoinfantil.com")


def draw_simple_crossword_page(c, w, h, theme, page_num):
    c.setFillColor(BLUE_BG)
    c.rect(0, 0, w, h, fill=1)

    c.setFillColor(BLUE_DARK)
    c.rect(0, h - 0.7*inch, w, 0.7*inch, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 15)
    c.drawCentredString(w/2, h - 0.45*inch, f"✏️ {theme['title']}")

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 9)
    c.drawRightString(w - 0.4*inch, h - 0.45*inch, f"Crucigrama {page_num}")

    words = theme["words"]
    cleaned = [clean_word(w_) for w_ in words]

    main_word = max(cleaned, key=len)
    main_idx = cleaned.index(main_word)
    other_words = [(cleaned[i], words[i]) for i in range(len(words)) if i != main_idx]

    cell_size = 0.4 * inch
    main_len = len(main_word)

    start_x = (w - cell_size) / 2
    start_y = h - 1.2*inch

    for i, ch in enumerate(main_word):
        x = start_x
        y = start_y - i * cell_size
        c.setStrokeColor(BLUE_MED)
        c.setLineWidth(1.5)
        c.setFillColor(white)
        c.rect(x, y - cell_size, cell_size, cell_size, fill=1, stroke=1)

        c.setFillColor(BLUE_DARK)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(x + 2, y - 10, str(i + 1))

    used_rows = set()
    clues = []
    clue_num = main_len + 1

    for ci, (cword, original) in enumerate(other_words):
        common = []
        for mi, mch in enumerate(main_word):
            if mi in used_rows:
                continue
            for wi, wch in enumerate(cword):
                if mch == wch:
                    common.append((mi, wi))
                    break
            if common and common[-1][0] == mi:
                break

        if common:
            row_idx, word_pos = common[0]
            used_rows.add(row_idx)

            cross_start_x = start_x - word_pos * cell_size
            cross_y = start_y - row_idx * cell_size

            for wi, ch in enumerate(cword):
                x = cross_start_x + wi * cell_size
                if wi == word_pos:
                    continue
                c.setStrokeColor(BLUE_MED)
                c.setLineWidth(1.5)
                c.setFillColor(HexColor("#e8f5e9"))
                c.rect(x, cross_y - cell_size, cell_size, cell_size, fill=1, stroke=1)

            c.setFillColor(BLUE_DARK)
            c.setFont("Helvetica-Bold", 7)
            c.drawString(cross_start_x + 2, cross_y - 10, str(clue_num))
            clues.append((clue_num, original, "horizontal"))
            clue_num += 1

    clues_y = start_y - main_len * cell_size - 0.5*inch

    c.setFillColor(BLUE_DARK)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.7*inch, clues_y, "PISTAS:")

    c.setFillColor(BLUE_MED)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0.7*inch, clues_y - 0.3*inch, "VERTICAL (↓):")

    c.setFillColor(GRAY)
    c.setFont("Helvetica", 9)
    hint = f"1-{main_len}. Palabra principal: {words[main_idx]} (lee las primeras letras)"
    c.drawString(0.9*inch, clues_y - 0.55*inch, hint)

    if clues:
        c.setFillColor(BLUE_MED)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0.7*inch, clues_y - 0.9*inch, "HORIZONTAL (→):")

        for i, (num, word, _) in enumerate(clues):
            c.setFillColor(GRAY)
            c.setFont("Helvetica", 9)
            blanks = "_ " * len(clean_word(word))
            c.drawString(0.9*inch, clues_y - 1.15*inch - i*0.22*inch, f"{num}. {blanks} ({len(clean_word(word))} letras)")

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w/2, 0.35*inch, "Mega Kit Bíblico Infantil — Crucigramas Bíblicos")


GRAY = HexColor("#555555")


def main():
    w, h = letter
    c = canvas.Canvas(OUTPUT_PATH, pagesize=letter)

    draw_cover(c, w, h)
    c.showPage()

    all_themes = SIMPLE_CROSSWORDS[:50]
    for i, theme in enumerate(all_themes):
        print(f"  Generando crucigrama {i+1}/50: {theme['title']}")
        draw_simple_crossword_page(c, w, h, theme, i + 1)
        c.showPage()

    c.save()
    print(f"\n PDF generado: {OUTPUT_PATH}")

if __name__ == "__main__":
    random.seed(42)
    main()
