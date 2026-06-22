from yt_dlp import YoutubeDL

async def search_youtube(query: str):
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "noplaylist": True
    }

    with YoutubeDL(ydl_opts) as ydl:
        data = ydl.extract_info(
            f"ytsearch:{query}",
            download=False
        )

    if not data["entries"]:
        return None

    video = data["entries"][0]

    return {
        "title": video.get("title"),
        "duration": video.get("duration"),
        "thumbnail": video.get("thumbnail"),
        "url": video.get("webpage_url")
    }
