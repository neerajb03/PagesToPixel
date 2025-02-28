import streamlit as st
import landing
import GUI
import os

# Set page configuration
st.set_page_config(
    page_title="Pages To Pixels",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for the entire application - enhanced aesthetics with improved color scheme
st.markdown("""
    <style>
        /* Main content styling - clean and minimal */
        .main .block-container {
            padding: 2rem 3rem;
            max-width: 1200px;
        }
        
        /* Enhanced gradient background with new color scheme */
        .stApp {
            background: linear-gradient(135deg, #f0f4f8 0%, #d1dde6 100%);
        }
        
        /* Modern typography with improved contrast */
        h1, h2, h3 {
            color: #1a365d;
            font-weight: 600;
            letter-spacing: -0.5px;
        }
        
        p, li {
            color: #2d3748;
        }
        
        /* Improved button styling with higher contrast */
        .stButton>button {
            border-radius: 6px;
            background-color: #2b6cb0;
            color: white;
            font-weight: 500;
            border: none;
            padding: 0.5rem 1rem;
            transition: all 0.2s ease;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        .stButton>button:hover {
            background-color: #1a4a8d;
            transform: translateY(-1px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        /* Clean sidebar styling with improved aesthetics */
        [data-testid="stSidebar"] {
            background-color: rgba(116,143,191);
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        
        [data-testid="stSidebar"] .stButton>button {
            width: 100%;
            margin-bottom: 0.5rem;
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        [data-testid="stSidebar"] .stButton>button:hover {
            background-color: rgba(255, 255, 255, 0.2);
            color: white;
        }
        
        /* Sidebar text color */
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] h3 {
            color: white;
        }
        
        /* Subtle footer styling */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: rgba(26, 54, 93, 0.9);
            backdrop-filter: blur(5px);
            text-align: center;
            padding: 8px;
            font-size: 12px;
            color: white;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            z-index: 999;
        }
        
        /* Fixed logo that remains visible even when sidebar is collapsed */
        .fixed-logo {
            position: fixed;
            top: 1rem;
            left: 1rem;
            z-index: 1000;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background-color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        
        .fixed-logo img {
            width: 80%;
            height: auto;
            object-fit: contain;
        }
        
        /* Sidebar logo with better sizing and contrast */
        .sidebar-logo {
            text-align: center;
            padding: 1rem;
            margin-bottom: 1rem;
            background-color: white;
            border-radius: 8px;
        }
        
        .sidebar-logo img {
            max-width: 70%;
            height: auto;
        }
        
        /* Smooth animation for page transitions */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .fade-in {
            animation: fadeIn 0.4s ease-out;
        }
        
        /* Card styling with new color scheme */
        .card {
            background-color: white;
            border-radius: 10px;
            padding: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            margin-bottom: 1rem;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            border: 1px solid #e2e8f0;
        }
        
        .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 3px 6px rgba(0,0,0,0.08);
        }
        
        /* Card headers with contrast */
        .card h4 {
            color: #2b6cb0;
            margin-top: 0;
        }
        
        /* Success messaging with better contrast */
        .element-container div[data-testid="stText"] div[class*="stAlert"] {
            background-color: #2b6cb0;
            color: white;
        }
        
        /* Divider line */
        hr {
            margin: 1.5rem 0;
            border: 0;
            height: 1px;
            background-color: rgba(255, 255, 255, 0.2);
        }
        
        /* Adjust main content padding when sidebar is collapsed */
        @media (max-width: 992px) {
            .main .block-container {
                padding-left: 5rem;
            }
        }
    </style>
    <div class="fade-in"></div>
    
    <!-- Fixed logo that remains visible even when sidebar is collapsed -->
    <div class="fixed-logo">
        <img src="Logo.png" alt="Pages To Pixels Logo">
    </div>
""", unsafe_allow_html=True)

# Logo in sidebar with improved styling
st.sidebar.markdown('<div class="sidebar-logo">', unsafe_allow_html=True)
st.sidebar.image("Logo.png")
st.sidebar.markdown('</div>', unsafe_allow_html=True)

# Initialize session state for page tracking
if "current_page" not in st.session_state:
    st.session_state.current_page = "landing"  # Default page

# Function to switch pages with animation
def switch_page(page):
    st.session_state.current_page = page
    st.experimental_rerun()

# Navigation buttons in sidebar with minimal design
st.sidebar.markdown("### Navigate")

# Fixed navigation - Use the name attribute instead of key for consistent button behavior
if st.sidebar.button("🏠 Home", key="home_btn"):
    st.session_state.current_page = "landing"
    st.rerun()
    
if st.sidebar.button("📄 Upload", key="upload_btn"):
    st.session_state.current_page = "GUI"
    st.rerun()

# Minimal divider
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# Brief info section in sidebar
st.sidebar.markdown("""
<div class="card" style="background-color: rgba(255, 255, 255, 0.1); border-color: rgba(255, 255, 255, 0.2);">
    <p style="font-size: 0.9rem; color: white;">Pages To Pixels converts documents into summarized video presentations.</p>
</div>
""", unsafe_allow_html=True)

# Render the selected page based on session state
if st.session_state.current_page == "landing":
    landing.show()
elif st.session_state.current_page == "GUI":
    GUI.show()

# Add minimal footer
st.markdown(
    """
    <div class="footer">
        © 2025 Pages To Pixels
    </div>
    """,
    unsafe_allow_html=True
)