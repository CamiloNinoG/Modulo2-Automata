# BaseAutomaton.py
class BaseAutomaton:
    def __init__(self, transitions):
        self.transitions = transitions

    def char_to_symbol(self, c):
        if c.isdigit():
            return 'D'
        elif c.isalpha() and c.isupper():
            return 'L'
        elif c == '-':
            return '-'
        else:
            return 'X'

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
            if state == 13:
                steps.append(f"Reached reject state 13 at step {i+1}")
                return False, steps
        if state == 12:
            steps.append("Valid string: ended in final state 12.")
            return True, steps
        else:
            steps.append(f"Invalid string: ended in non-final state {state}.")
            return False, steps
