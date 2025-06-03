# Reglas sintácticas del lenguaje Neutrino: 

# • Bloques: deben comenzar con iniciar y terminar con finalizar. 

# • Declaración de variables: 
#   - número nombre_variable; 
#   - cadena nombre_variable; 
#   - booleano nombre_variable; 

# • Asignación de valores: 
#   - nombre_variable := expresión; 

# • Operadores válidos: 
#   - Aritméticos: +, -, *, / 
#   - Comparación: ==, !=, <, >, <=, >= 
#   - Lógicos: y, o, no 

# • Estructuras de control: o si condición entonces ... sino ... fin 
#   - mientras condición hacer ... fin 
#   - para nombre := valor_inicial hasta valor_final hacer ... fin 

# • Entrada/salida: o mostrar "mensaje"; 
#       leer nombre_variable; 

# Reglas semánticas: 
#   - No se pueden usar variables no declaradas. 
#   - Cada instrucción debe finalizar con ;. 
#   - Las cadenas deben ir entre comillas dobles ("). 
#   - El nombre de variables debe iniciar con una letra y puede incluir letras, números y guiones 
# bajos. 

# Funcionalidades requeridas: 

# • Área de texto para cargar código desde un archivo .txt. 

# • El autómata debe: 
#   - Procesar línea por línea 
#   - Identificar errores de sintaxis 
#   - Mostrar número de línea, carácter del error y una descripción 

# • Si todo está correcto: mostrar "El código es válido". 

# Ejemplo de código válido: 
 
# iniciar 
#     número contador; 
#     contador := 0; 
#     para contador := 0 hasta 10 hacer 
#         mostrar "Iteración"; 
#     fin 
# finalizar 