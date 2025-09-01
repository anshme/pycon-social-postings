import time
from playwright.sync_api import Playwright, sync_playwright, expect
import cleanup
from content_details import POST_DETAILS

def run(playwright: Playwright) -> None:
    content = POST_DETAILS['linkedin_content']
    tags = sorted(POST_DETAILS['linkedin_tags'])
    alt_text = POST_DETAILS['alt_text']
    file_path = POST_DETAILS['file_path']

    user_data_dir = "./user_data/linkedin"

    # Launch browser with persistent session storage
    context = playwright.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,
        headless=False,
    )

    if context.pages:
        page = context.pages[0]
    else:
        page = context.new_page()


    page.goto("https://www.linkedin.com/feed/")
    page.get_by_role("link", name="PyCon India 2025", exact=True).click()

    # Click on "PyCon India 2025" link and wait for navigation to admin dashboard
    # with page.expect_navigation(wait_until="networkidle"):
    #     page.get_by_role("link", name="PyCon India 2025", exact=True).click()

    # Ensure we are on the admin dashboard
    page.wait_for_url("https://www.linkedin.com/company/14626244/admin/dashboard/*")

    print("Page loaded successfully.")
    print("Creating posts")
    page.get_by_role("link", name="Create").wait_for(state='visible')
    page.get_by_role("link", name="Create").click()

    page.get_by_role("link", name="Start a post Share content to").click()

    print("Adding media")
    page.get_by_role("button", name="Add media").click()

    page.set_input_files("input[type='file']", file_path)
    
    #Wait for file to upload
    time.sleep(5)
    print("Media Added")
    # Wait for the 'Tag' button to be visible and then click it.
    # This ensures the file upload is complete before proceeding.
    page.get_by_role("button", name="Tag").wait_for(state="visible")
    page.get_by_role("button", name="Tag").click()
    print("Tagging accounts")
    for tag in tags:
        print(f"Tagging {tag}...")
        page.get_by_role("combobox", name="Type a name or names").fill(tag)
        page.wait_for_timeout(1000)
        page.get_by_role("combobox", name="Type a name or names").press("ArrowDown")
        page.get_by_role("combobox", name="Type a name or names").press("Enter")

    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Add").click()
    print("Tags completed")

    print("Filling alt text")
    page.get_by_role("button", name="Alternative text").click()
    page.get_by_role("textbox", name="Alt text*").click()
    page.get_by_role("textbox", name="Alt text*").fill(alt_text)
    page.get_by_role("button", name="Add").click()
    page.wait_for_timeout(1000)
    print("Alt text added")
    
    print("Adding content")
    page.get_by_role("button", name="Next").click()
    page.get_by_role("textbox", name="Text editor for creating").click()
    page.get_by_role("textbox", name="Text editor for creating").fill(content)
    print("Browser will wait to you to verify and post")
    print("Please press ctrl+c to close the browser")
    try:
        while True:
            page.wait_for_timeout(1000)
    except KeyboardInterrupt:
        print("\n🛑 Exiting... Closing browser.")
    finally:
        cleanup()

with sync_playwright() as playwright:
    run(playwright)
