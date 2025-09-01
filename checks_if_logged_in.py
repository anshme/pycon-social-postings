from playwright.sync_api import sync_playwright
import time

def check_linkedin_login():
    with sync_playwright() as p:
        # Use the same user_data_dir as during login
        browser = p.chromium.launch_persistent_context(
            user_data_dir="user_data/linkedin",
            headless=False
        )

        page = browser.new_page()
        page.goto("https://www.linkedin.com/feed/")

        
        time.sleep(15)
        browser.close()

def check_x_login():
    with sync_playwright() as p:
        # Use the same user_data_dir as during login
        browser = p.chromium.launch_persistent_context(
            user_data_dir="user_data/x",
            headless=False
        )

        page = browser.new_page()
        page.goto("https://x.com/pyconindia")

        
        time.sleep(15)
        browser.close()

check_x_login()
