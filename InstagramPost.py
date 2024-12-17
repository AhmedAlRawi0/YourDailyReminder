"""
This script posts a random image from the "reminder_cards" directory to Instagram with a random caption. 
Cron job can be set to run this script at specified times to post a random image.
"""
from instagrapi import Client
import os
import random
from dotenv import load_dotenv

# Load environment variables (there is an .env file in the same directory)
load_dotenv()
USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

# Image directory, make sure you are providing the absolute path
IMAGE_DIR = os.getenv("IMAGE_DIR")

# Instagram caption templates to avoid spamming the same caption + avoid getting detected as a bot
CAPTIONS = [
    "سبحان الله والحمد لله ولا إله إلا الله والله أكبر ولا حول ولا قوة إلا بالله العلي العظيم ❤️\n.",
    "الحمد لله دائماً وأبداً ❤️\n.",
    "اللهم اجعلنا من الذاكرين الشاكرين ❤️\n."
]
HASHTAGS = """#إسلاميات #اسلام #مسلم #مسلمين #فضائل_الصحابة #مسلمون #دين #الدين_الاسلامي #مكة_المكرمة #المدينة_المنورة 
#مكه_المكرمه #المدينه_المنوره #اذكار #ذكرني #اذكار_الصباح #اذكار_المساء #دعوة #خطبة_الجمعة #الحج #رمضان 
#رمضانيات #مسجد #مساجد #كتاب_الله #محمد #الله #اللهم_صل_وسلم_على_نبينا_محمد"""

# Initialize the client
cl = Client()

# Login to Instagram
def login_to_instagram():
    print("Logging in to Instagram... the whole process takes around 20ish seconds")
    try:
        cl.login(USERNAME, PASSWORD)
        print("Login successful!")
    except Exception as e:
        print(f"Login failed: {e}")

# Function to create a random caption
def create_random_caption():
    return f"{random.choice(CAPTIONS)}{HASHTAGS}"

# Function to post an image
def post_image():
    image_files = [f for f in os.listdir(IMAGE_DIR) if f.endswith(".jpg") or f.endswith(".png")]
    if not image_files:
        print("No images to post!")
        return
    
    # Select a random image to post
    image_path = os.path.join(IMAGE_DIR, random.choice(image_files))
    caption = create_random_caption()
    
    try:
        cl.photo_upload(image_path, caption)
        print(f"Posted: {image_path}")
    except Exception as e:
        print(f"Failed to post image: {e}")

if __name__ == "__main__":
    login_to_instagram()
    post_image()
