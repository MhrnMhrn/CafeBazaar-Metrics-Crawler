# Cafe Bazaar Data Dashboard Crawler

A simple Python-based web crawler built with Selenium to scrape data from the Cafe Bazaar dashboard.

## 🚀 Setup

### Prerequisites

- Ensure you have Python and `pip` installed on your system.

### Dependencies

To install the required Python libraries, run:

pip install selenium


### WebDriver

Download the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/). Ensure it's in the same directory as the script or its path is specified in the script.

## 🔧 Usage

1. **Credentials**: Open `crawler.py` in an editor. Replace `YOUR_EMAIL_HERE` and `YOUR_PASSWORD_HERE` with your Cafe Bazaar dashboard login credentials.
2. **Run**: Execute the script with Python to fetch the data. The results will be saved to `output.json`.

## 🛠 Customization

To fetch any other element from the dashboard:
- Identify the element's CSS selectors.
- Modify them in the script as needed.
- Update the `data_dict` dictionary with the desired keys to output them.

## ⚠️ Disclaimer

Web scraping might be against the terms of service for some websites. Ensure you have the right to scrape a website. Avoid sending many requests in a short time frame.


