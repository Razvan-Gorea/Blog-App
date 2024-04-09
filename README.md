# Blog-App
A blog application made in the python django web framework. (In progress) 

To get started do the following:

1. Clone this repository
2. Navigate to the root of your cloned repository
3. Create a python virtual environment
4. Activate the python virtual environment
5. Install the project dependencies from the requirements.txt file using the following command: `pip install -r requirements.txt`
6. Check if you need to do any migrations and (optionally) create a super user for your own clone of the project
7. Run `python3 manage.py runserver`

If any errors popup, check the the console log within your browser or `http://localhost:8000`

This project is still a work in progress and still yet to be completed.
The objective of this project is to create a blog application with django that has plenty of functionality.

## Current Functionality

- Blog posts can be created, deleted and updated from django admin and the user interface
- Blog posts can be viewed on the main page
- Brand new user can be created from the registration page or django admin
- User can login from the login page
- User can logout by clicking the logout button
- A profile image can be now displayed on the user's profile, at the moment it can only be accomplished via django admin through the `Profile` model 
- The profile image has a set default image whenever a new user is created, a new profile object is created whenever a new user intance is created. This is accomplished through django signals.
- User can now edit their username, email and profile image. Additionally, the user's profile image now appears next to their blog posts. Any profile image uploaded gets scaled down to 300x300 px.
