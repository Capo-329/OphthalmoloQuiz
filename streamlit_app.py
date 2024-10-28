import streamlit as st

def main():
    st.title("Quizzone")

# App title
st.image("logo-MEb.png",width=60) 
st.markdown("""
<div class="titolone">
    <h1>Ophthalmoloquiz App by Matteo</h1>
</div>
""", unsafe_allow_html=True)
    
    # Introduction Screen
    st.write("Welcome to Quizzone!")
    st.image("intro_image.jpg")  # Replace with your image path
    if st.button("Start Quiz"):
        question_1()

def question_1():
    st.write("Question 1:")
    st.write("Placeholder Question Text")

    # Create radio button options
    options = ["Option A", "Option B", "Option C", "Option D"]
    selected_option = st.radio("Select your answer:", options)

    # Check the answer and provide feedback
    if st.button("Submit"):
        if selected_option == "Correct Answer":  # Replace with the correct answer
            st.success("Correct!")
        else:
            st.error("Incorrect. Please try again.")

    if st.button("Continue"):
        question_2()

def question_2():
    # Similar structure to question_1
    # ...

# Run the app
 if __name__ == "__main__":
    main()
