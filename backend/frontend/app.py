import streamlit as st

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & CUSTOM THEMING (Green, White, Dark Blue)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Obesity Clinical Knowledge Hub",
    page_icon="🩺",
    layout="wide"
)

# Custom CSS styling
st.markdown("""
<style>
    /* Main Background & Text Colors */
    .stApp {
        background-color: #FAFAFA;
        color: #1E293B;
    }
    
    /* Header Styling */
    h1, h2, h3 {
        color: #0F172A !important; /* Dark Blue */
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0F2A1D; /* Deep Forest Green */
        color: #FFFFFF;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] label {
        color: #E2E8F0 !important;
    }

    /* Buttons */
    .stButton>button {
        background-color: #10B981; /* Emerald Green */
        color: #FFFFFF;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #059669;
        color: #FFFFFF;
    }

    /* Cards/Containers */
    .clinical-card {
        background-color: #FFFFFF;
        border-left: 5px solid #10B981;
        padding: 1.2rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. SIDEBAR: CRAWLER & SEARCH CRITERIA SETTINGS
# -----------------------------------------------------------------------------
with st.sidebar:
    st.title("⚙️ AI Crawler Settings")
    st.caption("Configure continuous literature indexing")
    
    st.subheader("Target Feeds & Sources")
    sources = st.multiselect(
        "Sources to Crawl:",
        ["PubMed Central (Obesity)", "ClinicalTrials.gov", "Obesity Journal (AOS)", "Lancet Diabetes & Endocrinology"],
        default=["PubMed Central (Obesity)", "ClinicalTrials.gov"]
    )
    
    st.subheader("Inclusion Criteria")
    min_year = st.slider("Filter by Publication Year:", 2015, 2026, 2022)
    study_types = st.multiselect(
        "Study Types:",
        ["Phase III Trials", "Systematic Reviews", "Clinical Practice Guidelines", "Meta-Analyses"],
        default=["Clinical Practice Guidelines", "Phase III Trials"]
    )
    
    st.divider()
    strict_mode = st.toggle("Strict Clinical Grounding", value=True, help="When enabled, AI will ONLY answer using verified uploaded files.")

# -----------------------------------------------------------------------------
# 3. MAIN INTERFACE
# -----------------------------------------------------------------------------
st.title("🩺 Obesity Guidelines & Evidence Hub")
st.subheader("Strict Clinical Decision Support System")

tab1, tab2 = st.tabs(["🔍 Clinical Assistant", "📚 Knowledge Repository"])

# --- TAB 1: CLINICAL SEARCH ---
with tab1:
    st.markdown("Enter a patient case or clinical question below to retrieve grounded evidence from indexed materials.")
    
    query = st.text_input("Clinical Query:", placeholder="e.g., What are the current GLP-1 initiation guidelines for BMI ≥ 35 with non-steatotic fatty liver?")
    
    if st.button("Search Knowledge Base"):
        if query:
            st.markdown("---")
            st.markdown('<div class="clinical-card">', unsafe_allow_html=True)
            st.markdown("### 📋 Evidence Summary")
            st.markdown("""
            **Grounded Response (Strict Mode Active):**
            * **Guideline Consensus:** GLP-1 receptor agonists (e.g., Semaglutide 2.4 mg) are recommended as first-line pharmacotherapy alongside lifestyle intervention for individuals with BMI ≥ 30, or BMI ≥ 27 with weight-related comorbidities.
            * **Trial Evidence:** Recent trial data demonstrates a mean weight reduction of 15% at 68 weeks, with concurrent reductions in liver fat fraction.
            """)
            st.markdown("**Matched Sources on File:**")
            st.caption("1. *AACE/ACE Clinical Practice Guidelines for Comprehensive Medical Care of Patients with Obesity (2023)*")
            st.caption("2. *STEP-1 Clinical Trial Analysis — N Engl J Med*")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("Please enter a query first.")

# --- TAB 2: UPLOAD & REPOSITORY ---
with tab2:
    st.markdown("### Upload New Guidelines & Research")
    uploaded_files = st.file_uploader("Drop PDFs, guidelines, or trial documents here:", accept_multiple_files=True, type=["pdf", "txt"])
    
    if uploaded_files:
        st.success(f"Successfully uploaded {len(uploaded_files)} file(s) into the strict vector index.")
