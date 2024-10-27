import streamlit as st

# Import libraries
import streamlit as st

# App title
st.title("Clinical Case Study: Toxoplasmic Chorioretinitis")

# Introduction
st.markdown("""
### Case Overview
This case describes a 57-year-old woman with acute acquired toxoplasmic chorioretinitis.
The following case study will explore her symptoms, diagnosis through advanced imaging techniques, and clinical findings.
""")

# Case Presentation
st.subheader("Case Presentation")
st.write("""
A 57-year-old white woman presented with:
- **Symptoms**: Ocular pain and blurred vision in her left eye.
- **Visual Acuity**: 20/20 in the right eye, 20/200 in the left eye.
- **Findings**: Anterior segment of the left eye showed aqueous flare, cells, and keratic precipitates; 
  fundus exam revealed intense vitritis and focal necrotizing retinochoroiditis above the optic disc.
- **Diagnosis**: Suspected primary ocular toxoplasmosis, confirmed via positive serology for *Toxoplasma gondii*.
""")

# Diagnostic Imaging Findings
st.subheader("Diagnostic Imaging")
st.write("""
The patient underwent swept-source optical coherence tomography (SS-OCT) and optical coherence tomography angiography (OCTA).
- **SS-OCT Findings**: Retinal and choroidal involvement with swelling and inflammation.
- **OCTA Findings**: Complete loss of deep and superficial capillary networks in the inflamed area.
- **Post-Healing Imaging**: Retinal thinning and persistent vascular occlusion noted.
""")

# Treatment and Outcome
st.subheader("Treatment and Outcome")
st.write("""
The patient received a combination of antibiotics (pyrimethamine and sulfadiazine) and steroids (prednisone).
- **Outcome**: Inflammation resolved after two months, leaving an atrophic chorioretinal scar. 
- **Visual Acuity Post-Treatment**: Improved to 20/25 in the affected eye.
""")

# Quiz Section
st.subheader("Clinical Quiz")
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
    st.write(f"Your Score: {score} / {len(questions)}")
    if score == len(questions):
        st.success("Great job! You understand this case well.")
    else:
        st.info("Review the case details and try again for a better score!")
