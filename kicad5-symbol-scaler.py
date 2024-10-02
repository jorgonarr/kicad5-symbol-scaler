import re

def scale_symbol(lib_file, symbol_name, scale_factor):
    with open(lib_file, 'r') as f:
        lines = f.readlines()

    scaled_lines = []
    in_symbol_section = False
    in_draw_section = False
    new_symbol_name = f"{symbol_name}_{scale_factor}"

    for line in lines:
        # Detecta el comienzo del símbolo
        if line.startswith('DEF '):
            current_symbol = line.split()[1]
            if current_symbol == symbol_name:
                in_symbol_section = True
            else:
                in_symbol_section = False

        # Si estamos en el símbolo seleccionado
        if in_symbol_section:
            # Cambiar el nombre del símbolo para que tenga el sufijo con el valor de escalado
            if line.startswith('DEF '):
                parts = line.split()
                parts[1] = new_symbol_name
                scaled_lines.append(' '.join(parts) + '\n')
                continue

            # Detecta el inicio de la sección DRAW (donde se encuentran los gráficos)
            if line.startswith('DRAW'):
                in_draw_section = True
                scaled_lines.append(line)
                continue
            elif line.startswith('ENDDRAW'):
                in_draw_section = False
                scaled_lines.append(line)
                continue

            if in_draw_section:
                # Escala las líneas dentro de la sección DRAW
                scaled_lines.append(scale_draw_command(line, scale_factor))
            else:
                # Agrega todas las líneas del símbolo sin cambios fuera de DRAW
                scaled_lines.append(line)

    # Agregar el símbolo escalado al final de la librería original
    with open(lib_file, 'a') as f:
        f.writelines(scaled_lines)

def scale_draw_command(command_line, scale_factor):
    # Divide la línea en sus componentes
    parts = command_line.split()

    # Tipos de elementos gráficos que contienen coordenadas
    element_types = ['P', 'S', 'C', 'A', 'X', 'T']

    if parts[0] in element_types:
        # Dependiendo del tipo de elemento, las coordenadas están en diferentes posiciones
        if parts[0] == 'P':  # Polígono (varias coordenadas)
            num_points = int(parts[1])
            for i in range(2, 2 + num_points * 2, 2):
                parts[i] = str(int(float(parts[i]) * scale_factor))  # Escalar coordenada X (entero)
                parts[i+1] = str(int(float(parts[i+1]) * scale_factor))  # Escalar coordenada Y (entero)
        elif parts[0] == 'S':  # Rectángulo (dos pares de coordenadas)
            parts[1] = str(int(float(parts[1]) * scale_factor))  # Escalar X1
            parts[2] = str(int(float(parts[2]) * scale_factor))  # Escalar Y1
            parts[3] = str(int(float(parts[3]) * scale_factor))  # Escalar X2
            parts[4] = str(int(float(parts[4]) * scale_factor))  # Escalar Y2
        elif parts[0] == 'C':  # Círculo (centro y radio)
            parts[1] = str(int(float(parts[1]) * scale_factor))  # Escalar X centro
            parts[2] = str(int(float(parts[2]) * scale_factor))  # Escalar Y centro
            parts[3] = str(round(float(parts[3]) * scale_factor, 2))  # Escalar radio (flotante)
        elif parts[0] == 'A':  # Arco (centro, radio y ángulos)
            parts[1] = str(int(float(parts[1]) * scale_factor))  # Escalar X centro
            parts[2] = str(int(float(parts[2]) * scale_factor))  # Escalar Y centro
            parts[3] = str(round(float(parts[3]) * scale_factor, 2))  # Escalar radio (flotante)
        elif parts[0] == 'X':  # Pin (posición, tamaño de nombre)
            parts[3] = str(int(float(parts[3]) * scale_factor))  # Escalar X
            parts[4] = str(int(float(parts[4]) * scale_factor))  # Escalar Y
            parts[5] = str(int(float(parts[5]) * scale_factor))  # Escalar longitud del pin (entero)
        elif parts[0] == 'T':  # Texto
            parts[2] = str(int(float(parts[2]) * scale_factor))  # Escalar X
            parts[3] = str(int(float(parts[3]) * scale_factor))  # Escalar Y
            parts[4] = str(round(float(parts[4]) * scale_factor, 2))  # Escalar tamaño del texto (flotante)

    # Asegura que la línea final esté correctamente formada
    return ' '.join(parts) + '\n'

def list_symbols(lib_file):
    """Función que lista los nombres de los símbolos dentro de una librería .lib"""
    with open(lib_file, 'r') as f:
        lines = f.readlines()

    symbols = []
    for line in lines:
        if line.startswith('DEF '):
            symbol_name = line.split()[1]
            symbols.append(symbol_name)

    return symbols

# Función principal
if __name__ == "__main__":
    # Solicitar al usuario la entrada de los datos
    input_lib = input("Introduce el nombre del archivo de la librería (ej: mi_libreria.lib): ")
    scale_factor = float(input("Introduce el factor de escala (ej: 2 para duplicar el tamaño, 0.8 para reducirlo): "))

    # Listar los símbolos disponibles en la librería
    symbols = list_symbols(input_lib)
    print(f"Símbolos disponibles en {input_lib}:")
    for symbol in symbols:
        print(f"- {symbol}")

    # Solicitar al usuario que seleccione un símbolo
    symbol_name = input("Introduce el nombre del símbolo que quieres escalar: ")

    # Verificar si el símbolo existe
    if symbol_name not in symbols:
        print(f"Error: El símbolo '{symbol_name}' no se encuentra en la librería '{input_lib}'.")
    else:
        # Escalar el símbolo seleccionado y añadirlo a la misma librería con el nuevo nombre
        scale_symbol(input_lib, symbol_name, scale_factor)
        print(f"El símbolo '{symbol_name}' ha sido escalado y añadido como '{symbol_name}_{scale_factor}' a {input_lib}.")
