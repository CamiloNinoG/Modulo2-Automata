# . Placa vehicular con formato extendido 
# • Formato: ABC-1234-Q 
# o 3 letras mayúsculas, guion, 4 dígitos, guion, una letra para tipo de vehículo 
# • Ejemplo válido: PQR-1298-M

from BaseAutomaton import BaseAutomaton

class VehiclePlateAutomaton(BaseAutomaton):
    def __init__(self):
        transitions = {
            0:  {'D': 10, 'L': 1,  '-': 10, 'X': 10},
            1:  {'D': 10, 'L': 2,  '-': 10, 'X': 10},
            2:  {'D': 10, 'L': 3,  '-': 10, 'X': 10},
            3:  {'D': 10, 'L': 10, '-': 4,  'X': 10},
            4:  {'D': 5,  'L': 10, '-': 10, 'X': 10},
            5:  {'D': 6,  'L': 10, '-': 10, 'X': 10},
            6:  {'D': 7,  'L': 10, '-': 10, 'X': 10},
            7:  {'D': 8,  'L': 10, '-': 10, 'X': 10},
            8:  {'D': 10, 'L': 10, '-': 9,  'X': 10},
            9:  {'D': 10, 'L': 11, '-': 10, 'X': 10},
            10: {'D': 10, 'L': 10, '-': 10, 'X': 10},  # estado de rechazo
            11: {'D': 10, 'L': 10, '-': 10, 'X': 10},  # estado final
        }
        final_state = 11
        reject_state = 10
        super().__init__(transitions, final_state, reject_state)

    def validate_with_trace(self, string):
        string = string.strip()
        valid_format, trace, final_state = self.run_trace(string)

        if not valid_format:
            # Validación detallada cuando falla el autómata
            parts = string.split("-")

            if len(parts) != 3:
                trace.append("Error: Expected format 'ABC-1234-Q' with exactly two hyphens.")
                return False, trace

            letters, digits, vehicle_type = parts

            # Validación de las primeras 3 letras
            if len(letters) != 3:
                trace.append("Error: The first part must be exactly 3 letters.")
            elif not letters.isalpha():
                trace.append("Error: The first part must contain only letters (A-Z).")
            elif not letters.isupper():
                trace.append("Error: The first 3 letters must be uppercase (A-Z).")

            # Validación de los 4 dígitos
            if len(digits) != 4:
                trace.append("Error: The middle part must be exactly 4 digits.")
            elif not digits.isdigit():
                trace.append("Error: The middle part must contain only digits (0-9).")

            # Validación de la última letra del tipo de vehículo
            if len(vehicle_type) != 1:
                trace.append("Error: Expected format 'ABC-1234-Q' with exactly two hyphens.")
            elif not vehicle_type.isalpha():
                trace.append("Error: The vehicle type must be a letter (A-Z).")
            elif not vehicle_type.isupper():
                trace.append("Error: The vehicle type letter must be uppercase (A-Z).")

            return False, trace

        # Validación extra semántica: la letra final debe estar entre M, C o B
        vehicle_type = string[-1]
        if vehicle_type in ['M', 'C', 'B']:
            trace.append(f"Valid vehicle type: '{vehicle_type}'.")
            return True, trace
        else:
            trace.append(f"Invalid vehicle type: '{vehicle_type}'. Must be one of 'M', 'C', or 'B'.")
            return False, trace



# if __name__ == "__main__":
#     automaton = VehiclePlateAutomaton()

#     test_strings = [
#         "PQR-1298-M ",  # invalid: lowercase letters in type
#         "202X-IS-0841",  # invalid: non-digit character in yea
#     ]

#     for s in test_strings:
#         print(f"\nTesting: {s}")
#         valid, trace = automaton.validate_with_trace(s)
#         for step in trace:
#             print(step)
#         print("Result:", "Valid" if valid else "Invalid")