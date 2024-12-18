# 📜 Daily Reminders Automation

This simple project automates the process of posting reminder cards to Instagram _(without violating Ig's community guidlines)_ and soon Telegram. It scrapes cards from a Dawah website _(allowed by the website)_, saves the images, and schedules daily posts with meaningful captions. 

---

## 🕌 **Purpose of the Project**

This project aims to contribute to the spreading of beneficial knowledge, as emphasized in the noble Hadith of the Prophet Muhammad ﷺ:

> **"When a man dies, his deeds come to an end except for three things:  
> a continuing charity, beneficial knowledge, or a righteous child who prays for him."**  
> _(Sahih Muslim 1631)_

By automating the sharing of Islamic reminders, this project serves as a means to disseminate beneficial knowledge (عِلْمٍ يُنْتَفَعُ بِهِ), which can inspire and guide people every day.

---

## **Features**

1. **Web Scraping**: Scrapes Islamic cards from [albetaqa.site](https://www.albetaqa.site) and saves them locally.
2. **Automated Instagram Posting**:  
   - Posts a random image from the saved reminders twice a day using Instagram's API.
   - Adds captions with a mix of Dhikr and hashtags.
3. **Scheduled Tasks**: Leverages cron jobs to schedule posting at specific times.
4. **Reusability**: Anyone can fork and set up their own automated reminder bot with ease.

---

## **Project Setup**

Follow these steps to set up the project locally _(for personal use only)_.

### **1. Prerequisites**
Ensure you have the following installed:
- **Python 3.10 or later**
- **pip** (Python package manager)

Install required libraries:
```bash
pip install requests beautifulsoup4 python-dotenv instagrapi
```

---

### **2. Instagram Account Setup**

- Create an Instagram account dedicated to posting reminders.
- Log in to the account manually and verify it to avoid restrictions.
- Keep your credentials secure.

---

### **3. Project Structure**

```
YourDailyReminder/
│
├── reminder_cards/             # Directory where scraped images will be saved
├── CardsWebScraper.py          # Script to scrape images
├── InstagramPost.py            # Script to post images to Instagram
├── .env                        # Environment variables
├── README.md                   # Project documentation
├── LICENSE                     # MIT License
├── .gitignore                  # Items to ignore by git
└── instagram_log.txt           # File where InstagramPost.py logs will be saved
```

---

### **4. Create a `.env` File**

Create a `.env` file in the project root directory to securely store your credentials:

```env
INSTAGRAM_USERNAME=your_instagram_username
INSTAGRAM_PASSWORD=your_instagram_password
IMAGE_DIR=/absolute/path/to/reminder_cards
```

- Replace `/absolute/path/to/reminder_cards` with the full path to the `reminder_cards` directory.

---

## **🛠️ How to Run the Scripts**

### **1. Web Scraping: Save Images Locally**

Run the web scraping script **once** to download all reminder images:

```bash
python3 CardsWebScraper.py
```

- This script downloads all images from the source website and saves them in the `reminder_cards` directory.
- Adjust `TOTAL_PAGES` in the script if you want to scrape all pages.

---

### **2. Automated Instagram Posting**

The `InstagramPost.py` script posts a random image daily to Instagram.

Run it manually for testing:
```bash
python3 InstagramPost.py
```

---

## **⏰ Schedule the Scripts During Times Where the Laptop is ON (Cron Job)**

To automate daily posting, set up a **cron job**:

### Example: Post Twice a Day (9 AM and 5 PM)

1. Open your `crontab`:
   ```bash
   crontab -e
   ```

2. Add the following line:

   ```bash
   0 9,17 * * * cd /absolute/path/to/YourDailyReminder && /Library/Frameworks/Python.framework/Versions/3.10/bin/python3 InstagramPost.py >> instagram_log.txt 2>&1
   ```

   - Replace `/absolute/path/to/YourDailyReminder` with the full path to your project folder.
   - Run `which python3` to verify your Python path and replace `/Library/Frameworks/Python.framework/Versions/3.10/bin/python3` if needed.

3. Save and exit.

### **Verify the Cron Job**

Check all scheduled cron jobs:
```bash
crontab -l
```

---

## **📜 How It Works**

1. **CardsWebScraper.py**:
   - Scrapes reminder images from [albetaqa.site](https://www.albetaqa.site) and saves them locally.
   - Run **once** to download all content.

2. **InstagramPost.py**:
   - Logs into Instagram using credentials from the `.env` file.
   - Picks a random image from the `reminder_cards` folder.
   - Posts it with a caption that includes:
     - **Random Dhikr** (e.g., سبحان الله والحمد لله...).
     - **Hashtags** for visibility.

3. **Cron Job**:
   - Schedules the script to run at specific times daily.

---

## **🛠️ Forking and Customizing**

- **Create Your Instagram Bot**: Fork this repository and set up your own `.env` file with Instagram credentials.
- **Adjust Web Scraping**:
   - Modify the `TOTAL_PAGES` variable in `CardsWebScraper.py` to download all pages or limit it.
- **Custom Captions**:
   - Add or edit captions in the `CAPTIONS` list in `InstagramPost.py`.
- **Hashtags**:
   - Update the `HASHTAGS` variable for improved visibility.

---

## **🌟 Contributing**

This project is open for contributions! Feel free to:
- Enhance the script (e.g., error handling, scheduling).
- Add support for other platforms (e.g., Telegram).
- Open an issue

---

## **🥋 Closing Note**

May Allah accept this effort and make it a means of spreading beneficial knowledge.

---

## **🔗 License**
This project is licensed under the MIT License. Feel free to use, fork, and improve it.
