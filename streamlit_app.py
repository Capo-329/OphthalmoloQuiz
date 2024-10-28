# Import libraries
import streamlit as st

# Add custom CSS for styling
st.markdown("""
    <style>
    .stMain {
        background-color: #fff;
        color: black
    }
    .st-az {
        background-color: #5995f0 ;
    }
    .titolone {
        display: flex;
        align-items: center;
        background-color: #5995f0;
    }
    .h1 {
        color: #5995f0;
        }
    .subheader-text {
        color: #5995f0;
    }
    .section-text {
        color: #2C3E50;
        font-size: 18px;
        margin-top: 20px;
    }
    .quiz-section {
        background-color: #fff;
        padding: 20px;
        border-radius: 10px;
    }
    .score-text {
        color: #5995f0;
        font-size: 24px;
        font-weight: bold;
    }
    .divider {
        height: 5px;
        background-color: #5995f0;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# App title
st.image("logo-MEb.png",width=60) 
st.markdown("""
<div class="titolone">
    <h1 style="color: #fff">Ophthalmoloquiz App by Matteo</h1>
</div>
""", unsafe_allow_html=True)



# Case Presentation
st.subheader("Case Presentation")
st.markdown("A 28-year-old man presents with progressive vision loss, particularly in low-light conditions, starting from adolescence. He is diagnosed with gyrate atrophy of the choroid and retina, an autosomal recessive condition associated with elevated serum ornithine. The patient'high ornithine levels were treated with vitamin B6 (pyridoxine), leading to a significant decrease in serum ornithine.")

# Diagnostic Imaging Findings
st.image("img1.jpg", caption="Fundus view of the right eye", width=400)
st.image("img2.jpg", caption="Fluorescein angiogram", width=400)

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
selected_answers = []
for i, q in enumerate(questions):
    st.write(f"**Question {i+1}:** {q['question']}")
    answer = st.radio("", q['options'], key=f"q_{i}")
    selected_answers.append(answer)

# Display Score and highlight answers
if st.button("Submit Quiz"):
    for i, q in enumerate(questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        if selected_answers[i] == q['answer']:
            st.markdown(f"<p style='color:green;'>✔️{selected_answers[i]}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color:red;'>❌{selected_answers[i]}</p>", unsafe_allow_html=True)
 
