# Social Media Posting Automation

This guide explains how to set up and use the automated social media posting script. It covers the one-time setup and the process for posting content.

---

## 🚀 One-Time Setup

Follow these steps only once to set up the environment and save your login sessions.

1.  **Create and Activate a Virtual Environment:**
    * Create the virtual environment:
        ```sh
        python -m venv social_posts
        ```
    * Activate the environment:
        * **Windows:** `.\social_posts\Scripts\activate`
        * **Ubuntu/Mac:** `source social_posts/bin/activate`

2.  **Install Playwright:**
    * Install the library:
        ```sh
        pip install playwright
        ```
    * Install the necessary browsers:
        ```sh
        playwright install chromium
        ```

3.  **Save Your Login Sessions:**
    * Run the session-saving script:
        ```sh
        python save_cookie_and_session.py
        ```
    * Follow the on-screen prompts to select the social media platform you want to log into. A browser window will open.
    * **Manually log in** to the selected account by entering your username and password. Do not close the browser yourself; let it close automatically after you've successfully logged in.
    * Repeat this process for all the social media platforms you plan to use.
    * Once a session is saved, you will not need to perform this step again for that platform.

---

## 📝 How to Post Content

After the initial setup, follow these steps to post new content.

1.  **Activate Your Virtual Environment:**
    * **Windows:** `.\social_posts\Scripts\activate`
    * **Ubuntu/Mac:** `source social_posts/bin/activate`

2.  **Prepare Your Content:**
    * Open the `content_details.py` file.
    * Edit the content for LinkedIn, X, and Instagram as needed. Ensure the text for LinkedIn starts immediately after the triple quotes (`"""`) to avoid extra spaces or new lines.
    * Place any images or videos you want to upload into the `files_to_upload` folder.
    * In `content_details.py`, update the `poster_path` variable with the exact name of the file you want to upload.

3.  **Run the Posting Script:**
    * To post on X: `python twitter_post.py`
    * To post on LinkedIn: `python linkedin_post.py`
    * To post on Instagram: `python instagram_post.py`

---

## 📌 Important Notes

* **Browser Management:** Each posting script will open a browser window. You'll need to manually close the window by pressing `Ctrl+C` in your console to terminate the program.
* **File Uploads:** When the browser opens for LinkedIn or X, a photo upload dialog may appear. **Do not select a file.** Simply close this dialog, and the script will automatically upload the file specified in your configuration.
* **LinkedIn Admin URL:** The script checks the LinkedIn admin page based on the `linkedin_admin_url` setting in the config. This URL might differ from user to user, so you may need to configure it for your profile.

---


## TODO

* Instagram tagging, find the picture tag and make the bounding box bigger. Currently it takes the center and of the page and assumes that it has landed on the picture, which is correct when posting from high res, full screen browswer.


## 🖱️ Mouse Tracker

Use the `playwright codegen` command to track mouse actions and generate code for navigation. This is helpful for creating scripts that interact with web pages.
* `playwright codegen https://www.linkedin.com/feed/ --target python -o linkedin_post_play.py --user-data-dir=./user_data/linkedin`