
# 7. Formato de matrícula universitaria 
# Formato: AÑO-TIPO-CÓDIGO 
# 4 dígitos de año, guion, dos letras (tipo de carrera), guion, 4 dígitos 
# Ejemplo válido: 2023-IS-0841

# FORMATO: AAAA-TT-CCCC
# Donde:
# - AAAA: Año (4 dígitos)
# - TT: Letras del tipo de carrera (2 letras mayúsculas)
# - CCCC: Código (4 dígitos)
# EnrollmentAutomaton.py
from datetime import datetime
from BaseAutomaton import BaseAutomaton


class EnrollmentAutomaton(BaseAutomaton):
    def __init__(self):
        transitions = {
            0: {'D': 1, 'X': 13},
            1: {'D': 2, 'X': 13},
            2: {'D': 3, 'X': 13},
            3: {'D': 4, 'X': 13},
            4: {'-': 5, 'X': 13},
            5: {'L': 6, 'X': 13},
            6: {'L': 7, 'X': 13},
            7: {'-': 8, 'X': 13},
            8: {'D': 9, 'X': 13},
            9: {'D': 10, 'X': 13},
            10: {'D': 11, 'X': 13},
            11: {'D': 12, 'X': 13},
            12: {},  # Final state, no más transiciones
            13: {'X': 13}  # Estado de rechazo
        }
        final_states = {12}
        reject_state = 13
        super().__init__(transitions, final_states, reject_state)

    def validate_with_trace(self, string):
        string = string.strip()
        valid_format, trace, final_state = self.run_trace(string)

        if not valid_format:
            trace.append(f"Invalid format: ended in state {final_state}")
            return False, trace

        # Validación extra: año correcto
        year_part = string[:4]
        try:
            year_int = int(year_part)
            current_year = datetime.now().year
            if year_int < current_year:
                trace.append(f"Year check passed: {year_part} < {current_year}")
                return True, trace
            else:
                trace.append(f"Year check failed: {year_part} is not less than {current_year}")
                return False, trace
        except ValueError:
            trace.append("Year parsing error.")
            return False, trace


if __name__ == "__main__":
    automaton = EnrollmentAutomaton()

    test_strings = [
        "2023-is-0841",  # invalid: lowercase letters in type
        "202X-IS-0841",  # invalid: non-digit character in yea
    ]

    for s in test_strings:
        print(f"\nTesting: {s}")
        valid, trace = automaton.validate_with_trace(s)
        for step in trace:
            print(step)
        print("Result:", "Valid" if valid else "Invalid")