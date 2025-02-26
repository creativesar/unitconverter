import streamlit as st

# Streamlit app configuration
st.set_page_config(page_title="📏 Ultimate Unit Converter", layout="wide", page_icon="📏")
st.title("📏 Ultimate Unit Converter")

# Enhanced Custom Styling for UI/UX
st.markdown(
    """
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #f0f4f8, #e2e8f0);
            color: #2d3748;
            margin: 0;
            padding: 0;
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
            padding: 30px;
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .stHeader {
            animation: slideIn 0.8s ease-out;
            font-size: 3rem;
            font-weight: 700;
            color: #3182ce;
            text-align: center;
            margin-bottom: 30px;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background: linear-gradient(90deg, #3182ce, #63b3ed);
            color: white;
            border-radius: 15px;
            padding: 12px 30px;
            font-size: 16px;
            font-weight: 600;
            transition: all 0.4s ease;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.15);
        }
        .stButton>button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
            background: linear-gradient(90deg, #2b6cb0, #4299e1);
        }
        .stNumberInput>div>div,
        .stSelectbox>div>div {
            background: #ffffff;
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            padding: 8px;
            transition: all 0.3s ease;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        }
        .stNumberInput>div>div:focus-within,
        .stSelectbox>div>div:focus-within {
            border-color: #3182ce;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        .result-box {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            margin-top: 25px;
            animation: fadeIn 0.8s ease-in-out;
        }
        .explanation-box {
            background: #edf2f7;
            border-left: 4px solid #3182ce;
            border-radius: 8px;
            padding: 15px;
            margin-top: 15px;
            font-size: 14px;
            color: #4a5568;
        }
        .footer {
            text-align: center;
            padding: 20px;
            background: #ffffff;
            border-radius: 15px;
            margin-top: 30px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        }
        .sidebar .css-1d391kg {
            background: #ffffff;
            border-right: 2px solid #e2e8f0;
            box-shadow: 3px 0 10px rgba(0, 0, 0, 0.05);
            padding: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Conversion functions
def convert_length(value, from_unit, to_unit):
    conversions = {"meter": 1, "kilometer": 1000, "centimeter": 0.01, "millimeter": 0.001, "mile": 1609.34, "yard": 0.9144, "foot": 0.3048, "inch": 0.0254}
    return value * conversions[from_unit] / conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {"kilogram": 1, "gram": 0.001, "milligram": 0.000001, "pound": 0.453592, "ounce": 0.0283495}
    return value * conversions[from_unit] / conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius":
        if to_unit == "fahrenheit": return (value * 9/5) + 32
        elif to_unit == "kelvin": return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius": return (value - 32) * 5/9
        elif to_unit == "kelvin": return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius": return value - 273.15
        elif to_unit == "fahrenheit": return (value - 273.15) * 9/5 + 32
    return value

def convert_volume(value, from_unit, to_unit):
    conversions = {"liter": 1, "milliliter": 0.001, "gallon": 3.78541, "quart": 0.946353, "pint": 0.473176, "cup": 0.24}
    return value * conversions[from_unit] / conversions[to_unit]

def convert_area(value, from_unit, to_unit):
    conversions = {"square meter": 1, "square kilometer": 1e6, "square centimeter": 0.0001, "square mile": 2.58999e6, "square yard": 0.836127, "square foot": 0.092903, "acre": 4046.86}
    return value * conversions[from_unit] / conversions[to_unit]

def convert_speed(value, from_unit, to_unit):
    conversions = {"meter/second": 1, "kilometer/hour": 0.277778, "mile/hour": 0.44704, "foot/second": 0.3048, "knot": 0.514444}
    return value * conversions[from_unit] / conversions[to_unit]

def convert_time(value, from_unit, to_unit):
    conversions = {"second": 1, "minute": 60, "hour": 3600, "day": 86400, "week": 604800, "year": 31536000}
    return value * conversions[from_unit] / conversions[to_unit]

def convert_energy(value, from_unit, to_unit):
    conversions = {"joule": 1, "kilojoule": 1000, "calorie": 4.184, "kilocalorie": 4184, "watt-hour": 3600, "kilowatt-hour": 3.6e6}
    return value * conversions[from_unit] / conversions[to_unit]

# Sidebar for unit category selection
st.sidebar.header("📐 Select Unit Category")
unit_category = st.sidebar.selectbox(
    "Choose a category", 
    ["Length", "Weight", "Temperature", "Volume", "Area", "Speed", "Time", "Energy"], 
    help="Pick a category to start converting units!"
)

# Main conversion logic
st.header(f"🔢 {unit_category} Converter")
precision = st.slider("Decimal Precision", 1, 6, 2, help="Adjust decimal places in the result.")

if unit_category == "Length":
    col1, col2 = st.columns(2)
    with col1: from_unit = st.selectbox("From", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
    with col2: to_unit = st.selectbox("To", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    result = convert_length(value, from_unit, to_unit)
    explanation = f"To convert {value} {from_unit} to {to_unit}:\n1. Base unit is meter.\n2. {from_unit} to meter: {value} × {convert_length(1, from_unit, 'meter')} = {value * convert_length(1, from_unit, 'meter')} meters.\n3. Meter to {to_unit}: {value * convert_length(1, from_unit, 'meter')} ÷ {convert_length(1, to_unit, 'meter')} = {result:.{precision}f} {to_unit}."

elif unit_category == "Weight":
    col1, col2 = st.columns(2)
    with col1: from_unit = st.selectbox("From", ["kilogram", "gram", "milligram", "pound", "ounce"])
    with col2: to_unit = st.selectbox("To", ["kilogram", "gram", "milligram", "pound", "ounce"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    result = convert_weight(value, from_unit, to_unit)
    explanation = f"To convert {value} {from_unit} to {to_unit}:\n1. Base unit is kilogram.\n2. {from_unit} to kilogram: {value} × {convert_weight(1, from_unit, 'kilogram')} = {value * convert_weight(1, from_unit, 'kilogram')} kilograms.\n3. Kilogram to {to_unit}: {value * convert_weight(1, from_unit, 'kilogram')} ÷ {convert_weight(1, to_unit, 'kilogram')} = {result:.{precision}f} {to_unit}."

elif unit_category == "Temperature":
    col1, col2 = st.columns(2)
    with col1: from_unit = st.selectbox("From", ["celsius", "fahrenheit", "kelvin"])
    with col2: to_unit = st.selectbox("To", ["celsius", "fahrenheit", "kelvin"])
    value = st.number_input("Enter value", format="%.2f")
    result = convert_temperature(value, from_unit, to_unit)
    if from_unit == "celsius" and to_unit == "fahrenheit":
        explanation = f"To convert {value} °C to °F:\n1. Multiply by 9/5: {value} × 9/5 = {value * 9/5}.\n2. Add 32: {value * 9/5} + 32 = {result:.{precision}f} °F."
    elif from_unit == "celsius" and to_unit == "kelvin":
        explanation = f"To convert {value} °C to K:\n1. Add 273.15: {value} + 273.15 = {result:.{precision}f} K."
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        explanation = f"To convert {value} °F to °C:\n1. Subtract 32: {value} - 32 = {value - 32}.\n2. Multiply by 5/9: {value - 32} × 5/9 = {result:.{precision}f} °C."
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        explanation = f"To convert {value} °F to K:\n1. Subtract 32: {value} - 32 = {value - 32}.\n2. Multiply by 5/9: {value - 32} × 5/9 = {(value - 32) * 5/9}.\n3. Add 273.15: {(value - 32) * 5/9} + 273.15 = {result:.{precision}f} K."
    elif from_unit == "kelvin" and to_unit == "celsius":
        explanation = f"To convert {value} K to °C:\n1. Subtract 273.15: {value} - 273.15 = {result:.{precision}f} °C."
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        explanation = f"To convert {value} K to °F:\n1. Subtract 273.15: {value} - 273.15 = {value - 273.15}.\n2. Multiply by 9/5: {value - 273.15} × 9/5 = {(value - 273.15) * 9/5}.\n3. Add 32: {(value - 273.15) * 9/5} + 32 = {result:.{precision}f} °F."
    else:
        explanation = "No conversion needed as units are the same."

elif unit_category == "Volume":
    col1, col2 = st.columns(2)
    with col1: from_unit = st.selectbox("From", ["liter", "milliliter", "gallon", "quart", "pint", "cup"])
    with col2: to_unit = st.selectbox("To", ["liter", "milliliter", "gallon", "quart", "pint", "cup"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    result = convert_volume(value, from_unit, to_unit)
    explanation = f"To convert {value} {from_unit} to {to_unit}:\n1. Base unit is liter.\n2. {from_unit} to liter: {value} × {convert_volume(1, from_unit, 'liter')} = {value * convert_volume(1, from_unit, 'liter')} liters.\n3. Liter to {to_unit}: {value * convert_volume(1, from_unit, 'liter')} ÷ {convert_volume(1, to_unit, 'liter')} = {result:.{precision}f} {to_unit}."

elif unit_category == "Area":
    col1, col2 = st.columns(2)
    with col1: from_unit = st.selectbox("From", ["square meter", "square kilometer", "square centimeter", "square mile", "square yard", "square foot", "acre"])
    with col2: to_unit = st.selectbox("To", ["square meter", "square kilometer", "square centimeter", "square mile", "square yard", "square foot", "acre"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    result = convert_area(value, from_unit, to_unit)
    explanation = f"To convert {value} {from_unit} to {to_unit}:\n1. Base unit is square meter.\n2. {from_unit} to square meter: {value} × {convert_area(1, from_unit, 'square meter')} = {value * convert_area(1, from_unit, 'square meter')} square meters.\n3. Square meter to {to_unit}: {value * convert_area(1, from_unit, 'square meter')} ÷ {convert_area(1, to_unit, 'square meter')} = {result:.{precision}f} {to_unit}."

elif unit_category == "Speed":
    col1, col2 = st.columns(2)
    with col1: from_unit = st.selectbox("From", ["meter/second", "kilometer/hour", "mile/hour", "foot/second", "knot"])
    with col2: to_unit = st.selectbox("To", ["meter/second", "kilometer/hour", "mile/hour", "foot/second", "knot"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    result = convert_speed(value, from_unit, to_unit)
    explanation = f"To convert {value} {from_unit} to {to_unit}:\n1. Base unit is meter/second.\n2. {from_unit} to meter/second: {value} × {convert_speed(1, from_unit, 'meter/second')} = {value * convert_speed(1, from_unit, 'meter/second')} meter/second.\n3. Meter/second to {to_unit}: {value * convert_speed(1, from_unit, 'meter/second')} ÷ {convert_speed(1, to_unit, 'meter/second')} = {result:.{precision}f} {to_unit}."

elif unit_category == "Time":
    col1, col2 = st.columns(2)
    with col1: from_unit = st.selectbox("From", ["second", "minute", "hour", "day", "week", "year"])
    with col2: to_unit = st.selectbox("To", ["second", "minute", "hour", "day", "week", "year"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    result = convert_time(value, from_unit, to_unit)
    explanation = f"To convert {value} {from_unit} to {to_unit}:\n1. Base unit is second.\n2. {from_unit} to second: {value} × {convert_time(1, from_unit, 'second')} = {value * convert_time(1, from_unit, 'second')} seconds.\n3. Second to {to_unit}: {value * convert_time(1, from_unit, 'second')} ÷ {convert_time(1, to_unit, 'second')} = {result:.{precision}f} {to_unit}."

elif unit_category == "Energy":
    col1, col2 = st.columns(2)
    with col1: from_unit = st.selectbox("From", ["joule", "kilojoule", "calorie", "kilocalorie", "watt-hour", "kilowatt-hour"])
    with col2: to_unit = st.selectbox("To", ["joule", "kilojoule", "calorie", "kilocalorie", "watt-hour", "kilowatt-hour"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    result = convert_energy(value, from_unit, to_unit)
    explanation = f"To convert {value} {from_unit} to {to_unit}:\n1. Base unit is joule.\n2. {from_unit} to joule: {value} × {convert_energy(1, from_unit, 'joule')} = {value * convert_energy(1, from_unit, 'joule')} joules.\n3. Joule to {to_unit}: {value * convert_energy(1, from_unit, 'joule')} ÷ {convert_energy(1, to_unit, 'joule')} = {result:.{precision}f} {to_unit}."

# Display result with explanation
if st.button("Convert"):
    st.markdown(
        f"""
        <div class="result-box">
            <h3 style="color: #3182ce;">✅ Conversion Result</h3>
            <p><strong>{value:.{precision}f} {from_unit}</strong> equals <strong>{result:.{precision}f} {to_unit}</strong>.</p>
            <button onclick="navigator.clipboard.writeText('{result:.{precision}f} {to_unit}')">📋 Copy Result</button>
        </div>
        <div class="explanation-box">
            <h4>📘 How It Works:</h4>
            <pre>{explanation}</pre>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown(
    """
    <div class="footer">
        <h3 style="color: #3182ce;">🚀 Crafted by Sarfraz Ahmad</h3>
        <p>Unleash the power of unit conversion with this sleek tool!</p>
    </div>
    """,
    unsafe_allow_html=True,
)