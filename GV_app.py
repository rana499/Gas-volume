import streamlit as st

# App Title
st.title("Gas Volume Calculator App")
st.write("Calculate the volume of a gas by entering the temperature and pressure.")

# Input Section
st.header("Enter Inputs:")
p_unit = st.selectbox("Pressure Unit:", ["atm", "kPa"])
p = st.number_input(f"Pressure ({p_unit}):", min_value=0.01, value=1.0)

t_unit = st.selectbox("Temperature Unit:", ["Celsius (°C)", "Kelvin (K)"])
t = st.number_input(f"Temperature ({t_unit}):", value=25.0)

n = st.number_input("Number of Moles (n):", min_value=0.01, value=1.0)

# Calculation
if st.button("Calculate Volume"):
    # Convert temperature to Kelvin if it's in Celsius
    T_kelvin = t + 273.15 if t_unit == "Celsius (°C)" else t
    
    # Determine the value of R based on the pressure unit
    if p_unit == "atm":
        R = 0.0821  # L·atm/(mol·K)
        P_atm = p
    else:
        R = 8.314   # kPa·L/(mol·K)
        P_atm = p

    # Ideal Gas Law Formula: V = (n * R * T) / P
    v = (n * R * T_kelvin) / P_atm
    
    # Display the Result
    st.success(f"Estimated Gas Volume (V) = {v:.2f} Liters (L)")
