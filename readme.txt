##########################  ONE TIME ACTIVITY
##create a virtual env
python -m venv social_posts

## activate the venv
windows -> .\social_posts\Scripts\activate
ubuntu/mac -> source social_posts/bin/activate

##Run these command to install playwright
pip install playwright
playwright install chromium

##Save the login creds, to be run only once. 
- run the code -> python save_cookie_and_session.py. Follow the steps
- NOTE - don't close the browswer manually, let it automatically close
- Once you select an option, it would open the browswer with selected social media
- Enter the username/id and the password manually and wait for it to login. Let the browswer close.
- Repeat for all the socials that you want to post for.
############################   DON'T RUN ABOVE COMMANDS AGAIN

############################   HOW TO POST
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
2. Linkedin and twitter will open photo upload window. Don't select any file, and simple close that window. Files mentioned in the config will automatically get uploaded.
3. LinkedIn asserts the admin page by checking linkedin_admin_url in the config. It might differ for user to user, configure it for your profile.


#TODO
1. Smooth termination of program.
2. configure timeouts for each platform, so that netword latency is taken care of

## mosuse tracker to navigate.
playwright codegen https://www.linkedin.com/feed/ --target python -o linkedin_post_play.py --user-data-dir=./user_data/linkedin
playwright codegen https://x.com/pyconindia --target python -o twitter_post_play.py --user-data-dir=./user_data/x
playwright codegen https://www.instagram.com/ --target python -o instagram_post_play.py --user-data-dir=./user_data/instagram
