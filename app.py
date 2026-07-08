import streamlit as st
import google.generativeai as genai

# -----------------------------
# CONFIGURE GEMINI
# -----------------------------
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash-lite")

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="AI Learning Buddy Hasini",
    page_icon="🎓",
    layout="centered"
)

# -----------------------------
# TITLE
# -----------------------------
st.markdown(
    "<h1 style='text-align:center;'>🎓 AI Learning Buddy Hasini</h1>",
    unsafe_allow_html=True
)

st.write("")

# -----------------------------
# PERSONA
# -----------------------------
persona = """
You are Hasini, a friendly and patient tutor.
Explain concepts in simple language.
Use real-life examples.
Encourage the learner.
"""

# -----------------------------
# USER INPUT
# -----------------------------
topic = st.text_input(
    "Enter a Topic",
    placeholder="Example: Deep Learning"
)

activity = st.selectbox(
    "Choose Activity",
    (
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask a Doubt",
        "Complete Learning Session"
    )
)

# -----------------------------
# GENERATE BUTTON
# -----------------------------
if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
        st.stop()

    if activity == "Explain Concept":

        prompt = f"""
        {persona}

        Explain {topic} in simple language.

        Use one analogy.

        Keep it short.
        """

    elif activity == "Real-Life Example":

        prompt = f"""
        {persona}

        Give one real-life example of {topic}.

        Explain simply.
        """

    elif activity == "Generate Quiz":

        prompt = f"""
        {persona}

        Create 5 MCQs on {topic}.

        Each question should have:

        A)

        B)

        C)

        D)

        Then provide:

        Correct Answer

        Explanation
        """

    elif activity == "Ask a Doubt":

        prompt = f"""
        {persona}

        Answer the student's doubt about:

        {topic}

        Use beginner-friendly language.
        """

    elif activity == "Complete Learning Session":

        prompt = f"""
        {persona}

        Teach {topic} step by step.

        Include:

        • Greeting

        • Explanation

        • Real-life example

        • One quiz question

        • Feedback

        • Motivation
        """

    with st.spinner("Generating..."):

        response = model.generate_content(prompt)

    st.markdown("## 📖 Output")

    st.write(response.text)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("Capstone Project | AI Learning Buddy Hasini | Streamlit + Gemini")