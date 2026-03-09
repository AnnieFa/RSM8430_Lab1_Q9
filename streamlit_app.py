import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Annie Fa | Interactive Resume", page_icon="📊", layout="wide")

# --- SIDEBAR: PERSONAL INFO ---
with st.sidebar:
    st.title("Annie Fa, P.Eng")
    st.write("📍 Toronto, Ontario")
    st.write("📧 [annie.fa@rotman.utoronto.ca](mailto:annie.fa@rotman.utoronto.ca)")
    st.write("🔗 [LinkedIn Profile](https://www.linkedin.com/in/annie-fa/)")
    
    # WIDGET 1: Selectbox for Language Toggle
    lang = st.selectbox("Preferred Language / 语言选择", ["English", "Mandarin (中文)"])
    if lang == "Mandarin (中文)":
        st.info("Annie is proficient in Mandarin. (Annie 精通普通话。)")

# --- HEADER ---
st.title("Wanchun (Annie) Fa, P.Eng")
st.subheader("Master of Management Analytics Candidate | Rotman School of Management")
st.write("""
MMA candidate with 4 years in management consulting, advising on investment evaluation, 
market analysis, and operational review for transactions exceeding US$1B.
""")

# --- INTERACTIVE PORTFOLIO SECTION ---
st.divider()
st.header("🛠️ Interactive Portfolio")

col1, col2, col3 = st.columns(3)

with col1:
    # WIDGET 2: Slider to filter experience impact
    exp_year = st.slider("Filter Impact by Year at Hatch Ltd.", 2021, 2025, 2021)
    
with col2:
    # WIDGET 3: Radio button to toggle technical focus (NEW)
    focus = st.radio("Select Professional Focus:", ["Management Consulting", "Technical Projects"])

with col3:
    # WIDGET 4: Checkbox to show/hide extra details
    show_tech = st.checkbox("Show Detailed Descriptions")

# Logic for Interactive Content
st.write(f"### Highlighted {focus} Impact ({exp_year}):")

if focus == "Management Consulting":
    if exp_year == 2021:
        st.write("- Built a financial model for a power plant that improved economics by 15%.")
    elif exp_year >= 2024:
        st.write("- Enabled a US$300M lithium investment by translating technical insights into financial risks.")
    else:
        st.write("- Designed and launched an executive Power BI dashboard in 3 days.")
else:
    st.write("- Developed an algorithm to match and rank properties based on user preference using Python.")
    if show_tech:
        st.write("- Automated text conversion using Python and Excel VBA, expediting schedules by one week.")

# --- SKILLS CHART ---
st.divider()
st.header("📈 Skills Proficiency")

skills_data = {
    "Skill": ["Python", "Excel VBA", "Power BI", "Financial Modeling", "Market Analysis", "Strategic Thinking"],
    "Level": [90, 85, 95, 95, 90, 100]
}
df_skills = pd.DataFrame(skills_data)

fig = px.bar(df_skills, x='Level', y='Skill', orientation='h', 
             title="Self-Assessed Proficiency Score",
             color='Level', color_continuous_scale='Viridis')
st.plotly_chart(fig, use_container_width=True)

# --- TABLES SECTION ---
st.divider()
col_left, col_right = st.columns(2)

with col_left:
    st.header("🎓 Education")
    edu_data = {
        "Degree": ["Master of Management Analytics", "B.A.Sc. Chemical Engineering"],
        "Institution": ["Rotman (U of T)", "University of Toronto"],
        "Year": ["2026 (Candidate)", "2021"]
    }
    # Using st.dataframe with hide_index=True for a cleaner look
    st.dataframe(pd.DataFrame(edu_data), hide_index=True, use_container_width=True)

with col_right:
    st.header("💼 Core Competencies")
    comp_data = {
        "Competency": ["Experienced 'Translator'", "Persuasive Presenter", "Structured Thinker", "Problem Solver"]
    }
    # Hiding the index here as well
    st.dataframe(pd.DataFrame(comp_data), hide_index=True, use_container_width=True)