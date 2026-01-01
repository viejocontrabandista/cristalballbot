import json
from datetime import datetime

# Cargar datos
with open('numerologia_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

tabla = data['tabla_letras']
significados = data['significados']

def reducir_numero(n):
    while n > 9 and n not in [11, 22]:
        n = sum(int(d) for d in str(n))
    return n

def numero_vida(fecha_str):
    # Formato DD/MM/AAAA
    dia, mes, año = map(int, fecha_str.split('/'))
    suma = dia + mes + año
    return reducir_numero(suma)

# Prueba rápida
fecha = "31/12/1990"  # Cambia por una fecha para probar
num = numero_vida(fecha)
print(f"Número de Vida: {num}")
print(f"Significado: {significados[str(num)]}")
def numero_destino(nombre):
    nombre = nombre.upper().replace(" ", "")  # Quita espacios y mayúsculas
    suma = 0
    for letra in nombre:
        if letra in tabla:
            suma += tabla[letra]
    return reducir_numero(suma)

# Prueba con ambos
fecha = "31/12/1990"
nombre = "Juan Pérez"  # Cambia por cualquier nombre para probar

num_vida = numero_vida(fecha)
num_destino = numero_destino(nombre)

print(f"Número de Vida: {num_vida} → {significados[str(num_vida)]}")
print(f"Número de Destino: {num_destino} → {significados[str(num_destino)]}")
def porcentaje_afinidad(num1, num2):
    if num1 == num2:
        return 95  # Mismo número: alta afinidad
    pares_alta = [(1,3),(1,5),(1,9),(2,4),(2,6),(2,8),(3,1),(3,5),(3,9),
                  (4,2),(4,6),(4,8),(5,1),(5,3),(5,9),(6,2),(6,4),(6,9),
                  (7,7),(9,1),(9,3),(9,5),(9,6)]
    if (num1, num2) in pares_alta or (num2, num1) in pares_alta:
        return 85
    if num1 in [11,22] or num2 in [11,22]:
        return 75  # Maestros: media-alta
    return 50  # Default media-baja

# Prueba compatibilidad
num1 = num_vida  # 8
num2 = num_destino  # 3 (simulando pareja)

porc = porcentaje_afinidad(num1, num2)
print(f"\nAfinidad entre {num1} y {num2}: {porc}%")
def generar_reporte(nombre, fecha, nombre_pareja=None, fecha_pareja=None):
    nv = numero_vida(fecha)
    nd = numero_destino(nombre)
    texto = f"🔮 Estudio Numerológico para {nombre.upper()}\n\n"
    texto += f"Número de Vida: {nv}\n{significados[str(nv)]}\n\n"
    texto += f"Número de Destino: {nd}\n{significados[str(nd)]}\n\n"
    
    if nombre_pareja and fecha_pareja:
        nv2 = numero_vida(fecha_pareja)
        nd2 = numero_destino(nombre_pareja)
        porc = porcentaje_afinidad(nv, nv2)  # Usamos Vida vs Vida (puedes cambiar)
        texto += f"Compatibilidad con {nombre_pareja.upper()}:\n"
        texto += f"Su Número de Vida: {nv2} | Tú: {nv}\n"
        texto += f"Afinidad energética: {porc}%\n"
        if porc >= 80:
            texto += "Excelente armonía, gran potencial juntos."
        elif porc >= 60:
            texto += "Buena compatibilidad, con esfuerzo fluye bien."
        else:
            texto += "Desafíos presentes, pero oportunidades de crecimiento."
    
    return texto

# Prueba
reporte = generar_reporte("Juan Pérez", "31/12/1990", "María Gómez", "15/05/1988")
print(reporte)
import os

HISTORIAL_FILE = 'historial.json'

def guardar_consulta(nombre, fecha, nombre_pareja=None, fecha_pareja=None, reporte=None):
    if not os.path.exists(HISTORIAL_FILE):
        with open(HISTORIAL_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f)
    
    with open(HISTORIAL_FILE, 'r', encoding='utf-8') as f:
        historial = json.load(f)
    
    entrada = {
        "nombre": nombre,
        "fecha": fecha,
        "nombre_pareja": nombre_pareja,
        "fecha_pareja": fecha_pareja,
        "reporte": reporte
    }
    historial.append(entrada)
    
    with open(HISTORIAL_FILE, 'w', encoding='utf-8') as f:
        json.dump(historial, f, ensure_ascii=False, indent=4)

# Prueba guardando el reporte anterior
guardar_consulta("Juan Pérez", "31/12/1990", "María Gómez", "15/05/1988", reporte)
print("Consulta guardada en historial.json")