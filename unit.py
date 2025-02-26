import streamlit as st

# Streamlit app configuration
st.set_page_config(page_title="📏 Unit Converter", layout="wide", page_icon="📏")
st.title("📏 Unit Converter")

# Custom Styling for enhanced UI/UX (Modern Design)
st.markdown(
    """
    <style>
        /* General Styling */
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #1e1e2f; /* Dark background */
            color: #ffffff; /* White text */
            margin: 0;
            padding: 0;
        }
        .stApp {
            padding: 20px;
        }

        /* Header Animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .stHeader {
            animation: fadeIn 1s ease-in-out;
            font-size: 2.5rem;
            font-weight: bold;
            color: #00d1b2; /* Teal accent */
            margin-bottom: 20px;
        }

        /* Button Styling */
        .stButton>button {
            background: linear-gradient(to right, #00d1b2, #00b5a1);
            color: white;
            border-radius: 12px;
            padding: 12px 24px;
            font-size: 16px;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }

        /* Input Fields */
        .stNumberInput>div>div,
        .stSelectbox>div>div {
            background: #2a2a40;
            border: 1px solid #444;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease-in-out;
            color: #ffffff;
        }
        .stNumberInput>div>div:focus-within,
        .stSelectbox>div>div:focus-within {
            border-color: #00d1b2;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Result Box */
        .result-box {
            background: #2a2a40;
            border: 1px solid #444;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
            animation: fadeIn 1s ease-in-out;
            color: #ffffff;
        }

        /* Footer */
        .footer {
            text-align: center;
            padding: 20px;
            background: #2a2a40;
            border-radius: 12px;
            margin-top: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
            color: #ffffff;
        }

        /* Sidebar Styling */
        .sidebar .css-1d391kg {
            background: #2a2a40;
            border-right: 1px solid #444;
            box-shadow: 2px 0 6px rgba(0, 0, 0, 0.05);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Unit conversion functions
def convert_length(value, from_unit, to_unit):
    """Convert length units."""
    conversions = {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254,
        "nautical mile": 1852,
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    """Convert weight units."""
    conversions = {
        "kilogram": 1,
        "gram": 0.001,
        "milligram": 0.000001,
        "pound": 0.453592,
        "ounce": 0.0283495,
        "tonne": 1000,
        "stone": 6.35029,
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature units."""
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

def convert_volume(value, from_unit, to_unit):
    """Convert volume units."""
    conversions = {
        "liter": 1,
        "milliliter": 0.001,
        "gallon": 3.78541,
        "quart": 0.946353,
        "pint": 0.473176,
        "cup": 0.24,
        "cubic meter": 1000,
        "cubic foot": 28.3168,
        "cubic inch": 0.0163871,
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_time(value, from_unit, to_unit):
    """Convert time units."""
    conversions = {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400,
        "week": 604800,
        "month": 2628000,
        "year": 31536000,
    }
    return value * conversions[from_unit] / conversions[to_unit]

# Sidebar for unit category selection
st.sidebar.header("📐 Select Unit Category")
unit_category = st.sidebar.selectbox(
    "Choose a category", 
    ["Length", "Weight", "Temperature", "Volume", "Time"], 
    help="Select the type of unit you want to convert."
)

# Main conversion logic
st.header(f"🔢 {unit_category} Converter")

if unit_category == "Length":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch", "nautical mile"])
    with col2:
        to_unit = st.selectbox("To", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch", "nautical mile"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    result = convert_length(value, from_unit, to_unit)

elif unit_category == "Weight":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["kilogram", "gram", "milligram", "pound", "ounce", "tonne", "stone"])
    with col2:
        to_unit = st.selectbox("To", ["kilogram", "gram", "milligram", "pound", "ounce", "tonne", "stone"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
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
        from_unit = st.selectbox("From", ["liter", "milliliter", "gallon", "quart", "pint", "cup", "cubic meter", "cubic foot", "cubic inch"])
    with col2:
        to_unit = st.selectbox("To", ["liter", "milliliter", "gallon", "quart", "pint", "cup", "cubic meter", "cubic foot", "cubic inch"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    result = convert_volume(value, from_unit, to_unit)

elif unit_category == "Time":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["second", "minute", "hour", "day", "week", "month", "year"])
    with col2:
        to_unit = st.selectbox("To", ["second", "minute", "hour", "day", "week", "month", "year"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    result = convert_time(value, from_unit, to_unit)

# Display result with detailed explanation
if st.button("Convert"):
    st.markdown(
        f"""
        <div class="result-box">
            <h3 style="color: #00d1b2;">✅ Conversion Successful!</h3>
            <p><strong>{value:.2f} {from_unit}</strong> is equal to <strong>{result:.2f} {to_unit}</strong>.</p>
            <p><strong>Explanation:</strong></p>
            <ul>
                <li><strong>{from_unit}</strong> is converted to <strong>{to_unit}</strong> using the conversion factor.</li>
                <li>The conversion factor for <strong>{from_unit}</strong> to <strong>{to_unit}</strong> is calculated based on their relationship to the base unit.</li>
                <li>For example, 1 <strong>{from_unit}</strong> = {convert_length(1, from_unit, to_unit):.2f} <strong>{to_unit}</strong>.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Add a footer
st.markdown(
    """
    <div class="footer">
        <h3 style="color: #00d1b2;">🚀 Developed by Sarfraz Ahmad</h3>
        <p>Convert units like a pro with this intuitive tool!</p>
    </div>
    """,
    unsafe_allow_html=True,
)