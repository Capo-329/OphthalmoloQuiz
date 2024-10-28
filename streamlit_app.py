# Import libraries
import streamlit as st

# Add custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #F0F8FF;
    }
    .title-text {
        color: #2C3E50;
        font-size: 32px;
        font-weight: bold;
    }
    .subheader-text {
        color: #2980B9;
        font-size: 26px;
    }
    .section-text {
        color: #2C3E50;
        font-size: 18px;
        margin-top: 20px;
    }
    .quiz-section {
        background-color: #E8F8FF;
        padding: 20px;
        border-radius: 10px;
    }
    .score-text {
        color: #2980B9;
        font-size: 24px;
        font-weight: bold;
    }
    .divider {
        height: 2px;
        background-color: #2980B9;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and introduction with styling
st.markdown('<div class="title-text">Clinical Case Study: Toxoplasmic Chorioretinitis</div>', unsafe_allow_html=True)
st.markdown("""
### Case Overview
This case involves a 57-year-old woman diagnosed with acute acquired toxoplasmic chorioretinitis.
The following sections outline her symptoms, imaging diagnostics, and outcomes in a detailed way to enhance learning.
""")

# Sidebar with app information
st.sidebar.markdown("### Medical Case Study App")
st.sidebar.info("Navigate through the clinical case, examine the imaging results, and test your knowledge in the quiz section.")

# Case Presentation Section with dividers
st.markdown('<div class="subheader-text">Case Presentation</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-text">
A 57-year-old white woman presented with:
- **Symptoms**: Ocular pain and blurred vision in her left eye.
- **Visual Acuity**: 20/20 in the right eye, 20/200 in the left eye.
- **Findings**: The left eye showed aqueous flare, cells, and keratic precipitates. The fundus exam revealed intense vitritis and focal necrotizing retinochoroiditis above the optic disc.
- **Diagnosis**: Suspected primary ocular toxoplasmosis, confirmed with positive serology for *Toxoplasma gondii*.
</div>
""", unsafe_allow_html=True)

# Diagnostic Imaging Findings
st.markdown('<div class="subheader-text">Diagnostic Imaging</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-text">
The patient underwent the following diagnostic imaging:
- **Swept-source optical coherence tomography (SS-OCT)** revealed retinal and choroidal inflammation and swelling.
- **Optical coherence tomography angiography (OCTA)** indicated a complete loss of deep and superficial capillary networks in the inflamed area.
- **Post-Healing Imaging** showed retinal thinning and persistent vascular occlusion.
</div>
""", unsafe_allow_html=True)

# Treatment and Outcome Section
st.markdown('<div class="subheader-text">Treatment and Outcome</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-text">
The patient received combination therapy with antibiotics (pyrimethamine and sulfadiazine) and corticosteroids (prednisone).
- **Outcome**: Inflammation resolved within two months, leaving an atrophic chorioretinal scar.
- **Visual Acuity Post-Treatment**: Improved to 20/25 in the affected eye.
</div>
""", unsafe_allow_html=True)

# Insert an image with a caption
st.image("clinical_case_image.jpg", caption="OCT Imaging of Toxoplasmic Chorioretinitis", width=700)

# Clinical Quiz Section with box style
st.markdown('<div class="subheader-text">Clinical Quiz</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="quiz-section">', unsafe_allow_html=True)
st.write("Test your knowledge on this case!")

# Quiz Questions
questions = [
    {
        "question": "What was the primary symptom that led the patient to seek medical attention?",
        "options": ["Ocular pain and blurred vision", "Headache", "Dizziness", "Nausea"],
        "answer": "Ocular pain and blurred vision"
    },
    {
        "question": "What imaging technique showed vascular occlusion in the retina?",
        "options": ["MRI", "CT Scan", "SS-OCT", "OCTA"],
        "answer": "OCTA"
    },
    {
        "question": "What organism caused the infection in this case?",
        "options": ["Toxoplasma gondii", "Cytomegalovirus", "Herpes Simplex Virus", "Staphylococcus aureus"],
        "answer": "Toxoplasma gondii"
    },
    {
        "question": "What was the patient's visual acuity in the left eye post-treatment?",
        "options": ["20/20", "20/25", "20/200", "20/50"],
        "answer": "20/25"
    }
]

# Display Quiz
score = 0
for i, q in enumerate(questions):
    st.write(f"**Question {i+1}:** {q['question']}")
    answer = st.radio("", q['options'], key=f"q_{i}")
    if answer == q['answer']:
        score += 1

# Display Score
if st.button("Submit Quiz"):
    st.markdown(f'<div class="score-text">Your Score: {score} / {len(questions)}</div>', unsafe_allow_html=True)
    if score == len(questions):
        st.success("Great job! You understand this case well.")
    else:
        st.info("Review the case details and try again for a better score!")

st.markdown('</div>', unsafe_allow_html=True)  # Close quiz section
