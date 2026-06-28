from scraper import get_articles
from summarizer import summarize_articles

print("🔍 Buscando noticias...")
articles = get_articles(topic="tecnologia")
print(f"✅ {len(articles)} noticias encontradas\n")

print("🤖 Resumiendo con IA...")
summaries = summarize_articles(articles[:2])  # solo 2 para probar

for s in summaries:
    print(f"\n📰 {s['title']}")
    print(f"🔗 {s['link']}")
    print(f"📝 {s['ai_summary']}")
    print("-" * 50)