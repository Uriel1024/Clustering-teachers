import pdfplumber

def extraer_profesores(ruta_pdf):
    nombres_profesores = []
    
    with pdfplumber.open(ruta_pdf) as pdf:
        for pagina in pdf.pages:
            # Extraer la tabla de la página
            tabla = pagina.extract_table()
            
            if tabla:
                for fila in tabla:
                    nombre = fila[0] # La columna izquierda es el índice 0
                    # Limpiamos saltos de línea y espacios extras
                    if nombre and nombre != "NOMBRE PROFESOR":
                        nombres_profesores.append(nombre.replace('\n', ' ').strip())
    
    return nombres_profesores

# Uso
lista = extraer_profesores("1.pdf")
print(lista)