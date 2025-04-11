import streamlit as st
from PIL import Image

# ------------------ CONFIGURATION ------------------
st.set_page_config(page_title="Humaira Halder Portfolio", layout="wide")

# ------------------ SIDEBAR ------------------
with st.sidebar:
    # Profile Image (Uncomment and add 'profile.jpg' to the directory to use it)
    # profile_image = Image.open("profile.jpg")
    # st.image(profile_image, width=200)

    # Basic Info
    st.title("Humaira Halder")
    st.write("🌍 Kolkata, India")
    st.write("📧 humaira.halder24-26@bibs.co.in")
    st.write("📞 7478051931")

    # Social Media
    st.markdown("### 🔗 Connect with me")
    st.markdown("""
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://linkedin.com/in/debkumar-bera)
    """)

# ------------------ MAIN CONTENT ------------------

# Title
st.title("💼 Personal Portfolio")

# Summary
st.header("🔍 Summary")
st.write("""
Aspiring Business Analyst with a foundation in Data Analysis, Data Science, and problem-solving. 
Skilled in collecting, organizing, and interpreting data to support decision-making and process improvement. 
Enthusiastic about using analytical methods to explore insights, refine business performance, and implement data-driven approaches.
""")

# Education
st.header("🎓 Education")
st.write("""
- MBA in Business Analysis & Data Science – Bengal Institute of Business Studies, Kolkata (07/2024 – Present)
- Bachelor in Business Administration – Global Group of Institution, Haldia (06/2021 – 06/2024) – 64%
- Higher Secondary (Science) – Rajnagar Union High School (WBCHSE), Paschim Medinipur (2019 – 2021) – 60%%
""")

# Experience
st.header("💼 Experience")
st.write("""
*Sales Executive* – Agarwal Packers & Movers LTD, Chennai (08/2023 – 12/2023)
- Managed customer data, handled inquiries, generated quotations, negotiated deals, and finalized bookings.
- Strengthened communication skills through customer and stakeholder interactions.
- Gained experience in CRM systems, data handling, and process optimization.
""")

# Skills
st.header("🛠 Skills")
cols = st.columns(2)
with cols[0]:
    st.write("""
    - Python
    - SQL
    - Power BI
    - Advanced Excel
    """)
with cols[1]:
    st.write("""
    - MS PowerPoint, Word, Access
    - Collaboration
    - Problem-Solving & Critical Thinking
    - Time Management
    """)

# Projects
st.header("🚀 Projects")
st.write("""
*Customer Churn Data Analysis*
- Conducted analysis on 7,043 customers, identifying key churn factors.
- Applied Logistic Regression and Random Forest models to predict churn.
- Segmented high-risk customers and visualized churn trends.

*Unemployment Data Analysis*
- Built Power BI dashboards to analyze unemployment trends by age, gender, and year.
- Identified patterns and year-wise visual trends for insights.

*Shivshakti Sales Dashboard*
- Developed an interactive Power BI dashboard to monitor sales, profits ($37K), and trends.
- Analyzed top products and payment behaviors to support decision-making.
""")

# Certifications
st.header("📜 Certifications")
st.write("""
- Machine Learning with Python – IIT Kanpur
- Data Analysis Using SQL – Blinkit
- Power BI Fundamentals
""")

# Achievements
st.header("🏆 Achievements")
st.write("""
- Hands-on project implementations with real business value.
- Built analytical dashboards used for decision support.
- Applied machine learning to improve business insights.
""")

# Hobbies
st.header("🎨 Hobbies")
st.write("""
- 🏏 Cricket
- 🍳 Cooking
- 🎬 Watching Movies
""")