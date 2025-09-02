from playwright.sync_api import sync_playwright

def login_x():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="user_data/x",  # Directory to store session data
            headless=False               # Keep browser visible for manual login
        )

        page = browser.new_page()
        page.goto("https://x.com/login")

        print("Please log in manually if not already logged in...")
        page.wait_for_timeout(30000)  # Wait 30 seconds for manual login

        print("Session saved! Next time you won't need to log in.")
        browser.close()




def login_linkedin():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="user_data/linkedin",
            headless=False
        )

        page = browser.new_page()
        page.goto("https://www.linkedin.com/login")

        print("Please log in manually if not already logged in...")
        page.wait_for_timeout(30000)  # Wait 30 seconds for manual login

        print("Session saved! Next time you won't need to log in.")
        browser.close()



def login_instagram():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="user_data/instagram",
            headless=False
        )

        page = browser.new_page()
        page.goto("https://www.instagram.com/accounts/login/")

        print("Please log in manually if not already logged in...")
        page.wait_for_timeout(30000)  # Wait 30 seconds for manual login

        print("Session saved! Next time you won't need to log in.")
        browser.close()

def main_menu():
    while True:
        print("\n--- Social Media Login Saver ---")
        print("1. Log in to X (formerly Twitter)")
        print("2. Log in to LinkedIn")
        print("3. Log in to Instagram")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            login_x()
        elif choice == '2':
            login_linkedin()
        elif choice == '3':
            login_instagram()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main_menu()