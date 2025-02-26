import streamlit as st

# Streamlit app configuration
st.set_page_config(page_title="📏 Unit Converter Pro", layout="wide", page_icon="📏")
st.title("📏 Unit Converter Pro")

# Custom Styling with Enhanced Animations
st.markdown(
    """
    <style>
        /* General Styling */
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #e0f7fa, #f5f5f5); /* Gradient background */
            color: #333;
            margin: 0;
            padding: 0;
        }
        .stApp {
            padding: 30px;
        }

        /* Header Animation */
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-50px); }
            to { opacity: 1; transform: translateX(0); }
        }
        .stHeader {
            animation: slideIn 1.2s ease-out;
            font-size: 3rem;
            font-weight: 700;
            color: #0288D1; /* Blue accent */
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 25px;
        }

        /* Button Styling with Pulse Animation */
        .stButton>button {
            background: linear-gradient(45deg, #0288D1, #4FC3F7);
            color: white;
            border-radius: 15px;
            padding: 14px 28px;
            font-size: 18px;
            font-weight: bold;
            transition: all 0.4s ease;
            box-shadow: 0 5px 15px rgba(2, 136, 209, 0.3);
        }
        .stButton>button:hover {
            transform: scale(1.08) rotate(2deg);
            box-shadow: 0 8px 20px rgba(2, 136, 209, 0.5);
            animation: pulse 1s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1.08); }
            50% { transform: scale(1.12); }
            100% { transform: scale(1.08); }
        }

        /* Input Fields with Bounce Effect */
        .stNumberInput>div>div,
        .stSelectbox>div>div {
            background: #fff;
            border: 2px solid #b0bec5;
            border-radius: 15px;
            padding: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        .stNumberInput>div>div:focus-within,
        .stSelectbox>div>div:focus-within {
            border-color: #0288D1;
            box-shadow: 0 6px 15px rgba(2, 136, 209, 0.2);
            transform: scale(1.02);
        }

        /* Result Box with Fade-In */
        .result-box {
            background: #ffffff;
            border: 2px dashed #0288D1;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            margin-top: 30px;
            animation: fadeInUp 0.8s ease-in-out;
        }
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Footer with Glow */
        .footer {
            text-align: center;
            padding: 25px;
            background: #e0f7fa;
            border-radius: 15px;
            margin-top: 40px;
            box-shadow: 0 0 20px rgba(2, 136, 209, 0.2);
            animation: glow 2s infinite alternate;
        }
        @keyframes glow {
            from { box-shadow: 0 0 10px rgba(2, 136, 209, 0.2); }
            to { box-shadow: 0 0 20px rgba(2, 136, 209, 0.4); }
        }

        /* Sidebar Styling */
        .sidebar .css-1d391kg {
            background: #e0f7fa;
            border-right: 2px solid #b0bec5;
            box-shadow: 3px 0 10px rgba(0, 0, 0, 0.05);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Unit conversion functions
def convert_length(value, from_unit, to_unit):
    conversions = {
        "meter": 1, "kilometer": 1000, "centimeter": 0.01, "millimeter": 0.001,
        "mile": 1609.34, "yard": 0.9144, "foot": 0.3048, "inch": 0.0254, "nautical mile": 1852,
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        "kilogram": 1, "gram": 0.001, "milligram": 0.000001, "pound": 0.453592,
        "ounce": 0.0283495, "tonne": 1000, "stone": 6.35029,
    }
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
    conversions = {
        "liter": 1, "milliliter": 0.001, "gallon": 3.78541, "quart": 0.946353,
        "pint": 0.473176, "cup": 0.24, "cubic meter": 1000, "cubic foot": 28.3168,
        "cubic inch": 0.0163871,
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_time(value, from_unit, to_unit):
    conversions = {
        "second": 1, "minute": 60, "hour": 3600, "day": 86400, "week": 604800,
        "month": 2628000, "year": 31536000,
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_speed(value, from_unit, to_unit):
    conversions = {
        "meter/second": 1, "kilometer/hour": 0.277778, "mile/hour": 0.44704,
        "foot/second": 0.3048, "knot": 0.514444,
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_area(value, from_unit, to_unit):
    conversions = {
        "square meter": 1, "square kilometer": 1000000, "square mile": 2589988.11,
        "square yard": 0.836127, "square foot": 0.092903, "hectare": 10000,
        "acre": 4046.86,
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_energy(value, from_unit, to_unit):
    conversions = {
        "joule": 1, "kilojoule": 1000, "calorie": 4.184, "kilocalorie": 4184,
        "watt-hour": 3600, "kilowatt-hour": 3600000, "electronvolt": 1.60218e-19,
    }
    return value * conversions[from_unit] / conversions[to_unit]

# Sidebar for unit category selection
st.sidebar.header("📐 Select Unit Category")
unit_category = st.sidebar.selectbox(
    "Choose a category",
    ["Length", "Weight", "Temperature", "Volume", "Time", "Speed", "Area", "Energy"],
    help="Pick the unit type you want to convert!"
)

# Main conversion logic
st.header(f"🔢 {unit_category} Converter")

if unit_category == "Length":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(convert_length.__closure__[0].cell_contents.keys()))
    with col2:
        to_unit = st.selectbox("To", list(convert_length.__closure__[0].cell_contents.keys()))
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    result = convert_length(value, from_unit, to_unit)

elif unit_category == "Weight":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(convert_weight.__closure__[0].cell_contents.keys()))
    with col2:
        to_unit = st.selectbox("To", list(convert_weight.__closure__[0].cell_contents.keys()))
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    result = convert_weight(value, from_unit, to_unit)

elif unit_category == "Temperature":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["celsius", "fahrenheit", "kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["celsius", "fahrenheit", "kelvin"])
    value = st.number_input("Enter value", format="%.2f")
    result = convert_temperature(value, from_unit, to_unit)

elif unit_category == "Volume":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(convert_volume.__closure__[0].cell_contents.keys()))
    with col2:
        to_unit = st.selectbox("To", list(convert_volume.__closure__[0].cell_contents.keys()))
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    result = convert_volume(value, from_unit, to_unit)

elif unit_category == "Time":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(convert_time.__closure__[0].cell_contents.keys()))
    with col2:
        to_unit = st.selectbox("To", list(convert_time.__closure__[0].cell_contents.keys()))
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    result = convert_time(value, from_unit, to_unit)

elif unit_category == "Speed":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(convert_speed.__closure__[0].cell_contents.keys()))
    with col2:
        to_unit = st.selectbox("To", list(convert_speed.__closure__[0].cell_contents.keys()))
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    result = convert_speed(value, from_unit, to_unit)

elif unit_category == "Area":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(convert_area.__closure__[0].cell_contents.keys()))
    with col2:
        to_unit = st.selectbox("To", list(convert_area.__closure__[0].cell_contents.keys()))
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    result = convert_area(value, from_unit, to_unit)

elif unit_category == "Energy":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(convert_energy.__closure__[0].cell_contents.keys()))
    with col2:
        to_unit = st.selectbox("To", list(convert_energy.__closure__[0].cell_contents.keys()))
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    result = convert_energy(value, from_unit, to_unit)

# Display result with detailed explanation
if st.button("Convert"):
    st.markdown(
        f"""
        <div class="result-box">
            <h3 style="color: #0288D1;">🎉 Conversion Complete!</h3>
            <p><strong>{value:.4f} {from_unit}</strong> equals <strong>{result:.4f} {to_unit}</strong>.</p>
            <p><strong>How it Works:</strong></p>
            <ul>
                <li>The value in <strong>{from_unit}</strong> is converted to <strong>{to_unit}</strong> using standard conversion factors.</li>
                <li>For example, 1 <strong>{from_unit}</strong> = {globals()[f'convert_{unit_category.lower()}'](1, from_unit, to_unit):.4f} <strong>{to_unit}</strong>.</li>
                <li>Your input is multiplied by this factor to get the final result!</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Add a fancy footer
st.markdown(
    """
    <div class="footer">
        <h3 style="color: #0288D1;">🚀 Crafted by Sarfraz Ahmad</h3>
        <p>Unit conversion made simple, fast, and fun!</p>
        <p>Powered by Streamlit & Love 💙</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Bonus: Add a confetti animation on successful conversion (requires external JS)
st.markdown(
    """
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        function triggerConfetti() {
            confetti({
                particleCount: 100,
                spread: 70,
                origin: { y: 0.6 }
            });
        }
    </script>
    """,
    unsafe_allow_html=True,
)
if st.button("Convert"):  # Trigger confetti with the Convert button
    st.markdown("<script>triggerConfetti();</script>", unsafe_allow_html=True)