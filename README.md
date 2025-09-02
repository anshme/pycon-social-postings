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
    * **Manually log in** to the selected account by entering your username and password. [cite_start]Do not close the browser yourself; let it close automatically after you've successfully logged in[cite: 2, 3].
    * [cite_start]Repeat this process for all the social media platforms you plan to use[cite: 3].
    * Once a session is saved, you will not need to perform this step again for that platform.

---

## 📝 How to Post Content

After the initial setup, follow these steps to post new content.

1.  **Activate Your Virtual Environment:**
    * **Windows:** `.\social_posts\Scripts\activate`
    * **Ubuntu/Mac:** `source social_posts/bin/activate`

2.  **Prepare Your Content:**
    * Open the `content_details.py` file.
    * [cite_start]Edit the content for LinkedIn, X, and Instagram as needed[cite: 4]. [cite_start]Ensure the text for LinkedIn starts immediately after the triple quotes (`"""`) to avoid extra spaces or new lines[cite: 4].
    * [cite_start]Place any images or videos you want to upload into the `files_to_upload` folder[cite: 4].
    * [cite_start]In `content_details.py`, update the `poster_path` variable with the exact name of the file you want to upload[cite: 4].

3.  **Run the Posting Script:**
    * To post on X: `python twitter_post.py`
    * To post on LinkedIn: `python linkedin_post.py`
    * To post on Instagram: `python instagram_post.py`

---

## 📌 Important Notes

* **Browser Management:** Each posting script will open a browser window. [cite_start]You'll need to manually close the window by pressing `Ctrl+C` in your console to terminate the program[cite: 5].
* **File Uploads:** When the browser opens for LinkedIn or X, a photo upload dialog may appear. [cite_start]**Do not select a file.** Simply close this dialog, and the script will automatically upload the file specified in your configuration[cite: 5].
* [cite_start]**LinkedIn Admin URL:** The script checks the LinkedIn admin page based on the `linkedin_admin_url` setting in the config[cite: 5]. [cite_start]This URL might differ from user to user, so you may need to configure it for your profile[cite: 6].

---

## 🛠️ Future Improvements (TODO)

* [cite_start]Implement a smoother program termination method to avoid manual closure[cite: 7].
* [cite_start]Configure timeouts for each platform to better handle network latency[cite: 7].


## Mouse Tracker: 
The following Playwright codegen commands can be used to track mouse actions and generate code for navigation[cite: 8]:
    * LinkedIn: `playwright codegen https://www.linkedin.com/feed/ --target python -o linkedin_post_play.py --user-data-dir=./user_data/linkedin`
    * X: `playwright codegen https://x.com/pyconindia --target python -o twitter_post_play.py --user-data-dir=./user_data/x`
    * Instagram: `playwright codegen https://www.instagram.com/ --target python -o instagram_post_play.py --user-data-dir=./user_data/instagram`