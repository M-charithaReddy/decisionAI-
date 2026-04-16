import streamlit as st
from agents import optimist_agent, risk_agent, realist_agent, judge_agent

st.title("🧠 DECISION AI")

user_input = st.text_area("Enter your decision or problem:")

if st.button("Analyze"):
    if user_input:
        # Run agents first
        opt = optimist_agent(user_input)
        risk = risk_agent(user_input)
        real = realist_agent(user_input)

        # Show results
        st.subheader("Optimist View")
        st.write(opt)

        st.subheader("Risk Analysis")
        st.write(risk)

        st.subheader("Realist View")
        st.write(real)

        # Pass all results to judge
        st.subheader("Final Decision")
        final = judge_agent(user_input, opt, risk, real)
        st.write(final)

    else:
        st.warning("Please enter something first.")