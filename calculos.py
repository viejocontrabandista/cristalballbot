import json
import os

# Cargar datos numerológicos
with open('numerologia_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

tabla = data['tabla_letras']
significados = data['significados']

HISTORIAL_FILE = 'historial.json'

def reducir_numero(n):
    while n > 9 and n not in [11, 22]:
        n = sum(int(d) for d in str(n))
    return n

def numero_vida(fecha_str: str) -> int:
    dia, mes, año = map(int, fecha_str.split('/'))
    return reducir_numero(dia + mes + año)

def numero_destino(nombre: str) -> int:
    nombre = nombre.upper().replace(" ", "")
    suma = sum(tabla.get(letra, 0) for letra in nombre)
    return reducir_numero(suma)

def porcentaje_afinidad(num1: int, num2: int) -> int:
    if num1 == num2:
        return 95
    pares_alta = [(1,3),(1,5),(1,9),(2,4),(2,6),(2,8),(3,1),(3,5),(3,9),
                  (4,2),(4,6),(4,8),(5,1),(5,3),(5,9),(6,2),(6,4),(6,9),
                  (7,7),(9,1),(9,3),(9,5),(9,6)]
    if (num1, num2) in pares_alta or (num2, num1) in pares_alta:
        return 85
    if num1 in [11,22] or num2 in [11,22]:
        return 75
    return 50

import json
import os

# Cargar datos numerológicos
with open('numerologia_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

tabla = data['tabla_letras']
significados = data['significados']

HISTORIAL_FILE = 'historial.json'

def reducir_numero(n):
    while n > 9 and n not in [11, 22]:
        n = sum(int(d) for d in str(n))
    return n

def numero_vida(fecha_str: str) -> int:
    dia, mes, año = map(int, fecha_str.split('/'))
    return reducir_numero(dia + mes + año)

def numero_destino(nombre: str) -> int:
    nombre = nombre.upper().replace(" ", "")
    suma = sum(tabla.get(letra, 0) for letra in nombre)
    return reducir_numero(suma)

def porcentaje_afinidad(num1: int, num2: int) -> int:
    if num1 == num2:
        return 95
    pares_alta = [(1,3),(1,5),(1,9),(2,4),(2,6),(2,8),(3,1),(3,5),(3,9),
                  (4,2),(4,6),(4,8),(5,1),(5,3),(5,9),(6,2),(6,4),(6,9),
                  (7,7),(9,1),(9,3),(9,5),(9,6)]
    if (num1, num2) in pares_alta or (num2, num1) in pares_alta:
        return 85
    if num1 in [11,22] or num2 in [11,22]:
        return 75
    return 50

def generar_reporte(nombre: str, fecha: str, nombre_pareja: str = None, fecha_pareja: str = None) -> str:
    nv = numero_vida(fecha)
    nd = numero_destino(nombre)
    texto = f"🔮 *Estudio Numerológico para {nombre.upper()}*\n\n"
    texto += f"• Número de Vida: *{nv}*\n{significados[str(nv)]}\n\n"
    texto += f"• Número de Destino: *{nd}*\n{significados[str(nd)]}\n\n"
    
    if nombre_pareja and fecha_pareja:
        nv2 = numero_vida(fecha_pareja)
        porc = porcentaje_afinidad(nv, nv2)
        texto += f"💞 *Compatibilidad con {nombre_pareja.upper()}*\n"
        texto += f"Su Número de Vida: *{nv2}* | Tuyo: *{nv}*\n"
        texto += f"Afinidad energética: *{porc}%*\n"
        if porc >= 80:
            texto += "Excelente armonía, gran potencial juntos ✨\n"
        elif porc >= 60:
            texto += "Buena compatibilidad, fluye con esfuerzo ❤️\n"
        else:
            texto += "Desafíos presentes, pero gran crecimiento espiritual 🌱\n"
    
    return texto

def consulta_existe(nombre: str, fecha: str, nombre_pareja: str = None, fecha_pareja: str = None) -> bool:
    if not os.path.exists(HISTORIAL_FILE):
        return False
    with open(HISTORIAL_FILE, 'r', encoding='utf-8') as f:
        historial = json.load(f)
    
    clave = f"{nombre.upper()}_{fecha}"
    if nombre_pareja:
        clave += f"_{nombre_pareja.upper()}_{fecha_pareja or ''}"
    
    for entrada in historial:
        clave_exist = f"{entrada['nombre'].upper()}_{entrada['fecha']}"
        if entrada.get('nombre_pareja'):
            clave_exist += f"_{entrada['nombre_pareja'].upper()}_{entrada.get('fecha_pareja', '')}"
        if clave == clave_exist:
            return True
    return False

def guardar_consulta(nombre: str, fecha: str, nombre_pareja: str = None, fecha_pareja: str = None, reporte: str = None):
    if not os.path.exists(HISTORIAL_FILE):
        with open(HISTORIAL_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f)
    
    with open(HISTORIAL_FILE, 'r', encoding='utf-8') as f:
        historial = json.load(f)
    
    historial.append({
        "nombre": nombre,
        "fecha": fecha,
        "nombre_pareja": nombre_pareja,
        "fecha_pareja": fecha_pareja,
        "reporte": reporte
    })
    
    with open(HISTORIAL_FILE, 'w', encoding='utf-8') as f:
        json.dump(historial, f, ensure_ascii=False, indent=4)
def generar_cold_reading(genero: str = None, consulta: str = None) -> str:
    import random  # Import local para evitar problemas

    frases = [
        "Siento que estás en un momento de gran claridad interna. Las respuestas que buscabas están empezando a llegar solas.",
        "Tienes un don natural para conectar con las personas. Tu presencia calma e inspira a quienes te rodean.",
        "El universo te está preparando para un cambio positivo que llegará cuando menos lo esperes.",
        "Tu energía creativa está en ascenso. Pronto verás cómo tus ideas toman forma con facilidad.",
        "Hay una sincronía especial alineándose en tu vida. Confía en las señales que estás recibiendo.",
        "Eres más fuerte de lo que crees. Lo que superaste en el pasado te convirtió en quien eres hoy.",
        "Tu intuición está más afinada que nunca. Escucharla te llevará exactamente a donde debes estar.",
        "Se acerca un período de abundancia en el área que más deseas. Solo mantén la fe.",
        "Tienes un talento único que el mundo necesita. Cuando lo compartas, todo fluirá mejor.",
        "Las personas correctas están entrando en tu vida en el momento perfecto.",
        "Estás aprendiendo a soltar lo que no te sirve, y eso abre espacio para cosas maravillosas.",
        "Tu corazón sabe el camino. Cuando lo sigas sin miedo, todo se alineará.",
        "Hay una versión de ti más libre y feliz esperando ser expresada. Ya casi es hora.",
        "Tu capacidad para ver lo bueno en los demás es un superpoder que te devuelve bendiciones.",
        "El esfuerzo silencioso que estás haciendo ahora dará frutos visibles muy pronto.",
        "Tu luz interior es más brillante de lo que imaginas. Otros la ven aunque tú no siempre.",
        "Estás atrayendo oportunidades que resuenan con tu verdadero propósito.",
        "Cada paso que das, aunque pequeño, te acerca a la versión más plena de ti mismo/a.",
        "Tu sonrisa y energía positiva son contagiosas. Impactas más de lo que crees.",
        "El universo te está guiñando el ojo con pequeñas coincidencias. Presta atención.",
        "Tienes una sabiduría natural que guía tus decisiones mejor de lo que piensas.",
        "Se acerca un momento de reconocimiento por tu esfuerzo constante.",
        "Tu capacidad para adaptarte es una de tus mayores fortalezas.",
        "Estás rodeado/a de protección y guía, aunque no siempre la veas.",
        "Tu autenticidad atrae relaciones genuinas y profundas.",
        "Pronto experimentarás un 'click' interno que aclarará muchas cosas.",
        "Tu generosidad siempre regresa multiplicada, de formas inesperadas.",
        "Estás en el camino correcto. La paciencia te revelará la magia.",
        "Tu curiosidad y ganas de aprender abren puertas constantemente.",
        "Hay una paz interior creciendo en ti que nada externo podrá alterar.",
        "Tu presencia aporta calma y equilibrio a cualquier entorno.",
        "El amor (propio y ajeno) fluye hacia ti cuando te permites recibirlo.",
        "Tu resiliencia es admirable. Lo que no te rompe, te hace brillar más.",
        "Estás atrayendo experiencias que te harán sentir vivo/a y conectado/a.",
        "Tu voz interior tiene razón más veces de las que dudas.",
        "El futuro te reserva sorpresas agradables si mantienes el corazón abierto.",
        "Tu capacidad para encontrar belleza en lo cotidiano es un regalo raro.",
        "Estás evolucionando a un nivel superior sin darte cuenta.",
        "Tu energía positiva está creando un efecto dominó de cosas buenas.",
        "Pronto dirás 'valió la pena esperar' por algo importante.",
        "Tu empatía te convierte en un apoyo invaluable para quienes te rodean.",
        "El universo conspira a tu favor cuando actúas con autenticidad.",
        "Tu potencial es ilimitado cuando confías en tu proceso.",
        "Estás a punto de recibir una confirmación que te llenará de paz.",
        "Tu luz guía a otros sin que lo busques. Eso es magia pura.",
        "Todo lo que necesitas para el siguiente paso ya está dentro de ti.",
        "Tu camino se ilumina cada vez que das un paso con fe.",
        "La abundancia te encuentra cuando vives alineado/a con tu esencia.",
        "Tu historia inspira a otros más de lo que imaginas.",
        "Estás exactamente donde debes estar para lo que viene.",
        "Tu futuro brilla con posibilidades que aún no ves del todo."
    ]

    random.shuffle(frases)
    seleccion = frases[:random.randint(3, 6)]

    extra = ""
    if consulta:
        if 'amor' in consulta.lower():
            extra = "En el amor, se acerca una conexión auténtica y nutritiva.\n"
        elif 'trabajo' in consulta.lower():
            extra = "En lo laboral, tu esfuerzo será reconocido y recompensado pronto.\n"
        elif 'dinero' in consulta.lower():
            extra = "El flujo financiero mejora cuando confías en tu valor y creatividad.\n"
        elif 'salud' in consulta.lower():
            extra = "Tu cuerpo y mente responden bien al cuidado amoroso que te des.\n"

    return extra + "\n".join(seleccion)