import streamlit as st

# Streamlit app configuration
st.set_page_config(page_title="✨ Unit Converter Elite", layout="wide", page_icon="✨")
st.title("✨ Unit Converter Elite")

# Custom Styling for Elegant UI/UX
st.markdown(
    """
    <style>
        /* General Styling */
        body {
            font-family: 'Lora', serif; /* Elegant serif font */
            background: linear-gradient(120deg, #1A1A2E, #16213E); /* Deep, luxurious gradient */
            color: #E0E0E0; /* Soft white text */
            margin: 0;
            padding: 0;
        }
        .stApp {
            padding: 40px;
            max-width: 1200px;
            margin: auto; /* Center the app */
        }

        /* Header Animation */
        @keyframes floatIn {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .stHeader {
            animation: floatIn 1.5s ease-out;
            font-size: 3.2rem;
            font-weight: 600;
            color: #FFD700; /* Gold accent for elegance */
            text-shadow: 0 2px 10px rgba(255, 215, 0, 0.3);
            margin-bottom: 35px;
            text-align: center;
        }

        /* Button Styling with Subtle Shine */
        .stButton>button {
            background: linear-gradient(45deg, #FFD700, #DAA520);
            color: #1A1A2E;
            border: none;
            border-radius: 20px;
            padding: 14px 30px;
            font-size: 18px;
            font-weight: 500;
            letter-spacing: 1px;
            transition: all 0.4s ease;
            box-shadow: 0 5px 15px rgba(255, 215, 0, 0.4);
        }
        .stButton>button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(255, 215, 0, 0.6);
            background: linear-gradient(45deg, #DAA520, #FFD700);
        }

        /* Input Fields with Glassmorphism */
        .stNumberInput>div>div,
        .stSelectbox>div>div {
            background: rgba(255, 255, 255, 0.1); /* Glass effect */
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            padding: 12px;
            backdrop-filter: blur(10px); /* Glassmorphism blur */
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            color: #E0E0E0;
            transition: all 0.3s ease;
        }
        .stNumberInput>div>div:focus-within,
        .stSelectbox>div>div:focus-within {
            border-color: #FFD700;
            box-shadow: 0 6px 20px rgba(255, 215, 0, 0.3);
            transform: scale(1.02);
        }

        /* Result Box with Luxurious Animation */
        .result-box {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 215, 0, 0.2);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            margin-top: 40px;
            animation: reveal 1s ease-in-out;
            backdrop-filter: blur(8px);
        }
        @keyframes reveal {
            from { opacity: 0; transform: scale(0.95); }
            to { opacity: 1; transform: scale(1); }
        }

        /* Footer with Elegant Glow */
        .footer {
            text-align: center;
            padding: 30px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            margin-top: 50px;
            box-shadow: 0 0 25px rgba(255, 215, 0, 0.2);
            animation: subtleGlow 3s infinite alternate;
        }
        @keyframes subtleGlow {
            from { box-shadow: 0 0 15px rgba(255, 215, 0, 0.2); }
            to { box-shadow: 0 0 25px rgba(255, 215, 0, 0.4); }
        }

        /* Sidebar Styling */
        .sidebar .css-1d391kg {
            background: rgba(255, 255, 255, 0.05);
            border-right: 1px solid rgba(255, 215, 0, 0.2);
            box-shadow: 3px 0 15px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(10px);
        }
        .sidebar h1 {
            color: #FFD700;
            text-shadow: 0 2px 10px rgba(255, 215, 0, 0.3);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Unit conversion functions (same as before, abbreviated for brevity)
def convert_length(value, from_unit, to_unit):
    conversions = {"meter": 1, "kilometer": 1000, "centimeter": 0.01, "millimeter": 0.001, "mile": 1609.34, "yard": 0.9144, "foot": 0.3048, "inch": 0.0254, "nautical mile": 1852}
    return value * conversions[from_unit] / conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {"kilogram": 1, "gram": 0.001, "milligram": 0.000001, "pound": 0.453592, "ounce": 0.0283495, "tonne": 1000, "stone": 6.35029}
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
    conversions = {"liter": 1, "milliliter": 0.001, "gallon": 3.78541, "quart": 0.946353, "pint": 0.473176, "cup": 0.24, "cubic meter": 1000, "cubic foot": 28.3168, "cubic inch": 0.0163871}
    return value * conversions[from_unit] / conversions[to_unit]

def convert_time(value, from_unit, to_unit):
    conversions = {"second": 1, "minute": 60, "hour": 3600, "day": 86400, "week": 604800, "month": 2628000, "year": 31536000}
    return value * conversions[from_unit] / conversions[to_unit]

def convert_speed(value, from_unit, to_unit):
    conversions = {"meter/second": 1, "kilometer/hour": 0.277778, "mile/hour": 0.44704, "foot/second": 0.3048, "knot": 0.514444}
    return value * conversions[from_unit] / conversions[to_unit]

def convert_area(value, from_unit, to_unit):
    conversions = {"square meter": 1, "square kilometer": 1000000, "square mile": 2589988.11, "square yard": 0.836127, "square foot": 0.092903, "hectare": 10000, "acre": 4046.86}
    return value * conversions[from_unit] / conversions[to_unit]

def convert_energy(value, from_unit, to_unit):
    conversions = {"joule": 1, "kilojoule": 1000, "calorie": 4.184, "kilocalorie": 4184, "watt-hour": 3600, "kilowatt-hour": 3600000, "electronvolt": 1.60218e-19}
    return value * conversions[from_unit] / conversions[to_unit]

# Sidebar for unit category selection
st.sidebar.header("⚙️ Conversion Category")
unit_category = st.sidebar.selectbox(
    "Select a Category",
    ["Length", "Weight", "Temperature", "Volume", "Time", "Speed", "Area", "Energy"],
    help="Choose the type of units to convert with elegance."
)

# Main conversion logic with elegant layout
st.header(f"🔮 {unit_category} Conversion")

# Centered input layout
col1, col2, col3 = st.columns([1, 2, 1])  # Adjusted for balance
with col2:
    if unit_category == "Length":
        from_unit = st.selectbox("From Unit", list(convert_length.__closure__[0].cell_contents.keys()), key="length_from")
        to_unit = st.selectbox("To Unit", list(convert_length.__closure__[0].cell_contents.keys()), key="length_to")
        value = st.number_input("Value", min_value=0.0, format="%.4f", key="length_value")
        result = convert_length(value, from_unit, to_unit)

    elif unit_category == "Weight":
        from_unit = st.selectbox("From Unit", list(convert_weight.__closure__[0].cell_contents.keys()), key="weight_from")
        to_unit = st.selectbox("To Unit", list(convert_weight.__closure__[0].cell_contents.keys()), key="weight_to")
        value = st.number_input("Value", min_value=0.0, format="%.4f", key="weight_value")
        result = convert_weight(value, from_unit, to_unit)

    elif unit_category == "Temperature":
        from_unit = st.selectbox("From Unit", ["celsius", "fahrenheit", "kelvin"], key="temp_from")
        to_unit = st.selectbox("To Unit", ["celsius", "fahrenheit", "kelvin"], key="temp_to")
        value = st.number_input("Value", format="%.2f", key="temp_value")
        result = convert_temperature(value, from_unit, to_unit)

    elif unit_category == "Volume":
        from_unit = st.selectbox("From Unit", list(convert_volume.__closure__[0].cell_contents.keys()), key="volume_from")
        to_unit = st.selectbox("To Unit", list(convert_volume.__closure__[0].cell_contents.keys()), key="volume_to")
        value = st.number_input("Value", min_value=0.0, format="%.4f", key="volume_value")
        result = convert_volume(value, from_unit, to_unit)

    elif unit_category == "Time":
        from_unit = st.selectbox("From Unit", list(convert_time.__closure__[0].cell_contents.keys()), key="time_from")
        to_unit = st.selectbox("To Unit", list(convert_time.__closure__[0].cell_contents.keys()), key="time_to")
        value = st.number_input("Value", min_value=0.0, format="%.4f", key="time_value")
        result = convert_time(value, from_unit, to_unit)

    elif unit_category == "Speed":
        from_unit = st.selectbox("From Unit", list(convert_speed.__closure__[0].cell_contents.keys()), key="speed_from")
        to_unit = st.selectbox("To Unit", list(convert_speed.__closure__[0].cell_contents.keys()), key="speed_to")
        value = st.number_input("Value", min_value=0.0, format="%.4f", key="speed_value")
        result = convert_speed(value, from_unit, to_unit)

    elif unit_category == "Area":
        from_unit = st.selectbox("From Unit", list(convert_area.__closure__[0].cell_contents.keys()), key="area_from")
        to_unit = st.selectbox("To Unit", list(convert_area.__closure__[0].cell_contents.keys()), key="area_to")
        value = st.number_input("Value", min_value=0.0, format="%.4f", key="area_value")
        result = convert_area(value, from_unit, to_unit)

    elif unit_category == "Energy":
        from_unit = st.selectbox("From Unit", list(convert_energy.__closure__[0].cell_contents.keys()), key="energy_from")
        to_unit = st.selectbox("To Unit", list(convert_energy.__closure__[0].cell_contents.keys()), key="energy_to")
        value = st.number_input("Value", min_value=0.0, format="%.4f", key="energy_value")
        result = convert_energy(value, from_unit, to_unit)

    # Convert button centered
    if st.button("Convert Now"):
        st.markdown(
            f"""
            <div class="result-box">
                <h3 style="color: #FFD700;">🌟 Result Unveiled!</h3>
                <p><strong>{value:.4f} {from_unit}</strong> transforms to <strong>{result:.4f} {to_unit}</strong>.</p>
                <p><strong>Insight:</strong></p>
                <ul style="font-style: italic;">
                    <li>Conversion leverages precise factors relative to the base unit.</li>
                    <li>Example: 1 <strong>{from_unit}</strong> = {globals()[f'convert_{unit_category.lower()}'](1, from_unit, to_unit):.4f} <strong>{to_unit}</strong>.</li>
                    <li>Elegance in precision, delivered instantly!</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Elegant footer
st.markdown(
    """
    <div class="footer">
        <h3 style="color: #FFD700;">✨ Crafted by Sarfraz Ahmad</h3>
        <p style="font-style: italic;">Experience the art of conversion with timeless elegance.</p>
        <p>Powered by Precision & Passion</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Bonus: Particle Animation for Extra Elegance
st.markdown(
    """
    <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
    <div id="particles-js" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;"></div>
    <script>
        particlesJS("particles-js", {
            "particles": {
                "number": { "value": 50, "density": { "enable": true, "value_area": 800 } },
                "color": { "value": "#FFD700" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.5, "random": true },
                "size": { "value": 3, "random": true },
                "line_linked": { "enable": false },
                "move": { "enable": true, "speed": 1, "direction": "none", "random": true, "out_mode": "out" }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": { "onhover": { "enable": true, "mode": "repulse" }, "onclick": { "enable": true, "mode": "push" } },
                "modes": { "repulse": { "distance": 100, "duration": 0.4 }, "push": { "particles_nb": 4 } }
            },
            "retina_detect": true
        });
    </script>
    """,
    unsafe_allow_html=True,
)