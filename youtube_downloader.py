import yt_dlp
import os

# ✅ Folder to save downloaded videos
SAVE_FOLDER = "youtube_downloads"

def download_youtube_video(video_url, video_quality="highest"):
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    ydl_opts = {
        "outtmpl": os.path.join(SAVE_FOLDER, "%(title)s.%(ext)s"),
        "format": "best" if video_quality == "highest" else f"bestvideo[height={video_quality}]+bestaudio/best"
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"📥 Downloading: {video_url} ({video_quality})...")
            ydl.download([video_url])
        print(f"✅ Download complete! Saved to {SAVE_FOLDER}")

    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ").strip()
    video_quality = input("Enter quality (highest, 720, 1080, audio): ").strip().lower()

    if video_quality not in ["highest", "720", "1080", "audio"]:
        print("⚠️ Invalid quality! Defaulting to highest quality.")
        video_quality = "highest"

    download_youtube_video(video_url, video_quality)
