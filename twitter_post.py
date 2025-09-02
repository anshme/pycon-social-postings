from playwright.sync_api import Playwright, sync_playwright, expect
import cleanup
from content_details import POST_DETAILS
import time

def run(playwright: Playwright) -> None:
    content = POST_DETAILS['x_content']
    tags = sorted(POST_DETAILS['x_tags'])
    alt_text = POST_DETAILS['alt_text']
    file_path = POST_DETAILS['file_path']
    wait_ms = POST_DETAILS['x_wait_timeout_ms']

    user_data_dir = "./user_data/x"

    # Launch browser with persistent session storage
    context = playwright.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,
        headless=False,
    )

    if context.pages:
        page = context.pages[0]
    else:
        page = context.new_page()
    page.goto("https://x.com/pyconindia")
    page.wait_for_url("https://x.com/pyconindia")
    print("Page loaded successfully.")

    print("Creating posts")
    page.get_by_test_id("SideNav_NewTweet_Button").click()
    
    print("Adding media, you need to close the input window manually")
    page.get_by_role("button", name="Add photos or video").click()
    page.set_input_files("input[type='file']", file_path)
    
    #Wait for file to upload
    time.sleep(wait_ms/1000)
    print("Added media")
    
    print("Tagging accounts")
    page.get_by_role("link", name="Tag people").click()
    for tag in tags:
        print(f"Tagging {tag}...")
        page.get_by_test_id("searchPeople").fill(tag)
        page.wait_for_timeout(wait_ms)
        page.get_by_test_id("searchPeople").press("ArrowDown")
        page.get_by_test_id("searchPeople").press("Enter")
    page.get_by_role("button", name="Done").click()
    print("Tags completed")
    print("Filling alt text")
    page.get_by_test_id("altTextWrapper").click()
    page.get_by_test_id("altTextInput").fill(alt_text)
    page.get_by_test_id("endEditingButton").click()
    print("Alt text added")


    print("Adding content")
    page.get_by_test_id("tweetTextarea_0").locator("div").nth(2).click()
    page.get_by_test_id("tweetTextarea_0").fill(content)
    print("Browser will wait to you to verify and post")
    print("Please press ctrl+c to close the browser, press ctrl+c to exit from the script")
    # ---------------------
    try:
        while True:
            page.wait_for_timeout(1000)
    except KeyboardInterrupt:
        print("\n🛑 Exiting... Closing browser.")
    finally:
        cleanup()

with sync_playwright() as playwright:
    run(playwright)
