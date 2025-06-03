# . Placa vehicular con formato extendido 
# • Formato: ABC-1234-Q 
# o 3 letras mayúsculas, guion, 4 dígitos, guion, una letra para tipo de vehículo 
# • Ejemplo válido: PQR-1298-M

from BaseAutomaton import BaseAutomaton

class VehiclePlateAutomaton(BaseAutomaton):
    def __init__(self):
        transitions = {
            0: {'L': 1, 'X': 10},
            1: {'L': 2, 'X': 10},
            2: {'L': 3, 'X': 10},
            3: {'-': 4, 'X': 10},
            4: {'D': 5, 'X': 10},
            5: {'D': 6, 'X': 10},
            6: {'D': 7, 'X': 10},
            7: {'D': 8, 'X': 10},
            8: {'-': 9, 'X': 10},
            9: {'L': 11, 'X': 10},
            10: {'X': 10},  # estado de rechazo
            11: {},         # estado final
        }
        final_states = {11}
        reject_state = 10
        super().__init__(transitions, final_states, reject_state)

    def validate_with_trace(self, string):
        string = string.strip()
        valid_format, trace, final_state = self.run_trace(string)

        if not valid_format:
            trace.append(f"Invalid format: ended in state {final_state}")
            return False, trace

        # Verificación semántica adicional
        vehicle_type = string[-1]
        if vehicle_type in ['M', 'C', 'B']:
            trace.append(f"Tipo de vehículo válido: '{vehicle_type}'")
            return True, trace
        else:
            trace.append(f"Tipo de vehículo inválido: '{vehicle_type}'")
            return False, trace


if __name__ == "__main__":
    automaton = VehiclePlateAutomaton()

    test_strings = [
        "PQR-1298-M ",  # invalid: lowercase letters in type
        "202X-IS-0841",  # invalid: non-digit character in yea
    ]

    for s in test_strings:
        print(f"\nTesting: {s}")
        valid, trace = automaton.validate_with_trace(s)
        for step in trace:
            print(step)
        print("Result:", "Valid" if valid else "Invalid")