from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib import colors

OUTPUT_PATH = r"C:\Users\hp\Documents\kit-biblico-infantil\06_Historias_Biblicas_Ilustradas.pdf"

BLUE_DARK = HexColor("#1e3a5f")
BLUE_MED = HexColor("#2563eb")
BLUE_LIGHT = HexColor("#bfdbfe")
BLUE_BG = HexColor("#eff6ff")
AMBER = HexColor("#d97706")
GRAY_LIGHT = HexColor("#e0e0e0")
TEXT_COLOR = HexColor("#1e3a5f")

STORIES = [
    {
        "title": "La Creación del Mundo",
        "bible_ref": "Génesis 1-2",
        "paragraphs": [
            "Al principio, no había nada. Todo estaba oscuro y vacío. Pero Dios tenía un plan maravilloso.",
            "En el primer día, Dios dijo: \"¡Que haya luz!\" Y la luz apareció, brillante y hermosa. Dios separó la luz de la oscuridad y las llamó día y noche.",
            "En los siguientes días, Dios creó el cielo azul, los mares y la tierra firme. Hizo crecer plantas, flores y árboles llenos de frutas deliciosas.",
            "Luego creó el sol para el día, la luna y las estrellas para la noche. Llenó el mar de peces de colores y el cielo de pájaros que cantaban.",
            "Después creó todos los animales: leones, mariposas, elefantes, perritos y gatitos. ¡Cada uno era especial y diferente!",
            "Finalmente, Dios creó al hombre y a la mujer, Adán y Eva, y los puso en un jardín hermoso llamado Edén. El séptimo día, Dios descansó y vio que todo era muy bueno.",
        ],
        "lesson": "Dios creó todo con amor, y tú eres su creación más especial.",
        "activity": "Dibuja tu animal favorito que Dios creó.",
    },
    {
        "title": "Noé y el Gran Diluvio",
        "bible_ref": "Génesis 6-9",
        "paragraphs": [
            "Hace mucho tiempo, las personas se habían olvidado de Dios y hacían cosas malas. Pero había un hombre bueno llamado Noé que amaba a Dios.",
            "Dios le dijo a Noé: \"Va a llover mucho. Construye un arca grande de madera.\" Noé obedeció, aunque la gente se reía de él.",
            "Noé construyó el arca con la ayuda de su familia. Era enorme, ¡más grande que una casa! Tenía tres pisos y muchas habitaciones.",
            "Cuando el arca estuvo lista, los animales llegaron de dos en dos: dos leones, dos jirafas, dos elefantes, dos pajaritos... ¡Todos entraron ordenadamente!",
            "Entonces empezó a llover. Llovió durante cuarenta días y cuarenta noches sin parar. El agua cubrió toda la tierra, pero el arca flotaba segura.",
            "Cuando la lluvia paró, Noé envió una paloma. La paloma volvió con una rama de olivo en su pico. ¡La tierra se estaba secando! Dios puso un arcoíris en el cielo como promesa de que nunca más habría un diluvio así.",
        ],
        "lesson": "Cuando obedecemos a Dios, Él nos protege siempre.",
        "activity": "¿Cuántos animales puedes nombrar que entraron al arca?",
    },
    {
        "title": "Abraham y la Promesa de Dios",
        "bible_ref": "Génesis 12-21",
        "paragraphs": [
            "Abraham era un hombre que vivía en una ciudad llamada Ur. Un día, Dios le habló y le dijo algo increíble.",
            "\"Abraham, deja tu tierra y ve al lugar que yo te mostraré. Haré de ti una gran nación y te bendeciré,\" dijo Dios.",
            "Abraham confió en Dios y emprendió el viaje con su esposa Sara. Caminaron muchos días hasta llegar a una tierra nueva y hermosa.",
            "Dios le prometió a Abraham que tendría tantos hijos como estrellas hay en el cielo. Pero pasaron muchos años y Abraham y Sara no tenían hijos.",
            "Abraham nunca dejó de creer en la promesa de Dios. Y cuando ya eran muy viejitos, ¡Dios les dio un hijo! Lo llamaron Isaac, que significa \"risa\".",
            "Abraham aprendió que las promesas de Dios siempre se cumplen, aunque a veces hay que esperar con paciencia.",
        ],
        "lesson": "Dios siempre cumple sus promesas. Confía en Él.",
        "activity": "Sal al patio de noche y cuenta cuántas estrellas puedes ver.",
    },
    {
        "title": "Moisés y la Zarza Ardiente",
        "bible_ref": "Éxodo 3",
        "paragraphs": [
            "El pueblo de Israel vivía como esclavo en Egipto. Trabajaban muy duro y sufrían mucho. Pero Dios los escuchó.",
            "Moisés era un hombre que cuidaba ovejas en el desierto. Un día vio algo asombroso: ¡un arbusto que ardía en fuego pero no se quemaba!",
            "Moisés se acercó con curiosidad. Entonces escuchó la voz de Dios: \"¡Moisés! Quítate las sandalias, porque estás en tierra santa.\"",
            "Dios le dijo: \"He visto el sufrimiento de mi pueblo. Tú los sacarás de Egipto y los llevarás a una tierra donde fluye leche y miel.\"",
            "Moisés tenía miedo. \"¿Quién soy yo para hacer algo tan grande?\" preguntó. Pero Dios le prometió: \"Yo estaré contigo.\"",
            "Con la ayuda de Dios, Moisés fue valiente. Se presentó ante el faraón y dijo: \"¡Deja ir a mi pueblo!\" Y después de muchas señales, el faraón los dejó ir.",
        ],
        "lesson": "Dios puede usar a cualquier persona para hacer cosas grandes.",
        "activity": "¿Alguna vez tuviste miedo de hacer algo difícil? Recuerda que Dios está contigo.",
    },
    {
        "title": "David y el Gigante Goliat",
        "bible_ref": "1 Samuel 17",
        "paragraphs": [
            "Los filisteos tenían un guerrero gigante llamado Goliat. Era enorme, ¡medía casi tres metros! Todos los soldados de Israel le tenían miedo.",
            "Goliat gritaba todos los días: \"¡Envíen a alguien a pelear conmigo!\" Pero nadie se atrevía a enfrentarlo.",
            "David era un joven pastor que cuidaba las ovejas de su padre. Era pequeño pero muy valiente, porque confiaba en Dios.",
            "Cuando David escuchó a Goliat burlarse de Dios, se enojó. \"Yo pelearé contra él,\" dijo. El rey Saúl no podía creerlo.",
            "David no llevó espada ni armadura. Solo tomó cinco piedras lisas del río y su honda. Goliat se rio al verlo.",
            "Pero David le dijo: \"Tú vienes con espada, pero yo vengo en el nombre de Dios.\" Lanzó una piedra con su honda y... ¡le dio justo en la frente! El gigante cayó al suelo. ¡David había ganado!",
        ],
        "lesson": "No importa lo pequeño que seas, con Dios puedes vencer cualquier problema.",
        "activity": "Dibuja a David y a Goliat. ¿Quién es más grande? ¿Quién ganó?",
    },
    {
        "title": "Daniel en el Foso de los Leones",
        "bible_ref": "Daniel 6",
        "paragraphs": [
            "Daniel era un hombre muy sabio que amaba a Dios. Oraba tres veces al día, todos los días, sin falta.",
            "Algunos hombres envidiosos hicieron que el rey creara una ley: \"Nadie puede orar a ningún dios. Solo al rey. El que desobedezca será echado al foso de los leones.\"",
            "Daniel escuchó la nueva ley, pero no dejó de orar a Dios. Se arrodilló junto a su ventana y oró como siempre.",
            "Los hombres envidiosos lo vieron y corrieron a decirle al rey. El rey estaba muy triste porque quería mucho a Daniel, pero tuvo que cumplir la ley.",
            "Daniel fue echado al foso lleno de leones hambrientos. El rey le dijo: \"Que tu Dios te salve.\" Y pasó toda la noche sin dormir.",
            "Al amanecer, el rey corrió al foso y gritó: \"¡Daniel! ¿Te salvó tu Dios?\" Y Daniel respondió: \"¡Sí! Dios envió un ángel que cerró la boca de los leones. ¡Estoy bien!\" El rey se alegró mucho.",
        ],
        "lesson": "Nunca dejes de hablar con Dios. Él siempre te protege.",
        "activity": "¿Cuántas veces al día puedes hablar con Dios?",
    },
    {
        "title": "Jonás y la Ballena",
        "bible_ref": "Jonás 1-4",
        "paragraphs": [
            "Dios le pidió a Jonás que fuera a la ciudad de Nínive a decirles que se portaran bien. Pero Jonás no quería ir.",
            "En vez de obedecer, Jonás se subió a un barco que iba en la dirección opuesta. \"¡Me escaparé de Dios!\" pensó.",
            "Pero Dios envió una tormenta terrible. El barco se sacudía de un lado a otro. Los marineros tenían mucho miedo.",
            "Jonás sabía que la tormenta era por su culpa. \"Échenme al mar y la tormenta parará,\" les dijo. Los marineros lo lanzaron al agua y... ¡la tormenta se detuvo!",
            "Pero Jonás no se ahogó. ¡Un enorme pez se lo tragó! Jonás estuvo tres días dentro del pez. Allí oró y le pidió perdón a Dios.",
            "El pez escupió a Jonás en la playa. Esta vez, Jonás obedeció y fue a Nínive. Le dijo al pueblo que se arrepintiera, ¡y lo hicieron! Dios los perdonó.",
        ],
        "lesson": "Es mejor obedecer a Dios desde el principio. Él sabe lo que es mejor.",
        "activity": "¿Cuántos días estuvo Jonás dentro del pez? Dibuja el pez grande.",
    },
    {
        "title": "El Nacimiento de Jesús",
        "bible_ref": "Lucas 2:1-20",
        "paragraphs": [
            "María y José viajaron a la ciudad de Belén. María iba a tener un bebé muy especial, el Hijo de Dios.",
            "Cuando llegaron a Belén, no había lugar en ninguna posada. Todas estaban llenas. Por fin, alguien les ofreció un establo donde dormían los animales.",
            "Esa noche, en el humilde establo, nació Jesús. María lo envolvió en telas suaves y lo acostó en un pesebre, que es donde comen los animales.",
            "En los campos cercanos, unos pastores cuidaban sus ovejas bajo las estrellas. De repente, ¡un ángel apareció y todo se llenó de luz!",
            "El ángel les dijo: \"¡No tengan miedo! Les traigo buenas noticias. Hoy ha nacido el Salvador en Belén.\" Luego, muchos ángeles cantaron en el cielo.",
            "Los pastores corrieron a Belén y encontraron al bebé Jesús, tal como el ángel les había dicho. Se arrodillaron llenos de alegría y adoraron al niño.",
        ],
        "lesson": "Jesús vino al mundo porque Dios nos ama muchísimo.",
        "activity": "Haz un dibujo del pesebre con el niño Jesús.",
    },
    {
        "title": "Los Reyes Magos",
        "bible_ref": "Mateo 2:1-12",
        "paragraphs": [
            "Lejos, en el oriente, unos hombres sabios vieron una estrella muy brillante y especial en el cielo. Sabían que significaba que había nacido un rey.",
            "Los sabios prepararon regalos preciosos y emprendieron un largo viaje siguiendo la estrella. Viajaron durante muchos días por desiertos y montañas.",
            "Primero llegaron al palacio del rey Herodes en Jerusalén. \"¿Dónde está el nuevo rey?\" preguntaron. Herodes se asustó mucho.",
            "Los sabios siguieron la estrella hasta Belén. La estrella se detuvo justo encima del lugar donde estaba el niño Jesús.",
            "Cuando vieron al niño, se arrodillaron y le ofrecieron sus regalos: oro, incienso y mirra. Eran regalos dignos de un rey.",
            "Un ángel les avisó en sueños que no volvieran donde Herodes. Así que regresaron a su tierra por otro camino, felices de haber conocido al Rey de Reyes.",
        ],
        "lesson": "Como los sabios, debemos buscar a Jesús y darle lo mejor.",
        "activity": "¿Cuáles fueron los tres regalos? Dibújalos.",
    },
    {
        "title": "Jesús Calma la Tormenta",
        "bible_ref": "Marcos 4:35-41",
        "paragraphs": [
            "Un día, Jesús y sus discípulos subieron a una barca para cruzar el lago. Jesús estaba muy cansado y se quedó dormido.",
            "De repente, una tormenta terrible apareció. El viento soplaba con fuerza y las olas eran enormes. La barca se llenaba de agua.",
            "Los discípulos estaban asustadísimos. \"¡Nos vamos a hundir!\" gritaban. Corrieron a despertar a Jesús.",
            "\"¡Maestro! ¿No te importa que nos ahogemos?\" le dijeron con miedo.",
            "Jesús se levantó tranquilamente. Miró al viento y al mar y dijo con voz firme: \"¡Silencio! ¡Cálmate!\" Al instante, el viento paró y el mar quedó completamente tranquilo.",
            "Los discípulos se miraron asombrados. \"¿Quién es este hombre que hasta el viento y el mar le obedecen?\" Ese día entendieron que Jesús tenía un poder muy especial.",
        ],
        "lesson": "Cuando tengas miedo, llama a Jesús. Él puede calmar cualquier tormenta.",
        "activity": "Dibuja una barca en el mar. En un lado la tormenta, en el otro la calma.",
    },
    {
        "title": "La Multiplicación de los Panes y los Peces",
        "bible_ref": "Juan 6:1-14",
        "paragraphs": [
            "Miles de personas seguían a Jesús para escuchar sus enseñanzas. Ese día había más de cinco mil personas, y estaban lejos de cualquier pueblo.",
            "Cuando se hizo tarde, todos tenían hambre. Los discípulos le dijeron a Jesús: \"No hay comida suficiente para tanta gente.\"",
            "Un niño se acercó con su almuerzo: cinco panes pequeños y dos pescados. \"Es lo único que tenemos,\" dijeron los discípulos.",
            "Jesús sonrió. Tomó los panes y los pescados, miró al cielo y dio gracias a Dios. Luego empezó a partir el pan.",
            "¡Los panes y los pescados no se acababan! Los discípulos repartían y repartían, y seguía habiendo más. ¡Todos comieron hasta quedar satisfechos!",
            "Cuando terminaron, los discípulos recogieron las sobras: ¡doce canastas llenas! De cinco panes y dos pescados, Jesús alimentó a miles de personas.",
        ],
        "lesson": "Si compartes lo poco que tienes, Dios lo multiplica.",
        "activity": "Cuenta: 5 panes + 2 peces = comida para 5000 personas. ¡Eso es un milagro!",
    },
    {
        "title": "El Buen Samaritano",
        "bible_ref": "Lucas 10:25-37",
        "paragraphs": [
            "Jesús contó esta historia para enseñar quién es nuestro prójimo. Un hombre viajaba por un camino peligroso cuando unos ladrones lo atacaron.",
            "Lo golpearon, le quitaron todo y lo dejaron tirado en el camino, muy herido. El pobre hombre no podía moverse.",
            "Pasó un sacerdote por el mismo camino. Vio al hombre herido, pero cruzó al otro lado y siguió caminando sin ayudarlo.",
            "Luego pasó otro hombre importante del templo. También vio al herido, pero también lo ignoró y siguió su camino.",
            "Finalmente pasó un samaritano, alguien que los demás despreciaban. Pero él sí se detuvo. Curó las heridas del hombre, lo subió a su burro y lo llevó a una posada.",
            "El samaritano pagó para que cuidaran al hombre herido. Jesús preguntó: \"¿Quién fue el verdadero amigo?\" La respuesta era clara: el que ayudó.",
        ],
        "lesson": "Debemos ayudar a todos los que necesiten, sin importar quiénes sean.",
        "activity": "¿Cómo puedes ser un buen samaritano esta semana?",
    },
    {
        "title": "El Hijo Pródigo",
        "bible_ref": "Lucas 15:11-32",
        "paragraphs": [
            "Un padre tenía dos hijos. El menor le dijo: \"Papá, dame mi parte de la herencia.\" El padre, con tristeza, se la dio.",
            "El hijo se fue lejos y gastó todo el dinero en fiestas. Vivía como un rey, pero pronto se quedó sin nada.",
            "Sin dinero y sin amigos, el joven tuvo que trabajar cuidando cerdos. Tenía tanta hambre que quería comer la comida de los cerdos.",
            "Entonces pensó: \"Los trabajadores de mi padre comen mejor que yo. Volveré y le pediré perdón.\" Se levantó y empezó a caminar de regreso.",
            "Cuando estaba todavía lejos, su padre lo vio. ¡Corrió hacia él, lo abrazó y lo llenó de besos! No estaba enojado, ¡estaba feliz!",
            "El padre hizo una gran fiesta. \"¡Mi hijo estaba perdido y ha vuelto!\" dijo. Le puso ropa nueva, un anillo y zapatos. Así es el amor de Dios por nosotros.",
        ],
        "lesson": "Dios siempre nos espera con los brazos abiertos, sin importar lo que hayamos hecho.",
        "activity": "Dibuja al padre abrazando a su hijo. ¿Cómo crees que se sentían?",
    },
    {
        "title": "Rut y Noemí",
        "bible_ref": "Rut 1-4",
        "paragraphs": [
            "Noemí era una mujer israelita que vivía en un país lejano con su familia. Tristemente, su esposo y sus dos hijos murieron.",
            "Noemí decidió volver a su tierra, Israel. Le dijo a sus nueras: \"Vuelvan con sus familias.\" Orfa se despidió llorando, pero Rut no quiso irse.",
            "Rut le dijo a Noemí: \"Donde tú vayas, yo iré. Tu pueblo será mi pueblo, y tu Dios será mi Dios.\" Fue una promesa hermosa.",
            "Juntas llegaron a Belén. Eran muy pobres, así que Rut iba a los campos a recoger el trigo que los trabajadores dejaban caer.",
            "El dueño del campo se llamaba Booz. Era un hombre bueno y generoso. Vio lo trabajadora que era Rut y cómo cuidaba a Noemí. Se enamoró de ella.",
            "Booz y Rut se casaron y tuvieron un hijo llamado Obed. ¡Obed fue el abuelo del rey David! Dios premió la lealtad y el amor de Rut.",
        ],
        "lesson": "La lealtad y el amor verdadero siempre son recompensados por Dios.",
        "activity": "¿A quién eres leal tú? Escribe el nombre de alguien que siempre cuidas.",
    },
    {
        "title": "Ester, la Reina Valiente",
        "bible_ref": "Ester 1-10",
        "paragraphs": [
            "Ester era una joven judía muy hermosa que vivía con su primo Mardoqueo. El rey de Persia la eligió como reina por su belleza y bondad.",
            "Un hombre malvado llamado Amán odiaba al pueblo judío. Convenció al rey de hacer una ley terrible para destruir a todos los judíos.",
            "Mardoqueo le pidió ayuda a Ester: \"Tal vez Dios te hizo reina para este momento.\" Pero hablar con el rey sin ser invitada era muy peligroso.",
            "Ester tuvo mucho miedo, pero fue valiente. Le pidió a todos que oraran durante tres días. Luego se vistió con sus mejores ropas y fue ante el rey.",
            "El rey la recibió con cariño. Ester preparó una cena especial y allí reveló la verdad: \"Amán quiere destruir a mi pueblo. ¡Yo también soy judía!\"",
            "El rey se enfureció con Amán y salvó al pueblo judío. Ester, con su valentía, salvó a miles de personas. Hasta hoy se celebra la fiesta de Purim en su honor.",
        ],
        "lesson": "Dios puede ponerte en el lugar correcto para ayudar a otros. ¡Sé valiente!",
        "activity": "Si fueras rey o reina por un día, ¿qué ley harías para ayudar a los demás?",
    },
    {
        "title": "Sansón, el Hombre más Fuerte",
        "bible_ref": "Jueces 13-16",
        "paragraphs": [
            "Antes de que Sansón naciera, un ángel visitó a sus padres. Les dijo que su hijo sería especial y que nunca debía cortarse el cabello.",
            "Sansón creció y se convirtió en el hombre más fuerte del mundo. ¡Podía derrotar a un león con sus manos! Su fuerza venía de Dios.",
            "Sansón hizo muchas hazañas increíbles. Derrotó a mil enemigos él solo. Arrancó las puertas de una ciudad y las cargó en sus hombros.",
            "Pero Sansón no siempre tomó buenas decisiones. Una mujer llamada Dalila lo engañó y descubrió el secreto de su fuerza: su cabello.",
            "Mientras dormía, Dalila le cortó el cabello. Sansón perdió su fuerza y sus enemigos lo capturaron. Estaba triste y arrepentido.",
            "Pero su cabello volvió a crecer. Sansón oró a Dios una última vez, y Dios le devolvió su fuerza. Sansón aprendió que la verdadera fuerza viene de confiar en Dios.",
        ],
        "lesson": "La verdadera fuerza no está en los músculos, sino en confiar en Dios.",
        "activity": "¿Cuál es tu superpoder? Dibújate con un poder especial que Dios te dio.",
    },
    {
        "title": "La Torre de Babel",
        "bible_ref": "Génesis 11:1-9",
        "paragraphs": [
            "Después del diluvio, todas las personas hablaban el mismo idioma. Podían entenderse perfectamente.",
            "Un día, las personas tuvieron una idea orgullosa: \"¡Construyamos una torre tan alta que llegue al cielo! Así seremos famosos.\"",
            "Empezaron a hacer ladrillos y a construir. La torre crecía y crecía. Pero su intención no era buena: querían ser como Dios.",
            "Dios vio lo que hacían y decidió confundir sus idiomas. De repente, unos hablaban de una forma y otros de otra. ¡Nadie se entendía!",
            "\"¿Qué dices?\" \"¡No te entiendo!\" La construcción se detuvo porque no podían comunicarse. Era un gran desorden.",
            "Las personas se separaron en grupos según su idioma y se fueron a vivir a diferentes partes del mundo. Por eso hoy hay tantos idiomas diferentes.",
        ],
        "lesson": "El orgullo nos separa. La humildad nos une con Dios y con los demás.",
        "activity": "¿Cuántos idiomas conoces? Escribe \"hola\" en todos los que sepas.",
    },
    {
        "title": "José y sus Hermanos",
        "bible_ref": "Génesis 37-45",
        "paragraphs": [
            "José era el hijo favorito de su padre Jacob. Jacob le regaló una túnica de muchos colores. Sus hermanos estaban muy celosos.",
            "José tenía sueños especiales donde veía que un día su familia se inclinaría ante él. Cuando les contó, sus hermanos se enojaron aún más.",
            "Un día, los hermanos lo vendieron como esclavo. Le dijeron a su padre que un animal lo había atacado. Jacob lloró mucho.",
            "José llegó a Egipto como esclavo, pero Dios estaba con él. Aunque pasó por momentos muy difíciles, incluso en la cárcel, nunca perdió la fe.",
            "Dios le dio a José la habilidad de interpretar sueños. El faraón lo llamó y José interpretó su sueño: vendrían siete años de abundancia y siete de hambre. El faraón lo puso a cargo de todo Egipto.",
            "Cuando la hambruna llegó, los hermanos de José fueron a Egipto a buscar comida. ¡José los reconoció! En vez de castigarlos, los perdonó y abrazó llorando de alegría.",
        ],
        "lesson": "El perdón es más poderoso que la venganza. Dios puede cambiar lo malo en algo bueno.",
        "activity": "Dibuja la túnica de colores de José. ¡Usa todos los colores que tengas!",
    },
    {
        "title": "El Paso del Mar Rojo",
        "bible_ref": "Éxodo 14",
        "paragraphs": [
            "Moisés sacó al pueblo de Israel de Egipto. ¡Por fin eran libres! Pero el faraón cambió de opinión y envió a su ejército a perseguirlos.",
            "Los israelitas llegaron al Mar Rojo. Delante, el mar. Detrás, los soldados de Egipto. No había escape. El pueblo tenía mucho miedo.",
            "Pero Moisés les dijo: \"¡No tengan miedo! Quédense quietos y verán cómo Dios los salva hoy.\"",
            "Moisés extendió su mano sobre el mar. ¡Y un viento fuerte separó las aguas en dos! A la derecha, una pared de agua. A la izquierda, otra. En medio, ¡un camino seco!",
            "Todo el pueblo cruzó caminando por en medio del mar. Hombres, mujeres, niños y animales pasaron por el camino seco.",
            "Cuando el ejército del faraón intentó seguirlos, las aguas volvieron a su lugar. El pueblo de Israel estaba a salvo al otro lado. Todos cantaron y dieron gracias a Dios.",
        ],
        "lesson": "Cuando parece que no hay salida, Dios abre un camino.",
        "activity": "Dibuja el mar separado en dos con el pueblo caminando en medio.",
    },
    {
        "title": "Jesús y los Niños",
        "bible_ref": "Marcos 10:13-16",
        "paragraphs": [
            "Muchas personas traían a sus niños para que Jesús los bendijera. Querían que el Maestro los tocara y orara por ellos.",
            "Pero los discípulos les decían: \"¡No molesten al Maestro! Él está muy ocupado para atender niños.\" E impedían que los niños se acercaran.",
            "Cuando Jesús vio esto, se enojó con sus discípulos. \"¡Dejen que los niños vengan a mí!\" les dijo con voz firme.",
            "\"No se lo impidan, porque el reino de Dios es de los que son como niños,\" explicó Jesús.",
            "Jesús tomó a los niños en sus brazos, los abrazó con cariño, puso sus manos sobre ellos y los bendijo uno por uno.",
            "Ese día todos aprendieron algo importante: para Jesús, los niños son muy especiales. No hay nadie demasiado pequeño ni poco importante para Él.",
        ],
        "lesson": "Tú eres muy importante para Jesús. Él siempre tiene tiempo para ti.",
        "activity": "Haz un dibujo de ti mismo con Jesús. ¿Qué le dirías?",
    },
    {
        "title": "La Parábola de la Oveja Perdida",
        "bible_ref": "Lucas 15:1-7",
        "paragraphs": [
            "Jesús contó esta historia para mostrar cuánto nos ama Dios. Un pastor tenía cien ovejas y las cuidaba con mucho amor.",
            "Una noche, al contarlas, se dio cuenta de que faltaba una. Solo tenía noventa y nueve. ¡Una ovejita se había perdido!",
            "El pastor no dijo: \"Bueno, tengo noventa y nueve, eso es suficiente.\" No. Dejó a las noventa y nueve seguras y salió a buscar a la perdida.",
            "Buscó por montañas, valles y ríos. Llamaba a su ovejita mientras caminaba en la oscuridad. No iba a parar hasta encontrarla.",
            "¡Por fin la encontró! La ovejita estaba asustada y temblando. El pastor la cargó sobre sus hombros, feliz, y la llevó de vuelta a casa.",
            "\"Así es Dios,\" dijo Jesús. \"Hay más alegría en el cielo por una persona que regresa a Dios que por noventa y nueve que no se perdieron.\"",
        ],
        "lesson": "Dios nunca deja de buscarte. Eres tan importante que Él daría todo por ti.",
        "activity": "Cuenta hasta 100. Ahora imagina que falta uno. ¿Lo buscarías?",
    },
    {
        "title": "Zaqueo, el Hombre Pequeñito",
        "bible_ref": "Lucas 19:1-10",
        "paragraphs": [
            "Zaqueo vivía en Jericó. Era un hombre muy rico porque cobraba impuestos, pero les quitaba dinero de más a las personas. Nadie lo quería.",
            "Un día, Jesús pasó por Jericó. Mucha gente salió a verlo. Zaqueo también quería ver a Jesús, pero había un problema: ¡era muy bajito!",
            "Zaqueo no podía ver nada entre tanta gente alta. Entonces tuvo una idea: ¡se subió a un árbol! Desde arriba podría ver a Jesús perfectamente.",
            "Cuando Jesús pasó debajo del árbol, miró hacia arriba y dijo: \"¡Zaqueo! Baja rápido, porque hoy quiero ir a tu casa.\"",
            "Zaqueo no podía creerlo. ¡Jesús quería visitarlo a él! Bajó del árbol a toda velocidad, lleno de alegría.",
            "Ese día, Zaqueo cambió completamente. Dijo: \"Señor, daré la mitad de mis bienes a los pobres, y a los que les quité de más, les devolveré cuatro veces.\" Jesús sonrió: \"Hoy la salvación ha llegado a esta casa.\"",
        ],
        "lesson": "Jesús puede cambiar el corazón de cualquier persona. Nunca es tarde para hacer lo correcto.",
        "activity": "¿Qué harías si pudieras devolver algo bueno a alguien?",
    },
    {
        "title": "La Última Cena",
        "bible_ref": "Lucas 22:7-20",
        "paragraphs": [
            "Era la noche antes de que Jesús fuera arrestado. Él lo sabía, y quería pasar esa noche especial con sus mejores amigos, los doce discípulos.",
            "Prepararon una cena en un cuarto grande. Antes de comer, Jesús hizo algo que sorprendió a todos: se arrodilló y lavó los pies de cada discípulo.",
            "\"Pero Señor, tú eres el Maestro. ¡No deberías lavar nuestros pies!\" dijo Pedro. Jesús respondió: \"Les doy este ejemplo para que sirvan a los demás.\"",
            "Durante la cena, Jesús tomó el pan, dio gracias a Dios y lo partió. \"Este es mi cuerpo, que se entrega por ustedes,\" dijo, dándole un pedazo a cada uno.",
            "Luego tomó la copa de vino y dijo: \"Esta copa es mi sangre, que se derrama para el perdón de los pecados. Hagan esto para recordarme.\"",
            "Esa noche, Jesús les enseñó a sus amigos la lección más importante: el verdadero líder es el que sirve a los demás con amor.",
        ],
        "lesson": "Servir a los demás con amor es lo que nos hace grandes.",
        "activity": "¿Cómo puedes servir a alguien en tu familia esta semana?",
    },
    {
        "title": "La Resurrección de Jesús",
        "bible_ref": "Mateo 28:1-10",
        "paragraphs": [
            "Después de que Jesús murió en la cruz, sus amigos lo pusieron en una tumba cavada en la roca. Pusieron una piedra enorme en la entrada.",
            "Todos estaban muy tristes. Pensaban que todo había terminado. Los discípulos se escondieron con miedo.",
            "Al tercer día, muy temprano en la mañana, María Magdalena y otras mujeres fueron a la tumba con perfumes para honrar a Jesús.",
            "Cuando llegaron, ¡la piedra estaba movida! Un ángel vestido de blanco brillante estaba sentado allí. Las mujeres se asustaron mucho.",
            "El ángel les dijo: \"¡No tengan miedo! Buscan a Jesús, pero Él no está aquí. ¡Ha resucitado! Vayan a decirles a los discípulos.\"",
            "Las mujeres corrieron llenas de alegría. Y entonces... ¡Jesús mismo apareció frente a ellas! \"¡No teman!\" dijo, sonriendo. Jesús había vencido a la muerte. ¡Estaba vivo!",
        ],
        "lesson": "Jesús venció a la muerte. Con Él, siempre hay esperanza.",
        "activity": "Dibuja la tumba vacía con el ángel y el sol saliendo. ¡Jesús vive!",
    },
    {
        "title": "Noé y el Arcoíris de la Promesa",
        "bible_ref": "Génesis 9:8-17",
        "paragraphs": [
            "Después del gran diluvio, Noé y su familia salieron del arca. Los animales corrieron libres por la tierra nueva y limpia.",
            "Lo primero que hizo Noé fue construir un altar y dar gracias a Dios por haberlos salvado. Dios se alegró mucho.",
            "Entonces Dios hizo una promesa muy especial. Le dijo a Noé: \"Nunca más destruiré la tierra con un diluvio. Esta es mi promesa para ti y para todos los seres vivos.\"",
            "\"Y para que recuerden mi promesa,\" dijo Dios, \"pondré mi arcoíris en las nubes. Cada vez que lo vean, recuerden que yo cumplo mis promesas.\"",
            "Un hermoso arcoíris apareció en el cielo, con todos sus colores: rojo, naranja, amarillo, verde, azul y violeta. Era la señal del amor de Dios.",
            "Desde ese día, cada vez que vemos un arcoíris después de la lluvia, podemos recordar que Dios nos ama y que siempre cumple sus promesas.",
        ],
        "lesson": "Cada arcoíris es un recordatorio del amor y las promesas de Dios.",
        "activity": "La próxima vez que veas un arcoíris, ¡recuerda esta historia!",
    },
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
    c.drawCentredString(w/2, h/2 + 1.8*inch, "HISTORIAS")

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 32)
    c.drawCentredString(w/2, h/2 + 1.1*inch, "BÍBLICAS")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(w/2, h/2 + 0.4*inch, "ILUSTRADAS")

    c.setFillColor(BLUE_LIGHT)
    c.setFont("Helvetica", 16)
    c.drawCentredString(w/2, h/2 - 0.3*inch, "25 Historias · Para Leer y Colorear")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, h/2 - 1.0*inch, "¡Lee, aprende y diviértete!")

    c.setFillColor(GRAY_LIGHT)
    c.setFont("Helvetica", 11)
    c.drawCentredString(w/2, 1.5*inch, "Para niños de 4 a 10 años")

    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(w/2, 0.8*inch, "www.kitbiblicoinfantil.com")


def draw_toc(c, w, h):
    c.setFillColor(BLUE_BG)
    c.rect(0, 0, w, h, fill=1)

    c.setFillColor(BLUE_DARK)
    c.rect(0, h - 0.7*inch, w, 0.7*inch, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(w/2, h - 0.45*inch, "ÍNDICE DE HISTORIAS")

    y = h - 1.2*inch
    left_x = 0.8*inch
    right_x = w - 0.8*inch

    for i, story in enumerate(STORIES):
        if y < 1.0*inch:
            break
        num = i + 1
        c.setFillColor(BLUE_DARK)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(left_x, y, f"{num}.")
        c.setFont("Helvetica", 10)
        c.drawString(left_x + 0.3*inch, y, story["title"])
        c.setFont("Helvetica", 9)
        c.setFillColor(AMBER)
        c.drawRightString(right_x, y, story["bible_ref"])
        y -= 0.32*inch

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w/2, 0.35*inch, "Mega Kit Bíblico Infantil — Historias Bíblicas Ilustradas")


def wrap_text(text, font_name, font_size, max_width, c_obj):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = f"{current_line} {word}".strip()
        if c_obj.stringWidth(test_line, font_name, font_size) <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines


def draw_story_page(c, w, h, story, page_num):
    c.setFillColor(BLUE_BG)
    c.rect(0, 0, w, h, fill=1)

    c.setFillColor(BLUE_DARK)
    c.rect(0, h - 0.7*inch, w, 0.7*inch, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    title = story["title"]
    if len(title) > 35:
        c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(w/2, h - 0.42*inch, title)

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 9)
    c.drawRightString(w - 0.4*inch, h - 0.42*inch, f"Historia {page_num}")
    c.drawString(0.4*inch, h - 0.42*inch, story["bible_ref"])

    margin = 0.7*inch
    text_width = w - 2 * margin
    y = h - 1.1*inch

    for para in story["paragraphs"]:
        c.setFillColor(TEXT_COLOR)
        c.setFont("Helvetica", 10)
        lines = wrap_text(para, "Helvetica", 10, text_width, c)
        for line in lines:
            if y < 2.0*inch:
                break
            c.drawString(margin, y, line)
            y -= 14
        y -= 6

    lesson_y = 1.7*inch
    c.setFillColor(BLUE_MED)
    c.roundRect(margin - 0.1*inch, lesson_y - 0.15*inch, text_width + 0.2*inch, 0.55*inch, 5, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(margin + 0.05*inch, lesson_y + 0.2*inch, "Enseñanza:")
    c.setFont("Helvetica", 9)
    lesson_lines = wrap_text(story["lesson"], "Helvetica", 9, text_width - 0.1*inch, c)
    ly = lesson_y + 0.03*inch
    for ll in lesson_lines:
        c.drawString(margin + 0.05*inch, ly, ll)
        ly -= 12

    act_y = 1.15*inch
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(margin, act_y, "Actividad:")
    c.setFillColor(TEXT_COLOR)
    c.setFont("Helvetica", 9)
    act_lines = wrap_text(story["activity"], "Helvetica", 9, text_width - 0.8*inch, c)
    ax = margin + c.stringWidth("Actividad: ", "Helvetica-Bold", 9)
    for al in act_lines:
        c.drawString(ax, act_y, al)
        act_y -= 12
        ax = margin

    c.setFillColor(AMBER)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w/2, 0.35*inch, "Mega Kit Bíblico Infantil — Historias Bíblicas Ilustradas")


def main():
    w, h = letter
    c = canvas.Canvas(OUTPUT_PATH, pagesize=letter)

    draw_cover(c, w, h)
    c.showPage()

    draw_toc(c, w, h)
    c.showPage()

    for i, story in enumerate(STORIES):
        print(f"  Historia {i+1}/25: {story['title']}")
        draw_story_page(c, w, h, story, i + 1)
        c.showPage()

    c.save()
    print(f"\n PDF generado: {OUTPUT_PATH}")
    print(f" Total: {len(STORIES)} historias bíblicas")


if __name__ == "__main__":
    main()
