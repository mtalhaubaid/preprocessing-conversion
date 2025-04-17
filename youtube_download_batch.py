import os
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from yt_dlp import YoutubeDL

def clean_youtube_url(url):
    """
    Remove the 't' (timestamp) parameter from a YouTube URL if present.
    """
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    if 't' in query:
        del query['t']
    new_query = urlencode(query, doseq=True)
    cleaned_url = urlunparse((
        parsed.scheme, parsed.netloc, parsed.path, parsed.params, new_query, parsed.fragment
    ))
    return cleaned_url

def download_youtube_content(url, resolution="best", cookie_file="youtube.com_cookies.txt"):
    # Clean the URL first
    url = clean_youtube_url(url)
    
    # Create downloads directory if it doesn't exist
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)
    
    # Build yt-dlp options without forcing the generic extractor.
    ydl_opts = {
        "cookiefile": cookie_file if os.path.exists(cookie_file) else None,
        "outtmpl": os.path.join(download_dir, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
        # Download best available quality (adaptive streams, if available, merged with audio)
        "format": "bestvideo+bestaudio/best",
        "noplaylist": False,
        "quiet": False,
        "progress_hooks": [
            lambda d: print(f"📥 Download status: {d['status']} - {d.get('filename', '')}")
        ],
    }

    if resolution != "best":
        # Limit the selection based on height (e.g. "720" for 720p)
        ydl_opts["format"] = f"bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]"

    print(f"🔗 Downloading: {url}")
    print(f"🎯 Target resolution: {resolution.upper() if resolution != 'best' else 'HIGHEST AVAILABLE'}")
    print(f"📂 Saving to: {download_dir}")
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ Download complete.")
        return True
    except Exception as e:
        print(f"🚨 Error downloading video: {e}")
        return False

def batch_download(url_list, resolution="best"):
    # Use your cookie file from the current folder or a Windows-style alternate path
    cookie_path = "youtube.com_cookies.txt"
    if not os.path.exists(cookie_path):
        alt_cookie_path = os.path.join("D:", os.sep, "cookies", "youtube.com_cookies.txt")
        if os.path.exists(alt_cookie_path):
            cookie_path = alt_cookie_path
        else:
            print("⚠️ Cookie file not found. Continuing without cookies.")
    
    total_videos = len(url_list)
    successful = 0
    failed = 0
    
    print(f"🎬 Starting batch download of {total_videos} videos")
    
    for i, url in enumerate(url_list, 1):
        print(f"\n📌 Processing video {i}/{total_videos}")
        success = download_youtube_content(url, resolution, cookie_path)
        if success:
            successful += 1
        else:
            failed += 1
    
    print(f"\n📊 Batch download summary:")
    print(f"   ✅ Successfully downloaded: {successful}/{total_videos}")
    print(f"   ❌ Failed downloads: {failed}/{total_videos}")
    
    return successful, failed

if __name__ == "__main__":
    # List of YouTube URLs to download
    youtube_urls = [
        "https://www.youtube.com/watch?v=FgcUg837Fww",
        "https://www.youtube.com/watch?v=UHTDEdqJyD4",
        "https://www.youtube.com/watch?v=W_KNCGypkUE",
        
        "https://www.youtube.com/shorts/mymElEe0iMg",
        "https://www.youtube.com/watch?v=ZoCeJbhevek",
        "https://www.youtube.com/watch?v=zSjChjNhOfU&rco=1",
        "https://www.youtube.com/watch?v=cvVROcbZKbs",
        "https://www.youtube.com/watch?v=SLF9v4O_S5M",
        "https://www.youtube.com/watch?v=TjvSCl6ZcOE",
        "https://www.youtube.com/watch?v=3Ojsd6r4vO4&rco",

    ]
    
    # Set desired resolution (e.g., "720", "1080", or "best")
    desired_resolution = "best"
    
    # Start batch download
    batch_download(youtube_urls, desired_resolution)