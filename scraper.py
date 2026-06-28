import feedparser

FEEDS = {
    "tecnologia": [
        "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/section/tecnologia/portada",
        "https://www.xataka.com/index.xml",
    ],
    "economia": [
        "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/section/economia/portada",
    ]
}

def get_articles(topic="tecnologia", max_per_feed=3):
    articles = []
    for feed_url in FEEDS.get(topic, []):
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:max_per_feed]:
            articles.append({
                "title": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "link": entry.get("link", ""),
                "source": feed.feed.get("title", "")
            })
    return articles