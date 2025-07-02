import os, openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def explain(user_email, station, battery, dest):
    txt = f"User battery {battery}%, going to {dest}, station: {station}"
    resp = openai.ChatCompletion.create(model="gpt‑3.5‑turbo",
        messages=[{"role":"user","content":txt}])
    return resp.choices[0].message.content
