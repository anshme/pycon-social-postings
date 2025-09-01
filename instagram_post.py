import re
from playwright.sync_api import Playwright, sync_playwright, expect
from content_details import POST_DETAILS
import time
import random

def take_debug_screenshot(page, photo_box, filename="debug_screenshot.png"):
    """
    Take a screenshot and save it with visual annotations
    """
    # Draw the box first
    page.evaluate("""
        (box) => {
            const div = document.createElement('div');
            div.style.position = 'fixed';
            div.style.left = box.x + 'px';
            div.style.top = box.y + 'px';
            div.style.width = box.width + 'px';
            div.style.height = box.height + 'px';
            div.style.border = '3px solid lime';
            div.style.backgroundColor = 'rgba(0, 255, 0, 0.3)';
            div.style.zIndex = '9999';
            div.style.pointerEvents = 'none';
            div.textContent = 'TARGET AREA';
            div.style.color = 'black';
            div.style.textAlign = 'center';
            div.style.lineHeight = box.height + 'px';
            div.style.fontWeight = 'bold';
            
            document.body.appendChild(div);
        }
    """, photo_box)
    
    # Take screenshot
    page.screenshot(path=filename)
    print(f"📷 Debug screenshot saved: {filename}")


def tag_people_with_mouse_and_click(page, tags):
    """
    Enhanced tagging function with fallback strategies
    """
    try:
        # Strategy 1: Try to find photo container with multiple selectors
        photo_box = None
        viewport_size = page.viewport_size
        if viewport_size:
            print("Taking viewpoint size")
            center_x = (viewport_size['width'] // 2) - 100
            center_y = (viewport_size['height'] // 2) + 20
            
            # Create a bounding box representing the center area
            photo_box = {
                'x': center_x - 100,  # Adjust offset as needed
                'y': center_y - 50,  # Adjust offset as needed
                'width': 100,        # Adjust size as needed
                'height': 100        # Adjust size as needed
            }
            
            print(f"✅ Using page center coordinates")
            print(f"Page center: ({center_x}, {center_y})")
            print(f"Using photo box: {photo_box}")
        else:
            # Fallback: Use default viewport size
            print("Taking default viewport size")
            center_x = 640  # Common default width / 2
            center_y = 360  # Common default height / 2
            
            photo_box = {
                'x': center_x - 300,
                'y': center_y - 300,
                'width': 600,
                'height': 600
            }

        num_tags = len(tags)

        # Now proceed with tagging using the photo_box
        for i, tag in enumerate(tags):
            print(f"Attempting to tag: {tag}")

            progress = i / (num_tags - 1) if num_tags > 1 else 0
            
            # Calculate click position (with some randomization to avoid overlaps)
            start_x = photo_box['x'] + 20  # Left edge (with padding)
            start_y = photo_box['y'] + photo_box['height'] - 20  # Bottom edge

            end_x = photo_box['x'] + photo_box['width'] - 20  # Right edge
            end_y = photo_box['y'] + 20  # Top edge

            click_x = int(start_x + (end_x - start_x) * progress)
            click_y = int(start_y + (end_y - start_y) * progress)
            
            # Click to start tagging
            print(f"Clicking at ({click_x}, {click_y}) to tag {tag}")
            page.mouse.click(click_x, click_y)
            time.sleep(3)

            try:
                textbox = page.get_by_role("textbox", name="clear")
                textbox.wait_for(state="visible", timeout=5000)
                textbox.fill(tag)
                time.sleep(1.5)
            except Exception as e:
                print(f"❌ Could not fill textbox for {tag}: {e}")
                continue
            
            # Try to select user profile
            profile_selected = False
            
            # Multiple strategies for selecting profile
            profile_strategies = [
                lambda: page.get_by_role("button", name=re.compile(f"{tag}'s profile picture")).click(),
                lambda: page.get_by_role("button", name=re.compile(f"{tag}'s profile")).click(),
                lambda: page.locator(f"button:has-text('{tag}')").first.click(),
                lambda: page.locator(f"div:has-text('{tag}') button").first.click(),
            ]
            
            for i, strategy in enumerate(profile_strategies):
                try:
                    strategy()
                    print(f"✅ Successfully tagged {tag} (strategy {i+1})")
                    profile_selected = True
                    time.sleep(1)
                    break
                except Exception as e:
                    if i == len(profile_strategies) - 1:  # Last strategy
                        print(f"❌ Failed to select {tag}'s profile: {e}")
                    continue
            
            if not profile_selected:
                print(f"❌ Could not tag {tag} - profile selection failed")

        print("All tagging attempts complete.")
        
    except Exception as e:
        print(f"An error occurred during tagging: {e}")

def run(playwright: Playwright) -> None:
    content = POST_DETAILS['linkedin_content']
    tags = sorted(POST_DETAILS['insta_tags'])
    alt_text = POST_DETAILS['alt_text']
    file_path = POST_DETAILS['file_path']

    user_data_dir = "./user_data/instagram"

    # Launch browser with persistent session storage
    context = playwright.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,
        headless=False,
    )

    if context.pages:
        page = context.pages[0]
    else:
        page = context.new_page()

    page.goto("https://www.instagram.com/")
    page.wait_for_url("https://www.instagram.com/")
    print("Page loaded successfully.")

    print("Creating posts")
    page.get_by_role("link", name="New post Create").click()
    page.get_by_role("link", name="Post Post").click()

    print("Adding media, you need to close the input window manually")
    page.set_input_files("input[type='file']", file_path)
    time.sleep(2)
    print("Media Added")

    print("pressing next twice")
    page.get_by_role("button", name="Next").click()
    time.sleep(2)
    page.get_by_role("button", name="Next").click()
    time.sleep(2)

    print("Adding alt text and content")
    page.get_by_role("button", name="Accessibility Down chevron").click()
    page.get_by_role("textbox", name="Write alt text...").click()
    page.get_by_role("textbox", name="Write alt text...").fill(alt_text)
    page.get_by_role("textbox", name="Write a caption...").click()
    page.get_by_role("textbox", name="Write a caption...").fill(content)
    print("Content added")

    tag_people_with_mouse_and_click(page, tags)

    print("Browser will wait to you to verify and post")
    print("Please press ctrl+c to close the browser, press ctrl+c to exit from the script")

    try:
        while True:
            page.wait_for_timeout(1000)
    except KeyboardInterrupt:
        print("\n🛑 Exiting... Closing browser.")
        context.close()



with sync_playwright() as playwright:
    run(playwright)
