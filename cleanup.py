import sys

def cleanup():
    """Clean up browser resources"""
    global browser, page
    try:
        if page:
            page.close()
        if browser:
            browser.close()
        print("✅ Cleanup completed")
    except Exception as e:
        print(f"⚠️ Cleanup warning: {e}")
    finally:
        sys.exit(0)