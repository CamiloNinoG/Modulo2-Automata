
class BaseAutomaton:
    def __init__(self, transitions, final_state, reject_state):
        self.transitions = transitions
        self.final_state = final_state
        self.reject_state = reject_state

    def char_to_symbol(self, c):
        if c.isdigit():
            return 'D'
        elif c.isalpha() and c.isupper():
            return 'L'
        elif c == '-':
            return '-'
        else:
            return 'X'

    def run_trace(self, string):
        state = 0
        steps = []
        for i, c in enumerate(string):
            symbol = self.char_to_symbol(c)
            if symbol in self.transitions[state]:
                next_state = self.transitions[state][symbol]
                steps.append(f"Step {i+1}: '{c}' ({symbol}) {state} → {next_state}")
                state = next_state
                if state == self.reject_state:
                    steps.append(f"Rejected: Reached reject state {state} at step {i+1}")
                    return False, steps, state
            else:
                steps.append(f"Step {i+1}: '{c}' ({symbol}) → No transition from state {state}")
                return False, steps, state

        if state == self.final_state:
            return True, steps, state
        else:
            steps.append(f"Invalid: Ended in non-final state {state}")
            return False, steps, state

    
