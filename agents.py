from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"


def optimist_agent(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{
            "role": "user",
            "content": f"You are an optimistic advisor. Focus only on benefits.\nQuestion: {question}"
        }]
    )
    return "Optimist:\n" + response.choices[0].message.content


def risk_agent(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{
            "role": "user",
            "content": f"You are a risk analyst. Focus on risks and dangers.\nQuestion: {question}"
        }]
    )
    return "Risk Analyst:\n" + response.choices[0].message.content


def realist_agent(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{
            "role": "user",
            "content": f"You are a realist. Give balanced advice.\nQuestion: {question}"
        }]
    )
    return "Realist:\n" + response.choices[0].message.content


def judge_agent(question, opt, risk, real):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{
            "role": "user",
            "content": f"""
Question: {question}

Optimist:
{opt}

Risk Analyst:
{risk}

Realist:
{real}

Give final decision, explanation, and confidence.
"""
        }]
    )
    return "Final Decision:\n" + response.choices[0].message.content