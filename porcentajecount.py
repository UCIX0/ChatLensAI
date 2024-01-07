import re

# Detecta el patron de un mensaje en formato 12hrs
pattern = r"(\d{1,2}/\d{1,2}/\d{4}),\s(\d{1,2}:\d{2}\s[ap]\.\s?m\.)\s-\s(\+?\d*\s?\(?\d{3}\)?\s?\d{3}-\d{4}|[^:]+):\s(.*)"
# Detecta el patron de un mensaje en formato 24hrs
pattern2 = r"(\d{1,2}/\d{1,2}/\d{4}),\s((?:[01]?\d|2[0-3]):[0-5]\d)\s-\s(\+?\d*\s?\(?\d{3}\)?\s?\d{3}-\d{4}|[^:]+):\s(.*)"

def calcular_porcentaje(archivo):
	"""
	cuenta el numero de lineas que sigue el patron dado, y devuelve el porcentaje que sigue este patron
	"""
	total_lineas = 0
	lineas_validas = 0

	with open(archivo, 'r', encoding='utf-8') as file:
		for line in file:
			total_lineas += 1
			if re.match(pattern, line) or re.match(pattern2, line):
				lineas_validas += 1
	if total_lineas == 0:
		return 0
	# Calcular el porcentaje de líneas que siguen la estructura
	porcentaje = (lineas_validas / total_lineas) * 100
	return porcentaje

# Ruta del archivo en la carpeta específica
ruta_archivo = 'chatix.txt'


porcentaje = calcular_porcentaje(ruta_archivo)
print(f'El {porcentaje:.2f}% de las líneas sigue la estructura especificada.')