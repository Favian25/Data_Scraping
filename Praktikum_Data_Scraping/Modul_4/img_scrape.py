import os
import requests
from bs4 import BeautifulSoup
import fungsi

def scrape_images(url, save_path='Hasil'):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    images = []
    for img in soup.find_all("img"):
        img_url = img.get("src")
        if img_url and img_url.endswith(('.jpg', '.png', '.jpeg')):
            images.append(img_url)

    fungsi.create_directory(save_path)

    for img in images:
        try:
            img_response = requests.get(img)
            filename = os.path.basename(img)
            filepath = os.path.join(save_path, filename)
            with open(filepath, 'wb') as f:
                f.write(img_response.content)
            print(f"{filename} berhasil disimpan di direktori {save_path}")
        except Exception as e:
            print(f"Gagal menyimpan {img}: {e}")

if __name__ == "__main__":
    target_url = "https://www.jagatreview.com/"
    scrape_images(target_url)