import streamlit as st

# Set page configuration - THIS MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Agricultural Analysis Platform",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for agricultural theme
st.markdown("""
<style>
    .main {
        background-color: #f5f5dc;  /* Beige background */
    }
    .stButton button {
        background-color: #4CAF50;  /* Green */
        color: white;
    }
    h1, h2, h3 {
        color: #2e7d32;  /* Dark green */
    }
    .stSidebar {
        background-color: #e8f5e9;  /* Light green */
    }
    .feature-container {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .feature-title {
        color: #2e7d32;
        font-size: 24px;
        margin-bottom: 10px;
    }
    .feature-description {
        color: #333333;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# App title and description
st.title("🌾 Agricultural Analysis Platform")
st.markdown("""
Welcome to our comprehensive Agricultural Analysis Platform! This platform provides various tools and features 
to help analyze agricultural data and satellite imagery.
""")

# Team information
st.sidebar.title("Team Information")
st.sidebar.info(
    """
    This platform is developed by a collaborative team of agricultural data scientists and engineers.
    """
)

# Main content - Feature cards
st.header("Available Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-container">
        <div class="feature-title">🛰️ Satellite Image Segmentation</div>
        <div class="feature-description">
            Segment agricultural satellite imagery to identify different crop types, soil conditions, and more.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Go to Satellite Image Segmentation", key="satellite_button"):
        st.switch_page("pages/1_Satellite_Image_Segmentation.py")
    
    st.markdown("""
    <div class="feature-container">
        <div class="feature-title">📊 Crop Yield Prediction</div>
        <div class="feature-description">
            Predict crop yields based on historical data, weather patterns, and soil conditions.
        </div>
        <a href="#" target="_self">
            <button style="background-color: #4CAF50; color: white; border: none; padding: 10px 20px; 
            border-radius: 5px; cursor: pointer;">Coming Soon</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-container">
        <div class="feature-title">🌦️ Weather Analysis</div>
        <div class="feature-description">
            Analyze weather patterns and their impact on agricultural productivity.
        </div>
        <a href="#" target="_self">
            <button style="background-color: #4CAF50; color: white; border: none; padding: 10px 20px; 
            border-radius: 5px; cursor: pointer;">Coming Soon</button>
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-container">
        <div class="feature-title">🌱 Soil Health Monitoring</div>
        <div class="feature-description">
            Monitor soil health indicators and get recommendations for improvement.
        </div>
        <a href="#" target="_self">
            <button style="background-color: #4CAF50; color: white; border: none; padding: 10px 20px; 
            border-radius: 5px; cursor: pointer;">Coming Soon</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("© 2025 Agricultural Analysis Platform presented by us the BATATA TEAM ")