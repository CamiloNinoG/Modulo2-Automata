
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
            0:  {'D': 1,   'L': 13, '-': 13, 'X': 13},
            1:  {'D': 2,   'L': 13, '-': 13, 'X': 13},
            2:  {'D': 3,   'L': 13, '-': 13, 'X': 13},
            3:  {'D': 4,   'L': 13, '-': 13, 'X': 13},
            4:  {'D': 13,  'L': 13, '-': 5,  'X': 13},
            5:  {'D': 13,  'L': 6,  '-': 13, 'X': 13},
            6:  {'D': 13,  'L': 7,  '-': 13, 'X': 13},
            7:  {'D': 13,  'L': 13, '-': 8,  'X': 13},
            8:  {'D': 9,   'L': 13, '-': 13, 'X': 13},
            9:  {'D': 10,  'L': 13, '-': 13, 'X': 13},
            10: {'D': 11,  'L': 13, '-': 13, 'X': 13},
            11: {'D': 12,  'L': 13, '-': 13, 'X': 13},
            12: {'D': 13,  'L': 13, '-': 13, 'X': 13},
            13: {'D': 13,  'L': 13, '-': 13, 'X': 13}
        }
        final_state = 12
        reject_state = 13
        super().__init__(transitions, final_state, reject_state)

    def validate_with_trace(self, string):
        string = string.strip()
        valid_format, trace, final_state = self.run_trace(string)

        if not valid_format:
            parts = string.split("-")

            if len(parts) != 3:
                trace.append("Error: Expected format 'YYYY-TT-CCCC' with exactly two hyphens.")
                return False, trace

            year, career_type, code = parts

            # Validación del año
            if not year.isdigit() or len(year) != 4:
                trace.append("Error: The year part must be 4 digits (e.g., '2023').")
            else:
                try:
                    year_int = int(year)
                    current_year = datetime.now().year
                    if year_int > current_year:
                        trace.append(f"Error: Year '{year}' is in the future.")
                except ValueError:
                    trace.append("Error: Year part is not numeric.")

            # Validación del tipo de carrera (detectando minúsculas)
            if len(career_type) != 2:
                trace.append("Error: The career type must be exactly 2 characters.")
            elif not career_type.isalpha():
                trace.append("Error: The career type must contain only letters (e.g., 'IS').")
            elif not career_type.isupper():
                trace.append("Error: The career type must be in uppercase (e.g., 'IS'). Lowercase letters are not allowed.")

            # Validación del código
            if not code.isdigit() or len(code) != 4:
                trace.append("Error: The code part must be 4 digits (e.g., '0841').")

            return False, trace

        # Validación extra: año correcto
        year_part = string[:4]
        try:
            year_int = int(year_part)
            current_year = datetime.now().year
            if year_int <= current_year:
                # trace.append(f"Year check passed: {year_part} <= {current_year}")
                return True, trace
            else:
                trace.append(f"Error: Year '{year_part}' is greater than current year {current_year}.")
                return False, trace
        except ValueError:
            trace.append("Error: Year part is not numeric.")
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