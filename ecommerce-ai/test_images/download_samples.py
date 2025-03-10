import urllib.request
import os

# Sample product images URLs
test_images = {
    'laptop.jpg': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800',
    'tshirt.jpg': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=800',
    'sneakers.jpg': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800',
    'watch.jpg': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800',
    'backpack.jpg': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800'
}

def download_images():
    for filename, url in test_images.items():
        try:
            print(f"Downloading {filename}...")
            urllib.request.urlretrieve(url, filename)
            print(f"Successfully downloaded {filename}")
        except Exception as e:
            print(f"Error downloading {filename}: {e}")

if __name__ == "__main__":
    # Change to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    download_images() 