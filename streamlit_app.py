# Import libraries
import streamlit as st

# Logo
st.image("logo-MEb.png",width=60)
# App title
st.title("Ophthalmoloquiz App by Matteo C")

# Case Presentation
st.subheader("Case Presentation")
st.write("""
A 28-year-old man presents with progressive vision loss, particularly in low-light conditions, starting from adolescence. He is diagnosed with gyrate atrophy of the choroid and retina, an autosomal recessive condition associated with elevated serum ornithine. The patient’s high ornithine levels were treated with vitamin B6 (pyridoxine), leading to a significant decrease in serum ornithine.
""")

# Diagnostic Imaging Findings
st.image("img1.jpg", caption="Fundus view of the right eye", width=200)
st.image("img2.jpg", caption="Fluorescein angiogram", width=200)

# Quiz Section
st.subheader("Clinical Quiz")
st.write("Test your knowledge")

# Quiz Questions
questions = [
    {
        "question": "What are the typical early symptoms of gyrate atrophy of the retina and choroid?",
        "options": ["Gradual vision loss in low-light conditions", "Intense eye pain", "Peripheral field constriction in bright light", "Loss of color vision"],
        "answer": "Gradual vision loss in low-light conditions"
    },
    {
        "question": "In this case, what key laboratory finding led to the diagnosis of gyrate atrophy?",
        "options": ["Elevated plasma ornithine", "High serum creatinine", "Increased retinal pigment deposits", "Abnormal electroretinography"],
        "answer": "Elevated plasma ornithine"
    },
    {
        "question": "Gyrate atrophy is caused by a deficiency in which enzyme?",
        "options": ["Tyrosine aminotransferase", "Ornithine aminotransferase (OAT)", "Pyruvate dehydrogenase", "Glutathione reductase"],
        "answer": "Ornithine aminotransferase (OAT)"
    },
    {
        "question": "This patient’s condition showed a response to high-dose vitamin B6. Why might vitamin B6 be effective in this case?",
        "options": ["It stimulates the production of melanin in the retina", "It serves as a cofactor for the deficient enzyme, ornithine aminotransferase", "It acts as an anti-inflammatory in retinal tissues", "It decreases the permeability of the retinal barrier"],
        "answer": "It serves as a cofactor for the deficient enzyme, ornithine aminotransferase"
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
        st.success("Great job!")
    else:
        st.info("Review the case details and try again for a better score!")
 
