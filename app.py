import streamlit as st
st.set_page_config(layout="wide", page_title="India's Electricity Transition", page_icon="⚡", initial_sidebar_state="collapsed")



# st.markdown("""
# <style>
# /* Force all Plotly SVG text to dark */
# .js-plotly-plot .plotly text {
#     fill: #1A1A1A !important;
# }
# </style>
# """, unsafe_allow_html=True)
st.markdown(
    """
    <style>
    /* 1. Target the main app container and all text elements */
    .stApp, .stMarkdown, p, span, label, .stMetric div {
        color: #1A1A1A !important;
    }

    /* 2. Target all header levels */
    h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
    }

    /* 3. Ensure links don't become invisible */
    a {
        color: #0000EE !important;
    }
    
    /* 4. Fix for sidebar text if you use it */
    [data-testid="stSidebar"] .stMarkdown p {
        color: #1A1A1A !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 1. THE "VISIBLE NAVBAR" CSS
st.markdown("""
    <style>
    /* 1. Remove the huge gap at the top */
    .stAppHeader {
        background-color: rgba(0,0,0,0);
        height: 0px;
    }
    
    .block-container {
        padding-top: 2rem !important; /* Adjust this to move the buttons up or down */
        padding-bottom: 0rem !important;
    }

    /* 2. Make buttons stand out against the background */
    div.stButton > button {
        width: 100%;
        height: 42px;
        border-radius: 10px;
        border: 1px solid #d1d5db;
        background-color: white; /* Solid white so they are visible */
        color: #1f2937;
        font-weight: 600;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: all 0.2s;
    }

    div.stButton > button:hover {
        border-color: #2ecc71;
        color: #2ecc71;
        background-color: #f9fafb;
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)
import streamlit as st

# 1. THE BEAUTIFICATION (CSS)
st.markdown("""
    <style>
    /* Style the button containers */
    [data-testid="stColumn"] {
        display: flex;
        justify-content: center;
    }

    /* Style the buttons themselves */
    div.stButton > button {
        border-radius: 20px;
        border: 1px solid #e0e0e0;
        background-color: white;
        color: #31333F;
        padding: 10px 24px;
        width: 100%;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* Hover effects */
    div.stButton > button:hover {
        border-color: #ff4b4b;
        color: #ff4b4b;
        background-color: #fffafa;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    /* Active/Focus state */
    div.stButton > button:active {
        transform: translateY(0px);
    }
    </style>
""", unsafe_allow_html=True)
import streamlit as st

# 1. CSS FOR THE NAV BAR & TITLE ALIGNMENT
st.markdown("""
    <style>
    /* Align the title and buttons vertically */
    [data-testid="column"] {
        display: flex;
        align-items: center;
    }
    
    /* Clean button styling */
    div.stButton > button {
        border-radius: 15px;
        border: 1px solid #f0f2f6;
        background-color: #f8f9fb;
        transition: all 0.2s;
        width: 100%;
    }

    div.stButton > button:hover {
        border-color: #ff4b4b;
        color: #ff4b4b;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# 2. THE NAVIGATION BAR
# We use a larger weight for the title (3) and smaller for buttons (1.2)
title_col, n1, n2, n3 = st.columns([3, 1.2, 1.2, 1.2])

with title_col:
    st.markdown("<h3 style='margin:0; padding-bottom:10px;'>🚀 Navigation</h3>", unsafe_allow_html=True)

with n1:
    if st.button("📈 Capacity"):
        st.switch_page("pages/1_Growth.py")

with n2:
    if st.button("⚡ Generation"):
        st.switch_page("pages/2_Generation.py")

with n3:
    if st.button("📊 Prediction"):
        st.switch_page("pages/3_Prediction.py")

st.markdown("<hr style='margin-top: 5px; margin-bottom: 25px; opacity: 0.2;'>", unsafe_allow_html=True)



st.markdown(
    """
    <style>
    /* Page background */
    .stApp {
        background: linear-gradient(135deg, #f1f8e9, #e8f5e9);
        color: #2E7D32;
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 3.2rem;
        font-weight: 700;
        color: #2E7D32;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        letter-spacing: -0.8px;
        text-shadow: 0 1px 2px rgba(46, 125, 50, 0.2);
    }

    /* Subtitle */
    .sub-title {
        text-align: center;
        font-size: 1.15rem;
        color: #1B5E20;
        margin-bottom: 1.8rem;
        line-height: 1.5;
        opacity: 0.95;
    }

    /* Basic cards */
    .feature-card {
        background: #F1F8E9;
        border-radius: 16px;
        padding: 1.2rem;
        margin: 0.5rem 0;
        box-shadow: 0 4px 12px rgba(46, 125, 50, 0.12);
        border-top: 3px solid #4CAF50;
        transition: all 0.2s ease;
    }
    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(46, 125, 50, 0.2);
    }

    .card-title {
        font-weight: 600;
        color: #2E7D32;
        font-size: 1.1rem;
        margin-bottom: 0.3rem;
    }

    .card-text {
        font-size: 0.95rem;
        color: #333;
        opacity: 0.9;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #E8F5E9 !important;
    }
    section[data-testid="stSidebar"] .sidebar-content {
        padding-top: 1.5rem;
    }

    /* Button */
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-size: 1rem;
        font-weight: 500;
        box-shadow: 0 2px 6px rgba(76, 175, 80, 0.25);
    }
    .stButton button:hover {
        background-color: #388E3C;
        box-shadow: 0 3px 9px rgba(56, 142, 60, 0.35);
    }

    /* Small divider line */
    .divider {
        height: 1px;
        background: linear-gradient(to right, transparent, #81C784, transparent);
        margin: 1.2rem 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown(
    '<div class="main-title">India’s Electricity Transition Dashboard</div>',
    unsafe_allow_html=True,
)

# Subtitle
st.markdown(
    """
    <div class="sub-title">
        Analysis of India’s journey toward a cleaner, more reliable, and affordable electricity system by visualizing installed capacity, actual generation, and future demand predictions.
    </div>
    """,
    unsafe_allow_html=True,
)

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Feature cards aligned with your pages
cols = st.columns(3)

with cols[0]:
    st.markdown(
        """
        <div class="feature-card">
            <div class="card-title">🔋 Installed Capacity</div>
            <div class="card-text">
                Analysis of India's total electricity capacity at state and national levels.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with cols[1]:
    st.markdown(
        """
        <div class="feature-card">
            <div class="card-title">⚡ Actual Generation</div>
            <div class="card-text">
                Track of how much electricity is actually generated .
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with cols[2]:
    st.markdown(
        """
        <div class="feature-card">
            <div class="card-title"> Future Predictions</div>
            <div class="card-text">
                Demand and renewable‑generation forecasts.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Instruction text
st.markdown(
    """
    <p style="text-align: center; font-size: 1.1rem; color: #333; margin-top: 1.5rem;">
        Select a section from the navbar to begin exploring.
    </p>
    """,
    unsafe_allow_html=True,
)
