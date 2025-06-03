def autómata_termina_en_01(cadena):
    estado = "q0"  # estado inicial

    for simbolo in cadena:
        if estado == "q0":
            if simbolo == "0":
                estado = "q1"
            elif simbolo == "1":
                estado = "q0"
            else:
                return False  # carácter no válido
        elif estado == "q1":
            if simbolo == "1":
                estado = "q2"
            elif simbolo == "0":
                estado = "q1"
            else:
                return False
        elif estado == "q2":
            # Ya llegó al estado final, pero si sigue leyendo reinicia
            if simbolo == "0":
                estado = "q1"
            elif simbolo == "1":
                estado = "q0"
            else:
                return False

    return estado == "q2"  # acepta si termina en estado q2

# Ejemplos
print(autómata_termina_en_01("11010011"))  # 
print(autómata_termina_en_01("1000"))  # 
print(autómata_termina_en_01("01"))    # 
print(autómata_termina_en_01("111"))   # 
