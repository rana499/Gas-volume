import streamlit as st

# App Title
st.title("Advanced Gas Volume Calculator")
st.write("Calculate the volume of a gas by entering the temperature and pressure.")

# Input Section
st.header("Enter Inputs:")

# Pressure input with new unit kg/cm²
p_unit = st.selectbox("Pressure Unit:", ["atm", "kPa", "kg/cm²"])
p = st.number_input(f"Pressure ({p_unit}):", min_value=0.01, value=1.0)

# Temperature input with new unit Fahrenheit
t_unit = st.selectbox("Temperature Unit:", ["Celsius (°C)", "Kelvin (K)", "Fahrenheit (°F)"])
t = st.number_input(f"Temperature ({t_unit}):", value=25.0)

n = st.number_input("Number of Moles (n):", min_value=0.01, value=1.0)

# Calculation
if st.button("Calculate Volume"):
    
    # 1. Temperature Conversion to Kelvin
    if t_unit == "Celsius (°C)":
        T_kelvin = t + 273.15
    elif t_unit == "Fahrenheit (°F)":
        T_kelvin = (t - 32) * 5/9 + 273.15
    else:
        T_kelvin = t
        
    # 2. Pressure Conversion & R value setting
    # We will convert all pressures to 'atm' or 'kPa' to match standard R constants
    if p_unit == "atm":
        R = 0.0821  # L·atm/(mol·K)
        P_converted = p
    elif p_unit == "kPa":
        R = 8.314   # kPa·L/(mol·K)
        P_converted = p
    elif p_unit == "kg/cm²":
        R = 0.0821  # Standard R for atm
        P_converted = p * 0.967841  # Convert kg/cm² to atm

    # Ideal Gas Law Formula: V = (n * R * T) / P
    v = (n * R * T_kelvin) / P_converted
    
    # Display the Result
    st.success(f"Estimated Gas Volume (V) = {v:.2f} Liters (L)")
