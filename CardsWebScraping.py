import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Directory to save images
load_dotenv()
IMAGE_DIR = os.getenv("IMAGE_DIR")
os.makedirs(IMAGE_DIR, exist_ok=True)

# Base URL and total pages
BASE_URL = "https://www.albetaqa.site/lang/arb/?paged="
TOTAL_PAGES = 1 # it's actully 453 pages, to be changed once needed.

# Function to download images
def download_image(img_url):
    filename = os.path.join(IMAGE_DIR, img_url.split("/")[-1])
    response = requests.get(img_url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        # if you are running the full scipt to download all images, you can comment this line to avoid the output
        #print(f"Downloaded: {filename}")

# Function to scrape images
def scrape_images():
    '''
    Scrapes images from the website and downloads them to the IMAGE_DIR, this function will scrape all pages from 1 to TOTAL_PAGES
    this script is run once to download all images, then you can schedule the InstagramPost.py script to post a random image daily.
    '''
    image_sources = []
    for page in range(1, TOTAL_PAGES + 1):
        url = f"{BASE_URL}{page}"
        print(f"Scraping page {page}, this takes around 13ish sec/page, {TOTAL_PAGES - page} pages left...")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find images with a specific class
        images = soup.find_all("img", class_="attachment-sm-pe-normal size-sm-pe-normal wp-post-image")
        for img in images:
            img_url = img["src"]
            image_sources.append(img_url)
            download_image(img_url)

    print("Scraping complete for ALL pages! # of images downloaded:", len(image_sources), "images in:", IMAGE_DIR, "in the current directory.")

if __name__ == "__main__":
    scrape_images()
