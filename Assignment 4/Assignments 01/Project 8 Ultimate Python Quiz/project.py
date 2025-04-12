import streamlit as st

# Updated Custom CSS for a New Gradient Background
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #A1C4FD, #C2E9FB, #E0C3FC);
        background-attachment: fixed;
        color: #1f1f1f;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #2c3e50;
        margin-bottom: 20px;
    }
    .question {
        font-weight: 600;
        margin-top: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Quiz Questions
quiz_data = [
    ("Which data structure is mutable?", ["Tuple", "List", "String", "Enum"], "List"),
    ("What keyword is used for defining a function?", ["func", "define", "lambda", "def"], "def"),
    ("Which of these data structures maintains order?", ["Set", "Dictionary", "List", "Enum"], "List"),
    ("How do you check if a key exists in a dictionary?", ["dict.has_key()", "if key in dict", "dict.exists()", "check key dict"], "if key in dict"),
    ("Which statement is used for decision-making?", ["if-else", "loop", "define", "class"], "if-else"),
    ("What is the default value returned by a function if no return statement is used?", ["0", "False", "None", "Empty String"], "None"),
    ("Which data structure stores unique values only?", ["List", "Set", "Dictionary", "Tuple"], "Set"),
    ("How do you define a tuple?", ["[1,2,3]", "(1,2,3)", "{1,2,3}", "'1,2,3'"] , "(1,2,3)"),
    ("Which function is used to get user input?", ["get()", "read()", "input()", "scan()"], "input()"),
    ("Which module in Python is used for working with enumerations?", ["enum_class", "enumlib", "enum", "enumtypes"], "enum")
]

# Title
st.markdown("<div class='title'>💡 Ultimate Python Quiz</div>", unsafe_allow_html=True)
st.write("📝 Select the correct answers and click **Submit** to check your score.")

# Store user answers
user_answers = {}

with st.container():
    for i, (question, options, _) in enumerate(quiz_data):
        st.markdown(f"<div class='question'>Q{i+1}: {question}</div>", unsafe_allow_html=True)
        user_answers[i] = st.radio("", options, key=f"q{i}")

# Submit and Results
total_questions = len(quiz_data)
if st.button("Submit"):
    score = sum(1 for i, (_, _, correct) in enumerate(quiz_data) if user_answers[i] == correct)
    st.balloons()
    st.success(f"✅ You scored {score} out of {total_questions}!")

    # Personalized remarks
    if score > 8:
        st.markdown("🎯 **Excellent! You're a Python Pro!**")
    elif score > 5:
        st.markdown("💡 **Good Job! Keep Practicing.**")
    else:
        st.markdown("📚 **Don't worry, keep learning and you'll improve!**")
