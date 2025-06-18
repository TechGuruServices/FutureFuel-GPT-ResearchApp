import openai
import streamlit as st

st.set_page_config(page_title="Hydrogen Insight AI", layout="wide")
st.title("🔬 Green Hydrogen Research Assistant")

openai.api_key = st.secrets["OPENAI_API_KEY"]

query = st.text_input("Enter a research question about hydrogen fuel:")

if query:
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in hydrogen fuel technologies, electrolyzer design, and energy policy."},
                {"role": "user", "content": query}
            ]
        )
        st.write("**AI Insight:**", response.choices[0].message["content"])
