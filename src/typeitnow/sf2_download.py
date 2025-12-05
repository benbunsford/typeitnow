from pathlib import Path
import platformdirs
from urllib.request import urlretrieve

url = "https://github.com/benbunsford/typeitnow/releases/download/v0.1.1-alpha/undertale.sf2"
cache_folder = Path(platformdirs.user_cache_dir("typeitnow", "benbunsford"))
cache_folder.mkdir(parents=True, exist_ok=True)
sf2_path = cache_folder / "undertale.sf2"

def get_sf2():
    if not sf2_path.exists():
        print(f"Downloading soundfont to {sf2_path}...")
        try:
            urlretrieve(url, sf2_path)
            print("Download complete.")
        except Exception as e:
            print(f"Error downloading .sf2 file: {e}")
