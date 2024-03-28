# Blog-App
A blog application made in the python django web framework. (In progress) 

To get started do the following:

1. Clone this repository
2. Navigate to the root of your cloned repository
3. Run `python3 manage.py runserver`

This project is still a work in progress and still yet to be completed.
The objective of this project is to create a blog application with django that has plenty of functionality.

## Current Functionality

- Blog posts can be created from django admin
- Blog posts can be viewed on the main page
- User can be created from the registration page or django admin
- User can login from the login page
- User can logout by clicking the logout button
- A profile image can be now displayed on the user's profile, at the moment it can only be accomplished via django admin through the `Profile` model 
- The profile image has a default now, a new profile object is created whenever a new user intance is created. This is accomplished through django signals.
