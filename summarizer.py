import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_articles(articles):
    summaries = []
    for article in articles:
        prompt = f"""Resume esta noticia en exactamente 3 líneas en español.
Sé conciso y directo. No uses bullet points.

Título: {article['title']}
Contenido: {article['summary']}"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        summaries.append({
            **article,
            "ai_summary": response.choices[0].message.content
        })
    return summaries