import random
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black

OUTPUT_PATH = r"C:\Users\hp\Documents\kit-biblico-infantil\02_Laberintos_Biblicos.pdf"

BLUE_DARK = HexColor("#1e3a5f")
BLUE_MED = HexColor("#2563eb")
BLUE_LIGHT = HexColor("#bfdbfe")
BLUE_BG = HexColor("#eff6ff")
AMBER = HexColor("#d97706")
WALL_COLOR = HexColor("#1e3a5f")
PATH_COLOR = white

MAZE_THEMES = [
    {"title": "Ayuda a Noé a llegar al Arca", "emoji_start": "👨", "emoji_end": "🚢", "difficulty": "easy"},
    {"title": "Guía a Moisés por el desierto", "emoji_start": "👨", "emoji_end": "⛰️", "difficulty": "easy"},
    {"title": "Lleva a David hasta Goliat", "emoji_start": "🧒", "emoji_end": "👹", "difficulty": "easy"},
    {"title": "Ayuda a Jonás a salir de la ballena", "emoji_start": "👨", "emoji_end": "🐋", "difficulty": "easy"},
    {"title": "Guía a los Reyes Magos a Belén", "emoji_start": "👑", "emoji_end": "⭐", "difficulty": "easy"},
    {"title": "Lleva a José a Egipto", "emoji_start": "👨", "emoji_end": "🏛️", "difficulty": "medium"},
    {"title": "Ayuda a Daniel a escapar del foso", "emoji_start": "👨", "emoji_end": "🦁", "difficulty": "medium"},
    {"title": "Guía a Rut al campo de trigo", "emoji_start": "👩", "emoji_end": "🌾", "difficulty": "medium"},
    {"title": "Lleva a Abraham a la tierra prometida", "emoji_start": "👴", "emoji_end": "🏔️", "difficulty": "medium"},
    {"title": "Ayuda a Pedro a llegar a Jesús", "emoji_start": "👨", "emoji_end": "✝️", "difficulty": "medium"},
    {"title": "Guía al Buen Pastor a la oveja perdida", "emoji_start": "👨", "emoji_end": "🐑", "difficulty": "easy"},
    {"title": "Lleva a Ester al palacio del Rey", "emoji_start": "👸", "emoji_end": "👑", "difficulty": "medium"},
    {"title": "Ayuda a Sansón a encontrar su fuerza", "emoji_start": "💪", "emoji_end": "⭐", "difficulty": "medium"},
    {"title": "Guía a María y José a Belén", "emoji_start": "👫", "emoji_end": "🏠", "difficulty": "easy"},
    {"title": "Lleva a Elías al Monte Carmelo", "emoji_start": "👨", "emoji_end": "🔥", "difficulty": "hard"},
    {"title": "Ayuda a los israelitas a cruzar el Mar Rojo", "emoji_start": "👥", "emoji_end": "🌊", "difficulty": "hard"},
    {"title": "Guía a Josué a Jericó", "emoji_start": "⚔️", "emoji_end": "🏰", "difficulty": "hard"},
    {"title": "Lleva la paloma de Noé al olivo", "emoji_start": "🕊️", "emoji_end": "🌿", "difficulty": "easy"},
    {"title": "Ayuda a Salomón a construir el Templo", "emoji_start": "👑", "emoji_end": "🏛️", "difficulty": "hard"},
    {"title": "Guía a Rebeca al pozo de agua", "emoji_start": "👩", "emoji_end": "💧", "difficulty": "easy"},
    {"title": "Lleva a Pablo a predicar en Roma", "emoji_start": "👨", "emoji_end": "🏛️", "difficulty": "hard"},
    {"title": "Ayuda al hijo pródigo a volver a casa", "emoji_start": "🧒", "emoji_end": "🏠", "difficulty": "medium"},
    {"title": "Guía a Gedeón a la victoria", "emoji_start": "⚔️", "emoji_end": "🏆", "difficulty": "hard"},
    {"title": "Lleva a Zaqueo al árbol", "emoji_start": "👨", "emoji_end": "🌳", "difficulty": "easy"},
    {"title": "Ayuda a los pastores a encontrar al niño Jesús", "emoji_start": "🐑", "emoji_end": "👶", "difficulty": "easy"},
    {"title": "Guía a Nehemías para reconstruir el muro", "emoji_start": "👨", "emoji_end": "🧱", "difficulty": "hard"},
    {"title": "Lleva a Eliseo al río Jordán", "emoji_start": "👨", "emoji_end": "🌊", "difficulty": "medium"},
    {"title": "Ayuda a Samuel a llegar al Templo", "emoji_start": "🧒", "emoji_end": "🏛️", "difficulty": "easy"},
    {"title": "Guía al ciego Bartimeo hasta Jesús", "emoji_start": "👨", "emoji_end": "✨", "difficulty": "medium"},
    {"title": "Lleva a Adán al Jardín del Edén", "emoji_start": "👨", "emoji_end": "🌺", "difficulty": "easy"},
    {"title": "Ayuda a Eva a encontrar el fruto", "emoji_start": "👩", "emoji_end": "🍎", "difficulty": "easy"},
    {"title": "Guía a Isaac al Monte Moriah", "emoji_start": "🧒", "emoji_end": "⛰️", "difficulty": "medium"},
    {"title": "Lleva a Débora al campo de batalla", "emoji_start": "👩", "emoji_end": "⚔️", "difficulty": "hard"},
    {"title": "Ayuda a Marta a llegar a la cocina", "emoji_start": "👩", "emoji_end": "🍞", "difficulty": "easy"},
    {"title": "Guía a Lázaro fuera de la tumba", "emoji_start": "👨", "emoji_end": "☀️", "difficulty": "medium"},
    {"title": "Lleva al burrito a Belén con María", "emoji_start": "🫏", "emoji_end": "⭐", "difficulty": "easy"},
    {"title": "Ayuda a Booz a encontrar a Rut", "emoji_start": "👨", "emoji_end": "👩", "difficulty": "medium"},
    {"title": "Guía a Jacob al pozo de Raquel", "emoji_start": "👨", "emoji_end": "💧", "difficulty": "medium"},
    {"title": "Lleva a Moisés al Monte Sinaí", "emoji_start": "👨", "emoji_end": "📜", "difficulty": "hard"},
    {"title": "Ayuda a Jesús a llegar al Templo", "emoji_start": "🧒", "emoji_end": "🏛️", "difficulty": "easy"},
    {"title": "Guía a los discípulos a la barca", "emoji_start": "👥", "emoji_end": "⛵", "difficulty": "medium"},
    {"title": "Lleva al cordero al pesebre", "emoji_start": "🐑", "emoji_end": "👶", "difficulty": "easy"},
    {"title": "Ayuda a Ana a llegar al Templo a orar", "emoji_start": "👩", "emoji_end": "🙏", "difficulty": "easy"},
    {"title": "Guía a Josías al libro de la Ley", "emoji_start": "👑", "emoji_end": "📖", "difficulty": "hard"},
    {"title": "Lleva a Felipe al carro del etíope", "emoji_start": "👨", "emoji_end": "🐎", "difficulty": "medium"},
    {"title": "Ayuda al ángel a llegar a María", "emoji_start": "😇", "emoji_end": "👩", "difficulty": "easy"},
    {"title": "Guía a Timoteo a estudiar las Escrituras", "emoji_start": "🧒", "emoji_end": "📖", "difficulty": "easy"},
    {"title": "Lleva a Lot fuera de Sodoma", "emoji_start": "👨", "emoji_end": "🏔️", "difficulty": "hard"},
    {"title": "Ayuda a la viuda a encontrar el aceite", "emoji_start": "👩", "emoji_end": "🫗", "difficulty": "medium"},
    {"title": "Guía a Jesús resucitado a los discípulos", "emoji_start": "✨", "emoji_end": "👥", "difficulty": "medium"},
]


def generate_maze(rows, cols):
    maze = [[1] * cols for _ in range(rows)]

    def carve(r, c):
        maze[r][c] = 0
        dirs = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(dirs)
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 1:
                maze[r + dr//2][c + dc//2] = 0
                carve(nr, nc)

    carve(1, 1)
    maze[0][1] = 0
    maze[rows-1][cols-2] = 0
    return maze


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
    c.drawCentredString(w/2, h/2 + 1.5*inch, "🏰 LABERINTOS 🏰")

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(w/2, h/2 + 0.7*inch, "BÍBLICOS")

    c.setFillColor(BLUE_LIGHT)
    c.setFont("Helvetica", 16)
    c.drawCentredString(w/2, h/2, "50 Laberintos · Fácil, Medio y Difícil")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h/2 - 0.8*inch, "¡Encuentra el camino correcto!")

    c.setFillColor(GRAY_LIGHT)
    c.setFont("Helvetica", 11)
    c.drawCentredString(w/2, 1.5*inch, "Para niños de 4 a 10 años")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(w/2, 0.8*inch, "www.kitbiblicoinfantil.com")


GRAY_LIGHT = HexColor("#e0e0e0")


def draw_maze_page(c, w, h, theme, page_num):
    diff = theme["difficulty"]
    if diff == "easy":
        rows, cols = 13, 13
        diff_label = "⭐ FÁCIL"
        diff_color = HexColor("#27ae60")
    elif diff == "medium":
        rows, cols = 17, 17
        diff_label = "⭐⭐ MEDIO"
        diff_color = HexColor("#f39c12")
    else:
        rows, cols = 21, 21
        diff_label = "⭐⭐⭐ DIFÍCIL"
        diff_color = HexColor("#e74c3c")

    maze = generate_maze(rows, cols)

    c.setFillColor(BLUE_BG)
    c.rect(0, 0, w, h, fill=1)

    c.setFillColor(BLUE_DARK)
    c.rect(0, h - 0.7*inch, w, 0.7*inch, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    title_text = theme['title']
    if len(title_text) > 45:
        c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(w/2, h - 0.45*inch, title_text)

    c.setFillColor(diff_color)
    c.roundRect(0.4*inch, h - 1.1*inch, 1.5*inch, 0.28*inch, 5, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(0.4*inch + 0.75*inch, h - 1.03*inch, diff_label)

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 9)
    c.drawRightString(w - 0.4*inch, h - 1.03*inch, f"Laberinto {page_num}")

    available_height = h - 2.0*inch
    available_width = w - 1.4*inch
    cell_w = available_width / cols
    cell_h = available_height / rows
    cell_size = min(cell_w, cell_h)

    grid_w = cols * cell_size
    grid_h = rows * cell_size
    ox = (w - grid_w) / 2
    oy = (h - 1.3*inch - grid_h)

    for r in range(rows):
        for col_idx in range(cols):
            x = ox + col_idx * cell_size
            y = oy + (rows - 1 - r) * cell_size
            if maze[r][col_idx] == 1:
                c.setFillColor(WALL_COLOR)
                c.rect(x, y, cell_size, cell_size, fill=1, stroke=0)
            else:
                c.setFillColor(white)
                c.rect(x, y, cell_size, cell_size, fill=1, stroke=0)

    c.setStrokeColor(BLUE_DARK)
    c.setLineWidth(2)
    c.rect(ox, oy, grid_w, grid_h, fill=0, stroke=1)

    c.setFillColor(HexColor("#e74c3c"))
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(ox + 1 * cell_size + cell_size/2, oy + grid_h + 0.1*inch, "ENTRADA")

    c.setFillColor(HexColor("#27ae60"))
    c.drawCentredString(ox + (cols-2) * cell_size + cell_size/2, oy - 0.15*inch, "SALIDA")

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w/2, 0.35*inch, "Mega Kit Bíblico Infantil — Laberintos Bíblicos")


def main():
    w, h = letter
    c = canvas.Canvas(OUTPUT_PATH, pagesize=letter)

    draw_cover(c, w, h)
    c.showPage()

    for i, theme in enumerate(MAZE_THEMES):
        print(f"  Generando laberinto {i+1}/50: {theme['title']}")
        draw_maze_page(c, w, h, theme, i + 1)
        c.showPage()

    c.save()
    print(f"\n PDF generado: {OUTPUT_PATH}")
    print(f" Total: {len(MAZE_THEMES)} laberintos")

if __name__ == "__main__":
    random.seed(123)
    main()
