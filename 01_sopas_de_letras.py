import random
import string
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, cm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUTPUT_PATH = r"C:\Users\hp\Documents\kit-biblico-infantil\01_Sopas_de_Letras_Biblicas.pdf"

BLUE_DARK = HexColor("#1e3a5f")
BLUE_MED = HexColor("#2563eb")
BLUE_LIGHT = HexColor("#bfdbfe")
BLUE_BG = HexColor("#eff6ff")
AMBER = HexColor("#d97706")
ORANGE = HexColor("#e67e22")
RED_SOFT = HexColor("#c0392b")
GRAY = HexColor("#555555")
GRAY_LIGHT = HexColor("#e0e0e0")

THEMES = [
    {"title": "La Creación", "words": ["DIOS", "CIELO", "TIERRA", "LUZ", "SOL", "LUNA", "ESTRELLAS", "MAR", "ANIMALES", "HOMBRE", "MUJER", "JARDIN", "EDEN"]},
    {"title": "Noé y el Arca", "words": ["NOE", "ARCA", "DILUVIO", "PALOMA", "ARCOIRIS", "LLUVIA", "ANIMALES", "AGUA", "OBEDIENCIA", "FAMILIA"]},
    {"title": "Moisés", "words": ["MOISES", "EGIPTO", "FARAON", "PLAGA", "MAR ROJO", "DESIERTO", "ZARZA", "MANDAMIENTO", "TABLA", "LIBERTAD"]},
    {"title": "David y Goliat", "words": ["DAVID", "GOLIAT", "HONDA", "PIEDRA", "GIGANTE", "PASTOR", "VALIENTE", "VICTORIA", "FE", "DIOS"]},
    {"title": "Daniel en el Foso", "words": ["DANIEL", "LEON", "FOSO", "ORACION", "ANGEL", "REY", "FE", "PROTECCION", "VALIENTE", "DIOS"]},
    {"title": "Jonás y la Ballena", "words": ["JONAS", "BALLENA", "MAR", "NINIVE", "TORMENTA", "PEZ", "ORACION", "OBEDIENCIA", "DIOS", "PERDON"]},
    {"title": "El Nacimiento de Jesús", "words": ["JESUS", "MARIA", "JOSE", "BELEN", "PESEBRE", "ESTRELLA", "PASTORES", "ANGELES", "MAGOS", "REGALO"]},
    {"title": "Los 12 Discípulos", "words": ["PEDRO", "ANDRES", "SANTIAGO", "JUAN", "FELIPE", "MATEO", "TOMAS", "SIMON", "JUDAS", "BARTOLOME"]},
    {"title": "Parábola del Buen Pastor", "words": ["PASTOR", "OVEJA", "REBANO", "CUIDAR", "BUSCAR", "PERDIDA", "AMOR", "PROTEGER", "CAMPO", "VOZ"]},
    {"title": "Abrahán", "words": ["ABRAHAM", "SARA", "ISAAC", "PROMESA", "ESTRELLA", "FE", "ALTAR", "BENDICION", "HIJO", "DIOS"]},
    {"title": "Los Frutos del Espíritu", "words": ["AMOR", "GOZO", "PAZ", "PACIENCIA", "BONDAD", "FE", "MANSEDUMBRE", "TEMPLANZA", "BENIGNIDAD"]},
    {"title": "El Arca de la Alianza", "words": ["ARCA", "ALIANZA", "TABLAS", "MOISES", "ORO", "TEMPLO", "SANTO", "DIOS", "QUERUBINES", "LEY"]},
    {"title": "La Última Cena", "words": ["JESUS", "PAN", "VINO", "CENA", "MESA", "APOSTOLES", "AMOR", "SERVIR", "LAVADO", "PIES"]},
    {"title": "Samsón", "words": ["SANSON", "FUERZA", "CABELLO", "DALILA", "LEON", "FILISTEOS", "TEMPLO", "JUEZ", "DIOS", "SECRETO"]},
    {"title": "La Torre de Babel", "words": ["TORRE", "BABEL", "CIELO", "IDIOMAS", "CONFUSION", "LADRILLO", "ORGULLO", "DIOS", "LENGUAS", "PUEBLO"]},
    {"title": "Rut y Noemí", "words": ["RUT", "NOEMI", "BOOZ", "TRIGO", "CAMPO", "LEALTAD", "AMOR", "FAMILIA", "BELEN", "FIEL"]},
    {"title": "El Buen Samaritano", "words": ["SAMARITANO", "HERIDO", "CAMINO", "AYUDAR", "AMOR", "PROJIMO", "VENDAS", "ACEITE", "POSADA", "BONDAD"]},
    {"title": "Ester, la Reina Valiente", "words": ["ESTER", "REINA", "REY", "VALIENTE", "PUEBLO", "CORONA", "BANQUETE", "ORACION", "FE", "PERSIA"]},
    {"title": "José y sus Hermanos", "words": ["JOSE", "TUNICA", "SUENO", "EGIPTO", "HERMANOS", "PERDON", "TRIGO", "FARAON", "CARCEL", "COPA"]},
    {"title": "El Mar Rojo", "words": ["MAR", "ROJO", "MOISES", "PUEBLO", "EGIPTO", "MILAGRO", "CAMINO", "AGUA", "LIBERTAD", "FE"]},
    {"title": "La Zarza Ardiente", "words": ["ZARZA", "FUEGO", "MOISES", "DIOS", "SANDALIAS", "MONTE", "SINAI", "VOZ", "MISION", "SANTO"]},
    {"title": "El Rey Salomón", "words": ["SALOMON", "SABIO", "TEMPLO", "REY", "JUICIO", "ORO", "TRONO", "DIOS", "PROVERBIOS", "PAZ"]},
    {"title": "Los Diez Mandamientos", "words": ["MANDAMIENTO", "LEY", "TABLA", "MONTE", "SINAI", "MOISES", "DIOS", "AMOR", "VERDAD", "RESPETO"]},
    {"title": "Jesús Camina sobre el Agua", "words": ["JESUS", "AGUA", "PEDRO", "BARCA", "FE", "MILAGRO", "TORMENTA", "VIENTO", "CAMINAR", "OLAS"]},
    {"title": "La Multiplicación de Panes", "words": ["PAN", "PECES", "JESUS", "MILAGRO", "CINCO", "DOS", "MULTITUD", "CANASTA", "GRACIAS", "COMPARTIR"]},
    {"title": "El Arca de Noé - Animales", "words": ["LEON", "ELEFANTE", "JIRAFA", "PALOMA", "CUERVO", "OVEJA", "CABRA", "CABALLO", "CONEJO", "AGUILA"]},
    {"title": "Nombres de Dios", "words": ["PADRE", "CREADOR", "ETERNO", "TODOPODEROSO", "SANTO", "JUSTO", "AMOR", "LUZ", "REY", "SALVADOR"]},
    {"title": "El Jardín del Edén", "words": ["EDEN", "JARDIN", "ADAN", "EVA", "ARBOL", "FRUTO", "SERPIENTE", "RIO", "PARAISO", "DIOS"]},
    {"title": "Eliseo y los Milagros", "words": ["ELISEO", "ELIAS", "ACEITE", "MANTO", "RIO", "JORDAN", "MILAGRO", "PROFETA", "FE", "DIOS"]},
    {"title": "La Resurreccion", "words": ["JESUS", "TUMBA", "ANGEL", "PIEDRA", "VIDA", "GLORIA", "DOMINGO", "MARIA", "RESURRECCION", "LUZ"]},
    {"title": "Animales de la Biblia", "words": ["CORDERO", "PALOMA", "LEON", "BURRO", "SERPIENTE", "PEZ", "CAMELLO", "BALLENA", "CUERVO", "OVEJA"]},
    {"title": "Personajes Femeninos", "words": ["MARIA", "EVA", "SARA", "RUT", "ESTER", "RAQUEL", "REBECA", "MARTA", "DEBORA", "ANA"]},
    {"title": "La Navidad", "words": ["NAVIDAD", "PESEBRE", "ESTRELLA", "PASTORES", "MAGOS", "ORO", "INCIENSO", "MIRRA", "BELEN", "ANGEL"]},
    {"title": "El Templo de Salomón", "words": ["TEMPLO", "SALOMON", "ORO", "PIEDRA", "ALTAR", "SANTO", "COLUMNA", "QUERUBINES", "DIOS", "GLORIA"]},
    {"title": "Jesús Sana a los Enfermos", "words": ["JESUS", "SANAR", "CIEGO", "SORDO", "ENFERMO", "MILAGRO", "FE", "MANO", "TOCAR", "VIDA"]},
    {"title": "El Bautismo", "words": ["BAUTISMO", "AGUA", "JORDAN", "JUAN", "JESUS", "PALOMA", "CIELO", "VOZ", "ESPIRITU", "SANTO"]},
    {"title": "Ciudades Bíblicas", "words": ["JERUSALEN", "BELEN", "NAZARET", "JERICO", "NINIVE", "ROMA", "EGIPTO", "DAMASCO", "GALILEA", "SAMARIA"]},
    {"title": "Instrumentos Bíblicos", "words": ["ARPA", "TROMPETA", "PANDERO", "FLAUTA", "CIMBALO", "LIRA", "CUERNO", "CANCION", "ALABANZA", "MUSICA"]},
    {"title": "Parábola del Sembrador", "words": ["SEMBRADOR", "SEMILLA", "TIERRA", "ESPINA", "PIEDRA", "FRUTO", "SOL", "AGUA", "CAMINO", "RAIZ"]},
    {"title": "La Oración", "words": ["ORACION", "PADRE", "CIELO", "PAN", "PERDON", "AMOR", "GRACIAS", "RODILLAS", "CORAZON", "FE"]},
    {"title": "El Espíritu Santo", "words": ["ESPIRITU", "SANTO", "FUEGO", "PALOMA", "VIENTO", "LENGUAS", "PODER", "CONSUELO", "VERDAD", "DIOS"]},
    {"title": "Jesús el Buen Pastor", "words": ["JESUS", "PASTOR", "OVEJA", "REBANO", "PUERTA", "VOZ", "CUIDAR", "BUSCAR", "AMOR", "VIDA"]},
    {"title": "Elias y el Monte Carmelo", "words": ["ELIAS", "FUEGO", "CARMELO", "ALTAR", "PROFETA", "CIELO", "LLUVIA", "AGUA", "DIOS", "BAAL"]},
    {"title": "La Fe", "words": ["FE", "CREER", "CONFIANZA", "ESPERANZA", "DIOS", "PALABRA", "FIRME", "SEGURO", "INVISIBLE", "CERTEZA"]},
    {"title": "El Diluvio Universal", "words": ["DILUVIO", "NOE", "LLUVIA", "ARCA", "MONTE", "ARARAT", "PROMESA", "ARCOIRIS", "AGUA", "SALVAR"]},
    {"title": "Profetas de la Biblia", "words": ["ISAIAS", "JEREMIAS", "EZEQUIEL", "DANIEL", "OSEAS", "JOEL", "AMOS", "JONAS", "MALAQUIAS", "ELIAS"]},
    {"title": "Valores Cristianos", "words": ["AMOR", "BONDAD", "PERDON", "HUMILDAD", "PACIENCIA", "GRATITUD", "RESPETO", "HONESTIDAD", "GENEROSIDAD", "PAZ"]},
    {"title": "El Éxodo", "words": ["EXODO", "MOISES", "EGIPTO", "PLAGA", "CORDERO", "SANGRE", "PUERTA", "NOCHE", "PASCUA", "LIBERTAD"]},
    {"title": "La Armadura de Dios", "words": ["ARMADURA", "VERDAD", "JUSTICIA", "PAZ", "FE", "ESCUDO", "ESPADA", "CASCO", "SALVACION", "ORACION"]},
    {"title": "Milagros de Jesús", "words": ["AGUA", "VINO", "PAN", "PECES", "LAZARO", "CIEGO", "CAMINAR", "TORMENTA", "LEPROSO", "MILAGRO"]},
]


def clean_word(word):
    return word.replace(" ", "").replace("á", "A").replace("é", "E").replace("í", "I").replace("ó", "O").replace("ú", "U").replace("ñ", "N").replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U").replace("Ñ", "N").upper()


def generate_word_search(words, grid_size=14):
    grid = [['' for _ in range(grid_size)] for _ in range(grid_size)]
    directions = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
    placed = []

    cleaned = [(clean_word(w), w) for w in words]
    cleaned.sort(key=lambda x: -len(x[0]))

    for clean, original in cleaned:
        if len(clean) > grid_size:
            continue
        placed_word = False
        for attempt in range(200):
            d = random.choice(directions)
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)
            end_row = row + d[0] * (len(clean) - 1)
            end_col = col + d[1] * (len(clean) - 1)
            if end_row < 0 or end_row >= grid_size or end_col < 0 or end_col >= grid_size:
                continue
            ok = True
            for i, ch in enumerate(clean):
                r = row + d[0] * i
                c = col + d[1] * i
                if grid[r][c] != '' and grid[r][c] != ch:
                    ok = False
                    break
            if ok:
                for i, ch in enumerate(clean):
                    r = row + d[0] * i
                    c = col + d[1] * i
                    grid[r][c] = ch
                placed.append(original)
                placed_word = True
                break

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for r in range(grid_size):
        for c in range(grid_size):
            if grid[r][c] == '':
                grid[r][c] = random.choice(letters)

    return grid, placed


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
    c.drawCentredString(w/2, h/2 + 1.5*inch, "✨ SOPAS DE LETRAS ✨")

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(w/2, h/2 + 0.7*inch, "BÍBLICAS")

    c.setFillColor(BLUE_LIGHT)
    c.setFont("Helvetica", 16)
    c.drawCentredString(w/2, h/2, "50 Temas · +500 Palabras por Encontrar")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h/2 - 0.8*inch, "¡Aprende la Biblia jugando!")

    c.setFillColor(GRAY_LIGHT)
    c.setFont("Helvetica", 11)
    c.drawCentredString(w/2, 1.5*inch, "Para niños de 4 a 10 años")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(w/2, 0.8*inch, "www.kitbiblicoinfantil.com")


def draw_toc(c, w, h, themes):
    c.setFillColor(BLUE_BG)
    c.rect(0, 0, w, h, fill=1)

    c.setFillColor(BLUE_DARK)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(w/2, h - 0.8*inch, "ÍNDICE")

    c.setFillColor(AMBER)
    c.rect(w/2 - 1.5*inch, h - 0.95*inch, 3*inch, 2, fill=1)

    y = h - 1.4*inch
    col1_x = 0.7*inch
    col2_x = w/2 + 0.3*inch
    items_per_col = 25

    for i, theme in enumerate(themes):
        if i < items_per_col:
            x = col1_x
            current_y = y - (i * 0.3*inch)
        else:
            x = col2_x
            current_y = y - ((i - items_per_col) * 0.3*inch)

        c.setFillColor(BLUE_MED)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(x, current_y, f"{i+1}.")
        c.setFillColor(GRAY)
        c.setFont("Helvetica", 9)
        c.drawString(x + 0.25*inch, current_y, theme["title"])


def draw_word_search_page(c, w, h, theme_data, page_num, grid_size=14):
    grid, placed = generate_word_search(theme_data["words"], grid_size)

    c.setFillColor(BLUE_BG)
    c.rect(0, 0, w, h, fill=1)

    c.setFillColor(BLUE_DARK)
    c.rect(0, h - 0.7*inch, w, 0.7*inch, fill=1)

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(w/2, h - 0.48*inch, f"✨ {theme_data['title'].upper()} ✨")

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 9)
    c.drawString(w - 1.2*inch, h - 0.48*inch, f"Página {page_num}")

    cell_size = 0.38*inch
    grid_width = grid_size * cell_size
    grid_height = grid_size * cell_size
    start_x = (w - grid_width) / 2
    start_y = h - 1.0*inch - grid_height + (grid_size * cell_size)

    for r in range(grid_size):
        for col_idx in range(grid_size):
            x = start_x + col_idx * cell_size
            y = start_y - r * cell_size

            if (r + col_idx) % 2 == 0:
                c.setFillColor(white)
            else:
                c.setFillColor(HexColor("#e0edff"))
            c.rect(x, y - cell_size, cell_size, cell_size, fill=1)

            c.setStrokeColor(BLUE_LIGHT)
            c.setLineWidth(0.5)
            c.rect(x, y - cell_size, cell_size, cell_size, stroke=1, fill=0)

            c.setFillColor(BLUE_DARK)
            c.setFont("Helvetica-Bold", 14)
            c.drawCentredString(x + cell_size/2, y - cell_size + cell_size*0.3, grid[r][col_idx])

    words_y = start_y - grid_size * cell_size - 0.3*inch

    c.setFillColor(BLUE_DARK)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(w/2, words_y, "PALABRAS POR ENCONTRAR:")

    words_y -= 0.25*inch
    cols = 3
    col_width = (w - 1.4*inch) / cols

    for i, word in enumerate(placed):
        col = i % cols
        row = i // cols
        x = 0.7*inch + col * col_width
        y = words_y - row * 0.22*inch

        c.setFillColor(BLUE_MED)
        c.setFont("Helvetica", 10)
        c.drawString(x, y, f"▸ {word}")

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w/2, 0.35*inch, "Mega Kit Bíblico Infantil — Sopas de Letras Bíblicas")


def main():
    w, h = letter
    c = canvas.Canvas(OUTPUT_PATH, pagesize=letter)

    draw_cover(c, w, h)
    c.showPage()

    draw_toc(c, w, h, THEMES)
    c.showPage()

    for i, theme in enumerate(THEMES):
        print(f"  Generando sopa de letras {i+1}/50: {theme['title']}")
        draw_word_search_page(c, w, h, theme, i + 1)
        c.showPage()

    c.save()
    print(f"\n PDF generado: {OUTPUT_PATH}")
    print(f" Total: {len(THEMES)} sopas de letras + capa + indice")

if __name__ == "__main__":
    random.seed(42)
    main()
