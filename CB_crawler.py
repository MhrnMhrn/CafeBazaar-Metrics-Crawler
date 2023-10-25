
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

def login_and_fetch_data(email, password):
    # Set up Chrome
    chrome_options = Options()
    driver = webdriver.Chrome(executable_path='path-to-driver', options=chrome_options)
    # Uncomment the following lines if you want to run Chrome in headless mode
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--window-size=1920x1080")
    
    data_dict = {}

    try:
        # Navigate to the website
        # Paste Your App's dashboard
        driver.get("https://pishkhan.cafebazaar.ir/apps/YOUR-APP/dashboard")

        # Enter login credentials
        driver.find_element_by_css_selector(".text-latin > input:nth-child(1)").send_keys(email)
        driver.find_element_by_css_selector("div.el-form-item:nth-child(3) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)").send_keys(password)
        driver.find_element_by_css_selector("button.el-button").click()

        # Wait for page to load
        time.sleep(3)
        driver.implicitly_wait(30)

        # Get data from specific elements
        today_stats_element = driver.find_element_by_css_selector("div.row:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > strong:nth-child(2)")
        percentage_element = driver.find_element_by_css_selector("div.row:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > strong:nth-child(2)")

        data_dict["today_stats"] = today_stats_element.text
        data_dict["percentage"] = percentage_element.text

        # Save to JSON file
        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(data_dict, f, ensure_ascii=False, indent=4)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    EMAIL = "YOUR_EMAIL_HERE"
    PASSWORD = "YOUR_PASSWORD_HERE"
    login_and_fetch_data(EMAIL, PASSWORD)
