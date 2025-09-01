##########################ONE TIME ACTIVITY
##create a virtual env
python -m venv social_posts

## activate the venv
windows -> .\social_posts\Scripts\activate
ubuntu/mac -> source social_posts/bin/activate

##Run these command to install playwright
pip install playwright
playwright install chromium

##Save the login creds, to be run only once.
- uncommnet the login platform that you want to use.
- run the code -> python save_cookie_and_session.py
- This would open your browswer, login to the platform, wait for it to close automatically
- Repeat the above steps for all the platforms
############################DON'T RUN ABOVE COMMANDS AGAIN

############################HOW TO POST
Initailize your env
## activate the venv
windows -> .\social_posts\Scripts\activate
ubuntu/mac -> source social_posts/bin/activate

##To post, open the file content_details.py
    - edit the linkedin content, make sure to start just after """, else there would be unnecessary space or new line
    - Copy the file in flies_to_upload folder and mention the name in poster_path
    - to post on twitter -> python twitter_post.py
    - to post on linkedIn -> python linkedin_post.py
    - to post on instagram -> python_instagram.py

IMPORTANT NOTES: 
1. Each post will open a browswer. You would need to close the browswer by pressing ctrl+c on the console.
2. Linkedin and twitter will open photo upload window. Don't select any file, just close that window. Mentioned file will automatically get uploaded.

    




## mosuse tracker to navigate.
playwright codegen https://www.linkedin.com/feed/ --target python -o linkedin_post_play.py --user-data-dir=./user_data/linkedin
playwright codegen https://x.com/pyconindia --target python -o twitter_post_play.py --user-data-dir=./user_data/x
playwright codegen https://www.instagram.com/ --target python -o instagram_post_play.py --user-data-dir=./user_data/instagram
