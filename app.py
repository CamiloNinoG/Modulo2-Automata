import streamlit as st
import pandas as pd
from EnrollmentAutomaton import EnrollmentAutomaton
from VehiclePlateAutomaton import VehiclePlateAutomaton

st.title("Format Validator")

option = st.selectbox(
    "Select the format to validate:",
    ("University Enrollment", "Vehicle Plate")
)

symbols_matrix = ['D', 'L', '--', 'X'] 
if option == "University Enrollment":
    automaton = EnrollmentAutomaton()
    st.write("Expected format: YYYY-TT-CCCC (Year - Type - Code)")

    
    # Show transition matrix
    symbols = ['D', 'L', '-', 'X']
    states = range(14)
elif option == "Vehicle Plate":
    automaton = VehiclePlateAutomaton()
    st.write("Expected format: ABC-1234-Q (3 letters - 4 digits - 1 vehicle type letter)")

    # Show transition matrix
    symbols = ['L', 'D', '-', 'X']
    states = range(12)

# Build transition matrix for display
data = []
for state in states:
    row = []
    for s in symbols:
        next_state = automaton.transitions.get(state, {}).get(s)
        row.append(next_state if next_state is not None else "R/S")
    data.append(row)

df = pd.DataFrame(data, columns=symbols_matrix, index=[f"State {i}" for i in states])

st.subheader("Transition Matrix")
st.markdown("""
<style>
    table {
        margin-left: auto !important;
        margin-right: auto !important;
    }
    th, td {
        text-align: center !important;
    }
</style>
""", unsafe_allow_html=True)
st.table(df)

input_str = st.text_input("Enter the string to validate:")

if st.button("Validate"):
    if not input_str:
        st.warning("Please enter a string to validate.")
    else:
        valid, trace = automaton.validate_with_trace(input_str)
        st.subheader("Validation Steps:")
        for step in trace:
            st.text(step)
        if valid:
            st.success(f"The {option.lower()} format is valid 🎉")
        else:
            st.error(f"The {option.lower()} format is invalid ❌")
            
            
st.markdown("---")
st.subheader("Batch Validation from File")

uploaded_file = st.file_uploader("Upload a .txt file with strings (one per line)", type=["txt"])

def validate_file_lines(file_obj, automaton):
    lines = file_obj.read().decode('utf-8').splitlines()
    results = []
    for i, line in enumerate(lines, start=1):
        line_stripped = line.strip()
        if not line_stripped:
            continue  # Ignorar líneas vacías
        valid, trace = automaton.validate_with_trace(line_stripped)
        if valid:
            results.append((i, line_stripped, True, None, None))
        else:
            # Intentar encontrar error en trace
            error_pos = None
            error_char = None
            for msg in trace:
                if "No transition" in msg:
                    # Ejemplo: "Step 5: 'X' (L) → No transition from state 7"
                    # extraemos posición y char
                    parts = msg.split(":")[1].strip().split()
                    # parts ejemplo: "'X' (L) → No transition from state 7"
                    try:
                        error_char = parts[0].strip("'")
                        # el step indica la posición
                        step_part = msg.split(":")[0].strip()
                        # step_part ej: Step 5
                        error_pos = int(step_part.split()[1])
                    except:
                        pass
            results.append((i, line_stripped, False, error_pos, error_char))
    return results

if uploaded_file:
    st.write(f"Validating file for {option} format:")
    validation_results = validate_file_lines(uploaded_file, automaton)

    for (lineno, string, valid, err_pos, err_char) in validation_results:
        if valid:
            st.success(f"Line {lineno}: '{string}' → Valid")
        else:
            st.error(f"Line {lineno}: '{string}' → Invalid")
            if err_pos and err_char:
                st.write(f"  Error at position {err_pos} (character: '{err_char}')")
            st.write("  Trace:")
            # Recalculate and show the full trace for this line
            _, trace = automaton.validate_with_trace(string)
            for step in trace:
                st.text(f"    {step}")

                

