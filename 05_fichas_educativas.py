import random
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white

OUTPUT_PATH = r"C:\Users\hp\Documents\kit-biblico-infantil\05_Fichas_Educativas_Biblicas.pdf"

BLUE_DARK = HexColor("#1e3a5f")
BLUE_MED = HexColor("#2563eb")
BLUE_BG = HexColor("#eff6ff")
BLUE_LIGHT = HexColor("#bfdbfe")
AMBER = HexColor("#d97706")
GRAY = HexColor("#555555")
GRAY_LIGHT = HexColor("#e0e0e0")
ORANGE = HexColor("#e67e22")
BLUE = HexColor("#2980b9")
RED = HexColor("#c0392b")

VF_SHEETS = [
    {"title": "La Creación", "questions": [
        ("Dios creó el mundo en 6 días y descansó el séptimo.", True),
        ("La primera mujer se llamaba María.", False),
        ("Dios creó la luz el primer día.", True),
        ("Adán fue creado del barro.", True),
        ("El primer animal creado fue el perro.", False),
        ("Dios dijo que todo lo que creó era bueno.", True),
        ("El sol fue creado antes que la luz.", False),
        ("El jardín donde vivían Adán y Eva se llamaba Edén.", True),
    ]},
    {"title": "Noé y el Diluvio", "questions": [
        ("Noé construyó un castillo para protegerse.", False),
        ("El diluvio duró 40 días y 40 noches.", True),
        ("Noé metió solo perros en el arca.", False),
        ("La paloma trajo una rama de olivo.", True),
        ("El arcoíris fue una señal de la promesa de Dios.", True),
        ("Noé tenía 30 años cuando construyó el arca.", False),
        ("Dios le dijo a Noé cómo construir el arca.", True),
        ("En el arca entraron dos animales de cada especie.", True),
    ]},
    {"title": "Moisés", "questions": [
        ("Moisés fue encontrado en un río dentro de una canasta.", True),
        ("Moisés dividió el mar Rojo con una espada.", False),
        ("Dios le habló a Moisés desde una zarza ardiente.", True),
        ("Moisés recibió los 10 mandamientos en el Monte Sinaí.", True),
        ("Moisés nació en Roma.", False),
        ("Moisés guió al pueblo de Israel por el desierto.", True),
        ("El faraón dejó ir al pueblo inmediatamente.", False),
        ("Dios envió 10 plagas a Egipto.", True),
    ]},
    {"title": "David", "questions": [
        ("David era un pastor de ovejas.", True),
        ("David venció a Goliat con una espada.", False),
        ("David tocaba el arpa.", True),
        ("Goliat era un guerrero gigante.", True),
        ("David usó 5 piedras contra Goliat.", True),
        ("David tenía miedo de Goliat.", False),
        ("David llegó a ser rey de Israel.", True),
        ("David escribió muchos salmos.", True),
    ]},
    {"title": "Daniel", "questions": [
        ("Daniel fue lanzado a un foso de serpientes.", False),
        ("Daniel oraba tres veces al día.", True),
        ("Un ángel cerró la boca de los leones.", True),
        ("Daniel vivía en Egipto.", False),
        ("El rey se alegró de que Daniel estuviera bien.", True),
        ("Daniel desobedeció a Dios.", False),
        ("Daniel fue fiel a Dios toda su vida.", True),
        ("Daniel interpretaba sueños.", True),
    ]},
    {"title": "Jonás", "questions": [
        ("Dios le pidió a Jonás ir a Nínive.", True),
        ("Jonás obedeció inmediatamente.", False),
        ("Jonás fue tragado por un tiburón.", False),
        ("Jonás estuvo tres días dentro del gran pez.", True),
        ("Los marineros lanzaron a Jonás al mar.", True),
        ("La gente de Nínive no escuchó a Jonás.", False),
        ("Dios perdonó a la ciudad de Nínive.", True),
        ("Jonás estaba contento con el perdón de Dios.", False),
    ]},
    {"title": "Jesús - Su Nacimiento", "questions": [
        ("Jesús nació en un palacio.", False),
        ("María era la madre de Jesús.", True),
        ("Jesús nació en Belén.", True),
        ("Los reyes magos trajeron 2 regalos.", False),
        ("Un ángel avisó a los pastores.", True),
        ("José era carpintero.", True),
        ("Una estrella guió a los reyes magos.", True),
        ("Jesús nació en verano.", False),
    ]},
    {"title": "Jesús - Sus Milagros", "questions": [
        ("Jesús convirtió el agua en jugo.", False),
        ("Jesús caminó sobre el agua.", True),
        ("Jesús sanó a ciegos y enfermos.", True),
        ("Jesús multiplicó 5 panes y 2 peces.", True),
        ("Jesús calmó una tormenta.", True),
        ("Jesús resucitó a Lázaro.", True),
        ("Jesús solo hizo un milagro.", False),
        ("Pedro también caminó sobre el agua.", True),
    ]},
    {"title": "Abraham", "questions": [
        ("Abraham fue padre de Isaac.", True),
        ("Sara era la esposa de Abraham.", True),
        ("Dios le prometió a Abraham muchos descendientes.", True),
        ("Abraham vivía en Roma.", False),
        ("Abraham tenía poca fe en Dios.", False),
        ("Isaac era el hijo de la promesa.", True),
        ("Abraham estaba dispuesto a obedecer a Dios en todo.", True),
        ("Sara rió cuando escuchó que tendría un hijo.", True),
    ]},
    {"title": "Los Discípulos", "questions": [
        ("Jesús tuvo 12 discípulos.", True),
        ("Pedro era pescador antes de seguir a Jesús.", True),
        ("Mateo era carpintero.", False),
        ("Jesús llamó a sus discípulos en un templo.", False),
        ("Los discípulos dejaron todo para seguir a Jesús.", True),
        ("Judas traicionó a Jesús.", True),
        ("Juan era conocido como el discípulo amado.", True),
        ("Tomás creyó sin ver al principio.", False),
    ]},
]

COMPLETAR_SHEETS = [
    {"title": "Completa el Versículo", "items": [
        ("Porque de tal manera amó Dios al _____", "MUNDO"),
        ("El Señor es mi _____; nada me faltará", "PASTOR"),
        ("Ama a tu _____ como a ti mismo", "PROJIMO"),
        ("Todo lo puedo en Cristo que me _____", "FORTALECE"),
        ("Yo soy el camino, la _____ y la vida", "VERDAD"),
        ("Honra a tu _____ y a tu madre", "PADRE"),
        ("No tengas _____; yo estoy contigo", "MIEDO"),
        ("La fe es la certeza de lo que se _____", "ESPERA"),
    ]},
    {"title": "Completa la Historia de Noé", "items": [
        ("Noé construyó un _____ muy grande", "ARCA"),
        ("Llovió durante 40 _____ y 40 noches", "DIAS"),
        ("La _____ trajo una rama de olivo", "PALOMA"),
        ("Dios puso un _____ en el cielo como promesa", "ARCOIRIS"),
        ("Entraron _____ animales de cada especie", "DOS"),
        ("El arca se detuvo en el monte _____", "ARARAT"),
        ("Noé era un hombre _____ y justo", "BUENO"),
        ("Dios prometió no enviar otro _____", "DILUVIO"),
    ]},
    {"title": "Completa sobre Jesús", "items": [
        ("Jesús nació en la ciudad de _____", "BELEN"),
        ("María y José pusieron a Jesús en un _____", "PESEBRE"),
        ("Jesús fue bautizado en el río _____", "JORDAN"),
        ("Jesús multiplicó 5 _____ y 2 peces", "PANES"),
        ("Jesús dijo: Dejen que los _____ vengan a mí", "NINOS"),
        ("Jesús resucitó al _____ día", "TERCER"),
        ("Jesús calmó la _____ en el mar", "TORMENTA"),
        ("Jesús lavó los _____ de sus discípulos", "PIES"),
    ]},
    {"title": "Completa sobre David", "items": [
        ("David era pastor de _____", "OVEJAS"),
        ("David venció a _____ con una honda", "GOLIAT"),
        ("David tocaba el _____ para el rey Saúl", "ARPA"),
        ("David usó _____ piedras del río", "CINCO"),
        ("David escribió muchos _____", "SALMOS"),
        ("David fue ungido por el profeta _____", "SAMUEL"),
        ("David tenía un corazón conforme al de _____", "DIOS"),
        ("David fue rey de _____", "ISRAEL"),
    ]},
    {"title": "Completa sobre Moisés", "items": [
        ("Moisés fue encontrado en el _____ Nilo", "RIO"),
        ("Dios habló desde una _____ ardiente", "ZARZA"),
        ("Moisés dividió el Mar _____", "ROJO"),
        ("Dios envió 10 _____ a Egipto", "PLAGAS"),
        ("Moisés recibió los mandamientos en el Monte _____", "SINAI"),
        ("El pueblo caminó por el _____ 40 años", "DESIERTO"),
        ("Moisés llevaba un _____ en la mano", "BASTON"),
        ("Dios alimentó al pueblo con _____ del cielo", "MANA"),
    ]},
    {"title": "Completa sobre la Navidad", "items": [
        ("El ángel _____ visitó a María", "GABRIEL"),
        ("Jesús nació en un _____", "ESTABLO"),
        ("Los _____ magos vinieron de oriente", "REYES"),
        ("Trajeron oro, incienso y _____", "MIRRA"),
        ("Una _____ brillante guió a los magos", "ESTRELLA"),
        ("Los _____ fueron los primeros en visitar a Jesús", "PASTORES"),
        ("José era de la casa de _____", "DAVID"),
        ("No había lugar en la _____", "POSADA"),
    ]},
    {"title": "Completa los Mandamientos", "items": [
        ("Amarás al Señor tu _____ con todo tu corazón", "DIOS"),
        ("No tendrás otros _____ delante de mí", "DIOSES"),
        ("Honra a tu padre y a tu _____", "MADRE"),
        ("No _____", "MATARAS"),
        ("No _____", "ROBARAS"),
        ("No dirás falso _____", "TESTIMONIO"),
        ("Santificarás el día de _____", "REPOSO"),
        ("No _____  el nombre de Dios en vano", "TOMARAS"),
    ]},
    {"title": "Completa sobre el Arca", "items": [
        ("El _____ entró de dos en dos", "LEON"),
        ("La _____ voló para buscar tierra", "PALOMA"),
        ("El _____ caminó lento hacia el arca", "ELEFANTE"),
        ("Las _____ nadaban fuera del arca", "BALLENAS"),
        ("El _____ trepó al arca con su pareja", "MONO"),
        ("La _____ alta entró agachando su cuello", "JIRAFA"),
        ("El _____ cantó desde el techo del arca", "GALLO"),
        ("Noé cuidó a todos los _____ del arca", "ANIMALES"),
    ]},
    {"title": "Completa sobre los Profetas", "items": [
        ("_____ fue tragado por un gran pez", "JONAS"),
        ("_____ subió al cielo en un carro de fuego", "ELIAS"),
        ("_____ interpretaba sueños en Babilonia", "DANIEL"),
        ("_____ profetizó el nacimiento de Jesús", "ISAIAS"),
        ("_____ lloró por su pueblo", "JEREMIAS"),
        ("_____ vio un valle de huesos secos", "EZEQUIEL"),
        ("_____ fue un pastor antes de ser profeta", "AMOS"),
        ("_____ era esposo de una mujer infiel", "OSEAS"),
    ]},
    {"title": "Completa sobre Parábolas", "items": [
        ("El buen _____ ayudó al herido en el camino", "SAMARITANO"),
        ("El hijo _____ regresó a casa de su padre", "PRODIGO"),
        ("El _____ sembró semillas en diferentes tierras", "SEMBRADOR"),
        ("La oveja _____ fue buscada por el pastor", "PERDIDA"),
        ("El _____ encontró un tesoro en el campo", "HOMBRE"),
        ("La _____ de mostaza es la más pequeña", "SEMILLA"),
        ("Las vírgenes _____ tenían aceite en sus lámparas", "PRUDENTES"),
        ("El siervo _____ multiplicó los talentos", "FIEL"),
    ]},
]

QUIZ_SHEETS = [
    {"title": "Quiz: Personajes Bíblicos", "questions": [
        {"q": "¿Quién construyó el arca?", "options": ["Abraham", "Noé", "Moisés", "David"], "answer": 1},
        {"q": "¿Quién dividió el Mar Rojo?", "options": ["Josué", "Elías", "Moisés", "Daniel"], "answer": 2},
        {"q": "¿Quién venció a Goliat?", "options": ["Sansón", "David", "Salomón", "Pedro"], "answer": 1},
        {"q": "¿Quién fue tragado por un gran pez?", "options": ["Jonás", "Pedro", "Pablo", "Juan"], "answer": 0},
        {"q": "¿Quién fue la madre de Jesús?", "options": ["Sara", "Rut", "María", "Ester"], "answer": 2},
        {"q": "¿Quién fue el primer hombre?", "options": ["Noé", "Abraham", "Adán", "Moisés"], "answer": 2},
    ]},
    {"title": "Quiz: Historias Bíblicas", "questions": [
        {"q": "¿Dónde nació Jesús?", "options": ["Nazaret", "Jerusalén", "Belén", "Egipto"], "answer": 2},
        {"q": "¿Cuántos mandamientos recibió Moisés?", "options": ["5", "7", "10", "12"], "answer": 2},
        {"q": "¿Qué instrumento tocaba David?", "options": ["Flauta", "Arpa", "Trompeta", "Pandero"], "answer": 1},
        {"q": "¿Cuántos discípulos tuvo Jesús?", "options": ["7", "10", "12", "15"], "answer": 2},
        {"q": "¿Qué animal tragó a Jonás?", "options": ["Tiburón", "Delfín", "Gran pez", "Cocodrilo"], "answer": 2},
        {"q": "¿Cuántos días llovió en el diluvio?", "options": ["7", "20", "40", "100"], "answer": 2},
    ]},
    {"title": "Quiz: Animales de la Biblia", "questions": [
        {"q": "¿Qué animal llevó una rama de olivo a Noé?", "options": ["Cuervo", "Paloma", "Águila", "Golondrina"], "answer": 1},
        {"q": "¿Qué animal habló con Eva?", "options": ["Loro", "León", "Serpiente", "Burro"], "answer": 2},
        {"q": "¿Qué animales estaban en el foso de Daniel?", "options": ["Osos", "Leones", "Lobos", "Tigres"], "answer": 1},
        {"q": "¿Qué animal venció Sansón con sus manos?", "options": ["Oso", "León", "Toro", "Águila"], "answer": 1},
        {"q": "Jesús entró a Jerusalén montado en un...", "options": ["Caballo", "Camello", "Burro", "Elefante"], "answer": 2},
        {"q": "¿Qué animal representa al Espíritu Santo?", "options": ["Cordero", "Paloma", "León", "Águila"], "answer": 1},
    ]},
    {"title": "Quiz: Lugares de la Biblia", "questions": [
        {"q": "¿Dónde vivían Adán y Eva?", "options": ["Belén", "Edén", "Egipto", "Roma"], "answer": 1},
        {"q": "¿De dónde sacó Moisés al pueblo?", "options": ["Babilonia", "Roma", "Egipto", "Persia"], "answer": 2},
        {"q": "¿Dónde recibió Moisés los mandamientos?", "options": ["Monte Carmelo", "Monte Sinaí", "Monte Olivete", "Monte Nebo"], "answer": 1},
        {"q": "¿En qué río fue bautizado Jesús?", "options": ["Nilo", "Éufrates", "Jordán", "Tigris"], "answer": 2},
        {"q": "¿Adónde no quería ir Jonás?", "options": ["Belén", "Nínive", "Roma", "Egipto"], "answer": 1},
        {"q": "¿Dónde construyó Salomón el templo?", "options": ["Belén", "Nazaret", "Jerusalén", "Jericó"], "answer": 2},
    ]},
    {"title": "Quiz: Números en la Biblia", "questions": [
        {"q": "¿En cuántos días creó Dios el mundo?", "options": ["5", "6", "7", "10"], "answer": 1},
        {"q": "¿Cuántas plagas envió Dios a Egipto?", "options": ["5", "7", "10", "12"], "answer": 2},
        {"q": "¿Cuántos años estuvo Israel en el desierto?", "options": ["10", "20", "30", "40"], "answer": 3},
        {"q": "¿Cuántos panes multiplicó Jesús?", "options": ["2", "3", "5", "7"], "answer": 2},
        {"q": "¿Cuántas veces negó Pedro a Jesús?", "options": ["1", "2", "3", "4"], "answer": 2},
        {"q": "¿Cuántos hijos tuvo Jacob?", "options": ["7", "10", "12", "15"], "answer": 2},
    ]},
]


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
    c.drawCentredString(w/2, h/2 + 1.5*inch, "FICHAS EDUCATIVAS")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(w/2, h/2 + 0.7*inch, "BÍBLICAS")
    c.setFillColor(BLUE_LIGHT)
    c.setFont("Helvetica", 14)
    c.drawCentredString(w/2, h/2, "Verdadero o Falso · Completar · Quiz")
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h/2 - 0.8*inch, "¡Aprende y diviértete con la Biblia!")
    c.setFillColor(GRAY_LIGHT)
    c.setFont("Helvetica", 11)
    c.drawCentredString(w/2, 1.5*inch, "Para niños de 4 a 10 años")
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(w/2, 0.8*inch, "www.kitbiblicoinfantil.com")


def draw_vf_page(c, w, h, sheet, page_num):
    c.setFillColor(BLUE_BG)
    c.rect(0, 0, w, h, fill=1)

    c.setFillColor(BLUE_DARK)
    c.rect(0, h - 0.7*inch, w, 0.7*inch, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h - 0.45*inch, f"VERDADERO O FALSO: {sheet['title']}")
    c.setFillColor(AMBER)
    c.setFont("Helvetica", 9)
    c.drawRightString(w - 0.4*inch, h - 0.45*inch, f"Ficha {page_num}")

    y = h - 1.2*inch
    for i, (question, answer) in enumerate(sheet["questions"]):
        bg = white if i % 2 == 0 else HexColor("#e8f5e9")
        c.setFillColor(bg)
        c.roundRect(0.5*inch, y - 0.55*inch, w - 1*inch, 0.6*inch, 5, fill=1, stroke=0)

        c.setFillColor(BLUE_DARK)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(0.7*inch, y - 0.25*inch, f"{i+1}.")

        c.setFillColor(GRAY)
        c.setFont("Helvetica", 10)
        c.drawString(1.0*inch, y - 0.25*inch, question)

        c.setStrokeColor(BLUE_MED)
        c.setLineWidth(1.5)
        c.setFillColor(white)
        c.circle(w - 1.8*inch, y - 0.25*inch, 8, fill=1, stroke=1)
        c.circle(w - 1.0*inch, y - 0.25*inch, 8, fill=1, stroke=1)

        c.setFillColor(HexColor("#27ae60"))
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(w - 1.8*inch, y - 0.28*inch, "V")
        c.setFillColor(RED)
        c.drawCentredString(w - 1.0*inch, y - 0.28*inch, "F")

        y -= 0.7*inch

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w/2, 0.35*inch, "Mega Kit Bíblico Infantil — Fichas Educativas")


def draw_completar_page(c, w, h, sheet, page_num):
    c.setFillColor(BLUE_BG)
    c.rect(0, 0, w, h, fill=1)

    c.setFillColor(BLUE_DARK)
    c.rect(0, h - 0.7*inch, w, 0.7*inch, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h - 0.45*inch, f"COMPLETA: {sheet['title']}")
    c.setFillColor(AMBER)
    c.setFont("Helvetica", 9)
    c.drawRightString(w - 0.4*inch, h - 0.45*inch, f"Ficha {page_num}")

    y = h - 1.2*inch
    for i, (sentence, answer) in enumerate(sheet["items"]):
        bg = white if i % 2 == 0 else HexColor("#e8f5e9")
        c.setFillColor(bg)
        c.roundRect(0.5*inch, y - 0.55*inch, w - 1*inch, 0.6*inch, 5, fill=1, stroke=0)

        c.setFillColor(BLUE_DARK)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(0.7*inch, y - 0.2*inch, f"{i+1}.")

        c.setFillColor(GRAY)
        c.setFont("Helvetica", 10)
        parts = sentence.split("_____")
        x = 1.0*inch
        for pi, part in enumerate(parts):
            c.drawString(x, y - 0.2*inch, part)
            x += c.stringWidth(part, "Helvetica", 10)
            if pi < len(parts) - 1:
                c.setStrokeColor(BLUE_MED)
                c.setLineWidth(1)
                c.line(x, y - 0.35*inch, x + 1.2*inch, y - 0.35*inch)
                x += 1.3*inch

        y -= 0.7*inch

    c.setFillColor(BLUE_MED)
    c.setFont("Helvetica-Bold", 9)
    words_hint = ", ".join([item[1] for item in sheet["items"]])
    c.drawCentredString(w/2, 0.7*inch, f"Palabras: {words_hint}")

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w/2, 0.35*inch, "Mega Kit Bíblico Infantil — Fichas Educativas")


def draw_quiz_page(c, w, h, sheet, page_num):
    c.setFillColor(BLUE_BG)
    c.rect(0, 0, w, h, fill=1)

    c.setFillColor(BLUE_DARK)
    c.rect(0, h - 0.7*inch, w, 0.7*inch, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h - 0.45*inch, sheet['title'])
    c.setFillColor(AMBER)
    c.setFont("Helvetica", 9)
    c.drawRightString(w - 0.4*inch, h - 0.45*inch, f"Ficha {page_num}")

    y = h - 1.1*inch
    for i, q in enumerate(sheet["questions"]):
        c.setFillColor(BLUE_DARK)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(0.7*inch, y, f"{i+1}. {q['q']}")
        y -= 0.3*inch

        for j, opt in enumerate(q["options"]):
            letter = chr(65 + j)
            c.setStrokeColor(BLUE_MED)
            c.setFillColor(white)
            c.circle(1.1*inch, y + 0.03*inch, 7, fill=1, stroke=1)
            c.setFillColor(BLUE_DARK)
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(1.1*inch, y - 0.02*inch, letter)
            c.setFillColor(GRAY)
            c.setFont("Helvetica", 10)
            c.drawString(1.4*inch, y, opt)
            y -= 0.25*inch

        y -= 0.15*inch

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w/2, 0.35*inch, "Mega Kit Bíblico Infantil — Fichas Educativas")


def main():
    w, h = letter
    c = canvas.Canvas(OUTPUT_PATH, pagesize=letter)

    draw_cover(c, w, h)
    c.showPage()

    page_num = 1
    for sheet in VF_SHEETS:
        print(f"  V/F: {sheet['title']}")
        draw_vf_page(c, w, h, sheet, page_num)
        c.showPage()
        page_num += 1

    for sheet in COMPLETAR_SHEETS:
        print(f"  Completar: {sheet['title']}")
        draw_completar_page(c, w, h, sheet, page_num)
        c.showPage()
        page_num += 1

    for sheet in QUIZ_SHEETS:
        print(f"  Quiz: {sheet['title']}")
        draw_quiz_page(c, w, h, sheet, page_num)
        c.showPage()
        page_num += 1

    c.save()
    print(f"\n PDF generado: {OUTPUT_PATH}")
    print(f" Total: {page_num - 1} fichas educativas")

if __name__ == "__main__":
    main()
