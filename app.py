import streamlit as st
import pandas as pd
from EnrollmentAutomaton import EnrollmentAutomaton

automaton = EnrollmentAutomaton()

st.title("University Enrollment Format Validator")
st.write("Expected format: YYYY-TT-CCCC (Year - Type - Code)")

st.subheader("Transition Matrix")
symbols = ['D', 'L', '--', 'X']  # include invalid symbol
data = []
for state in range(14):  # states 0 to 13
    row = []
    for s in symbols:
        next_state = automaton.transitions.get(state, {}).get(s)
        row.append(next_state if next_state is not None else "—")
    data.append(row)

df = pd.DataFrame(data, columns=symbols, index=[f'State {i}' for i in range(14)])

# Apply custom CSS to center align
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

# Use st.table for clean layout (no scroll, centered)
st.table(df)

# Input and validation
input_str = st.text_input("Enter enrollment string to validate:")

if st.button("Validate"):
    if not input_str:
        st.warning("Please enter an enrollment string.")
    else:
        valid, trace = automaton.validate_with_trace(input_str)
        st.subheader("Validation Steps:")
        for step in trace:
            st.text(step)
        if valid:
            st.success("The enrollment format is valid 🎉")
        else:
            st.error("The enrollment format is invalid ❌")
