from youtubesearchpython import VideosSearch

def search_youtube(query):
    results = VideosSearch(query, limit=1).result()

    if not results["result"]:
        return None

    video = results["result"][0]

    return {
        "title": video["title"],
        "duration": video["duration"],
        "thumbnail": video["thumbnails"][0]["url"],
        "url": video["link"]
    }
