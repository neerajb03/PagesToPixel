import streamlit as st

def show():
    # Add animation effect
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    # Main content layout
    st.title("Pages To Pixels")
    st.markdown("##### Transform documents into engaging videos with minimal effort")
    
    # Main content in two columns
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # Description with enhanced card
        st.markdown("""
        <div class="card">
            <h3>Simplify Your Content</h3>
            <p>Upload documents and transform them into clean, engaging video presentations with AI avatars.</p>
            <p>Designed for:</p>
            <ul>
                <li>Students reviewing study materials</li>
                <li>Professionals creating presentations</li>
                <li>Anyone converting text to video</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Call to action - improved styling
        if st.button("Start Now", key="cta_button"):
            st.session_state.current_page = "GUI"
            st.rerun()
            
    with col2:
        # Simple process steps
        st.markdown("""
        <div class="card">
            <h4>How It Works</h4>
            <ol style="padding-left: 1.2rem;">
                <li>Upload your document</li>
                <li>Choose summary preferences</li>
                <li>Generate video with AI avatar</li>
                <li>Download or share</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    # Features section - enhanced cards in columns with improved color scheme
    st.markdown("### Key Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h4>Multiple File Types</h4>
            <p>PDF, DOCX, and PPTX support</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h4>Custom Summaries</h4>
            <p>Control text length and format</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h4>AI Avatars</h4>
            <p>Professional video narration</p>
        </div>
        """, unsafe_allow_html=True)
    
    # End animation div
    st.markdown('</div>', unsafe_allow_html=True)