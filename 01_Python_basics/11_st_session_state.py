# !pip install streamlit
# !python -m streamlit run app.py
import streamlit as st

def incr():
    # this function increase both counters by 1
    global temp_counter
    temp_counter += 1
    st.session_state.perm_counter += 1

# regular python variable 
temp_counter = 0

# streamlit session state variable
if "perm_counter" not in st.session_state:
    st.session_state.perm_counter = 0

# display both counter values
st.write(f"TEMP = {temp_counter}")
st.write(f"PERM = {st.session_state.perm_counter}")

# this button calls the `incr` function
st.button("Increment", on_click=incr)