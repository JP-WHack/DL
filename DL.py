import requests
from tqdm import tqdm

# ダウンロード対象のURLをここに入力
url = "https://example.com/video.mp4"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "identity;q=1, *;q=0",
    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Host": "example.com",
    "If-Range": '"1234567890"',  
    "Range": "bytes=0-",
    "Referer": "https://example.com/",
    "Sec-Fetch-Dest": "video",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers, stream=True)
total_size = int(response.headers.get("content-length", 0))

with open("video.mp4", "wb") as f:
    with tqdm(total=total_size, unit="B", unit_scale=True, desc="Downloading") as pbar:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                pbar.update(len(chunk))

print("ダウンロード完了")