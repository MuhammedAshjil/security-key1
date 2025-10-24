import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title=" Security Key", layout="wide")

# Add custom CSS for animated gradient background
st.markdown("""
    <style>
    /* Animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }
    
    /* Style the title with interactive animation */
    h1 {
        background: linear-gradient(90deg, #3AAB98, #2d8a7a, #3AAB98);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: none;
        text-align: center;
        padding: 20px 0;
        transition: all 0.3s ease;
        cursor: default;
        filter: drop-shadow(0 0 10px #3AAB98) drop-shadow(0 0 20px #3AAB98) drop-shadow(0 0 30px #3AAB98);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from {
            filter: drop-shadow(0 0 10px #FFFFFF) drop-shadow(0 0 20px #3AAB98);
        }
        to {
            filter: drop-shadow(0 0 20px #FFFFFF) drop-shadow(0 0 30px #3AAB98) drop-shadow(0 0 40px #3AAB98);
        }
    }
    
    h1:hover {
        transform: scale(1.05);
        letter-spacing: 2px;
    }
    
    /* Style the caption */
    .caption {
        color: white;
        text-align: center;
        font-size: 1.1em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    /* Add subtle shadow to image container with hover effect and gradient border */
    .stImage {
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        transition: all 0.4s ease;
        padding: 5px;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #f7b731, #ff6b6b);
        background-size: 300% 300%;
        animation: borderGradient 3s ease infinite;
    }
    
    @keyframes borderGradient {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }
    
    .stImage:hover {
        transform: scale(1.05) translateY(-10px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.5);
        filter: brightness(1.1);
    }
    
    /* Style for the actual image */
    .stImage img {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Treassure Hunt by BCA")

# Add spacing
st.write("")
st.write("")

# Display the image centered with fixed size
try:
    # Load the image
    image = Image.open("images/5.png")
    
    # Center the image using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image(image, width=600)
        
except FileNotFoundError:
    st.error("Image file not found. Please make sure the image is in the correct path.")
    st.info("Expected path: images/5.png")
except Exception as e:
    st.error(f"Error loading image: {e}")

# Add spacing
st.write("")
st.write("")
