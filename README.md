
# KiCad 5 Symbol Scaler Script

Este script permite escalar automáticamente símbolos de una librería `.lib` de KiCad 5, manteniendo las proporciones y agregando los símbolos escalados al final de la misma librería. Los símbolos escalados se renombran para incluir el valor de escalado en su nombre, permitiendo distinguirlos de los símbolos originales.

## Características

- Escala automáticamente cualquier símbolo de una librería `.lib` de KiCad 5.
- Mantiene las proporciones al reescalar los elementos gráficos del símbolo.
- Agrega el símbolo escalado a la misma librería original, con un sufijo que indica el factor de escalado.
- Funciona con factores de escalado mayores y menores a 1 (por ejemplo, `2.0` para duplicar el tamaño, `0.8` para reducirlo en un 20%).

## Requisitos

- **Python 3.x** instalado.
- Una librería `.lib` de KiCad 5 que contenga los símbolos a escalar.

## Instalación

#Con terminal

1. Clona el repositorio en tu máquina local:

   \`\`\`bash
   git clone https://github.com/tu_usuario/kicad5-symbol-scaler.git
   \`\`\`

2. Navega al directorio del repositorio:

   \`\`\`bash
   cd kicad5-symbol-scaler
   \`\`\`

#Sin terminal

1. Descarga el script kicad5-symbol-scaler.py de Releases

2. Cópialo a la carpeta donde está la librería que contiene el símbolo que quieres editar.

## Uso

1. Ejecuta el script con Python:

   #Linux / macOS
   \`\`\`bash
   python kicad5-symbol-scaler.py
   \`\`\`

   #Windows
   \`\`\`python3 kicad5-symbol-scaler.py

3. Introduce los datos solicitados:
   - Nombre del archivo de la librería `.lib` (Ej: `mi_libreria.lib`).
   - Factor de escala (Ej: `0.8` para reducir el tamaño un 20% o `2.0` para duplicarlo).
   - Selecciona el símbolo que deseas escalar de la lista que se te muestra.

4. El símbolo escalado se añadirá al final del archivo de la librería original con el sufijo que indica el valor de escalado. Por ejemplo, `PIC16F84A-DIP_0.8` si escalas el símbolo `PIC16F84A-DIP` con un factor de `0.8`.

### Ejemplo de Entrada

\`\`\`bash
Introduce el nombre del archivo de la librería (ej: mi_libreria.lib): mi_libreria.lib
Introduce el factor de escala (ej: 2 para duplicar el tamaño, 0.8 para reducirlo): 0.8
Símbolos disponibles en mi_libreria.lib:
- PIC16F84A-DIP
- Resistor
Introduce el nombre del símbolo que quieres escalar: PIC16F84A-DIP
\`\`\`

### Resultado

El símbolo `PIC16F84A-DIP_0.8` se añadirá al final del archivo `mi_libreria.lib`.

## Consideraciones

- **No sobrescribe** los símbolos existentes. El símbolo escalado se añade con un nuevo nombre, dejando intacto el símbolo original.
- **Factores de escala recomendados**: Puedes usar cualquier valor positivo de escala, tanto mayor como menor a 1. Sin embargo, algunos factores muy pequeños o muy grandes pueden deformar el símbolo de forma inesperada.

## Estructura del proyecto

- `kicad5-symbol-scaler.py`: El script principal para escalar símbolos.
- `README.md`: Instrucciones de uso y descripción del script.

## Licencia

El script ha sido creado con ChatGPT. Este proyecto está licenciado bajo la Licencia MIT. Puedes usarlo y modificarlo libremente para tus propios proyectos.
