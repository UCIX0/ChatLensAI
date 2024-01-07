import re
import os

# Define la expresión regular de mensajes del sistema en formato 12hrs
sys_mess = r"(\d{1,2}/\d{1,2}/\d{4}),\s(\d{1,2}:\d{2}\s[ap]\.\s?m\.)\s-\s(?!.*:)"
# Define la expresión regular de mensajes del sistema en formato 24hrs
sys_mess2 = r"(\d{1,2}/\d{1,2}/\d{4}),\s((?:[01]?\d|2[0-3]):[0-5]\d)\s-\s(?!.*:)"

def filtrar_y_escribir(archivo):
	archivo_temporal = "temporalfilepy"
	try:
		with open(archivo, 'r', encoding='utf-8') as file_lectura, open(archivo_temporal, 'w', encoding='utf-8') as file_escrituratemp:
			for linea in file_lectura:
				# Reemplazar el caracter Unicode raros por un espacio simple o ninguno
				linea = linea.replace('\u00A0', ' ')  # Espacio sin separación
				linea = linea.replace('\u2002', ' ')  # Espacio de cuarto de eme
				linea = linea.replace('\u2003', ' ')  # Espacio de media eme
				linea = linea.replace('\u2004', ' ')  # Espacio de tres por cuarto de eme
				linea = linea.replace('\u2005', ' ')  # Espacio de cuatro por eme
				linea = linea.replace('\u2006', ' ')  # Espacio de seis por eme
				linea = linea.replace('\u2009', ' ')  # Espacio delgado
				linea = linea.replace('\u200A', ' ')  # Espacio sin separación fino
				linea = linea.replace('\u200B', ' ')  # Espacio de puntuación cero ancho
				linea = linea.replace('\u200E', ' ')  # Marcador de izquierda a derecha
				linea = linea.replace('\u200F', ' ')  # Marcador de derecha a izquierda
				linea = linea.replace('\u202F', ' ')  # Espacio estrecho sin separación
				linea = linea.replace('\u205F', ' ')  # Espacio matemático
				linea = linea.replace('\u2007', ' ')  # Espacio sin separación de figura
				linea = linea.replace('\u2008', ' ')  # Espacio sin separación de puntuación
				linea = linea.replace('\u202C', '')
				linea = linea.replace('\u202D', '')

				#escribe solo los mensaje que no sean del sistema (del patron) y que no tengan saltos de lineas o espacios
				if not re.match(sys_mess, linea) and linea.strip():
					file_escrituratemp.write(linea)

		# Reemplazar el archivo original con el archivo temporal
		os.replace(archivo_temporal, archivo)
		print("Archivo procesado y sobrescrito exitosamente.")
	except Exception as e: #manejo de errores
		print(f"Ocurrió un error: {e}")
		# Intentar eliminar el archivo temporal si existe
		try:
			os.remove(archivo_temporal)
			print("Archivo temporal eliminado.")
		except Exception as e:
			print(f"No se pudo eliminar el archivo temporal: {e}")

# Nombre del archivo a procesar
archivo = "chatix.txt"

filtrar_y_escribir(archivo)
