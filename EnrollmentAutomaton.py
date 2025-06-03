
# 7. Formato de matrícula universitaria 
# Formato: AÑO-TIPO-CÓDIGO 
# 4 dígitos de año, guion, dos letras (tipo de carrera), guion, 4 dígitos 
# Ejemplo válido: 2023-IS-0841

# FORMATO: AAAA-TT-CCCC
# Donde:
# - AAAA: Año (4 dígitos)
# - TT: Letras del tipo de carrera (2 letras mayúsculas)
# - CCCC: Código (4 dígitos)
 
class EnrollmentAutomaton:
    def __init__(self):
        self.transitions = {
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

    def char_to_symbol(self, c):
        if c.isdigit():
            return 'D'
        elif c.isalpha() and c.isupper():
            return 'L'
        elif c == '-':
            return '-'
        else:
            return 'X'  # any invalid char maps to 'X'

    def validate_with_trace(self, string):
        state = 0
        steps = []
        for i, c in enumerate(string):
            symbol = self.char_to_symbol(c)
            if symbol in self.transitions[state]:
                next_state = self.transitions[state][symbol]
                steps.append(f"Step {i+1}: '{c}' ({symbol}) {state} -> {next_state}")
                state = next_state
            else:
                steps.append(f"Step {i+1}: '{c}' ({symbol}) No transition from state {state}")
                return False, steps
            if state == 13:  # reject state reached
                steps.append(f"Reached reject state 13 at step {i+1}")
                return False, steps

        if state == 12:
            steps.append("Valid string: ended in final state 12.")
            return True, steps
        else:
            steps.append(f"Invalid string: ended in non-final state {state}.")
            return False, steps


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