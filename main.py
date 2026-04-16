from agents import optimist_agent, risk_agent, realist_agent, judge_agent

question = input("Enter your decision problem: ")

opt = optimist_agent(question)
risk = risk_agent(question)
real = realist_agent(question)
judge = judge_agent(question, opt, risk, real)

print("\n" + "="*50)
print("DECISION BATTLE AI")
print("="*50)

print("\n" + opt)
print("\n" + risk)
print("\n" + real)
print("\n" + judge)

print("\n" + "="*50)