# Flashcards App

This Django application allows users to create and study flashcards, track their progress, and review learned words. It includes features such as proficiency tracking, statistics, and user authentication.


## Distinctiveness and Complexity
My Flashcards app proves being distinct to other applications I have the oportunity to develop during the CS50Web course. It is clear that is not a social network, nor an e-commerce site, instead, it can be categorized as an educational application (but different than a wiki). I tried to imagine how to develop this application without seeing other similar language flashcard apps, to not influence strongly the design. 

Also, the ability to create your own flashcards and not be limited to a specific language makes it flexible. Functionalities like tracking words proficiency, reviewing known words, displaying a list of learned words and having user stats makes it sufficiently complex to satisfy the requirements of the submission. A simple tutorial in the home page helps new users to familiarize with its minimalistic user interface. I combined techniques learned during the course such as scalability, responsive interfaces, asyncronous calls to Python API's using JavaScript, Django models and version control to make sure to apply almost everything I learned during this awesome course!


## Key Features
- **Flashcard Creation**: Users can create new flashcards with words in their target language, translation in their native language, and images.

- **Proficiency Tracking**: Users can set their proficiency level for each flashcard, indicating whether they need practice or have learned the word.

- **Check learned words**: Users can check all learned words in case they need to remember them and know their count.

- **Statistics**: The app calculates and displays user statistics, including the total number of cards, cards that need practice, learned cards, the percentage of learned cards, and the last time studied.

- **Study and Review**: Users can study new flashcards and review cards that need practice.

- **User Authentication**: Users can register, log in, and log out of the application.

## Files Explanation 
(What’s contained in each file)

### 1. Models

The `models.py` file defines the database models for the application: 
- **User**: represents a user account with attributes such as username, email, password, and other fields inherited from the default User model. The custom User model has methods to authenticate users and I added an ImageField for the profile picture.
- **Flashcard**: represents a card with attributes including target language word, native language translation, and a reference image.
- **Proficiency**: Represents a level of mastery for a specific flashcard word. It is related to the Flashcard and User model using ForeignKeys, with a unique_together attribute between user and flashcard fields to avoid duplication.
- **Stats**: Represents statistics about a user's performance on studying or practicing flashcards. It contains fields for total cards studied, learned flashcards, flashcards that need more practice, last time studied, etc. This model is linked to the User model via a OneToOneField

### 2. Views
The `views.py` file contains all the views functions which handle incoming requests from users. There are three main types of views: login/logout related views, dashboard views, and
card management views. Each view is associated with a URL route defined in `urls.py`.

- **New Flashcard**: Receives a POST request to create a new flashcard object and save it in the database.
- **Set Proficiency**: Receives a POST request from a fetch call and updates an user proficiency of certaing word/flashcard. 
- **Update Stats**: Update user stats into the database and calculate percent of words learned. Is called when a flashcard proficiency is updated.
- **Index**: Renders index template.
- **Study**: Gets max 10 flashcards for a study deck and shows one per page using Django paginator. 
- **Review**: Gets max 10 flashcards that needs more practice for a review deck and shows one per page using Django paginator. 
- **Learned**: Gets all learned flashcards ordered by last studied date time, using Paginator shows 5 per page.
- **Profile**: Gets user stats and renders stats template.
- **Login**: Handles user login by checking if provided credentials match those stored in the database and redirects accordingly. If not logged in, renders login page with error message (if any).
- **Logout**: Logs out current user by removing session data and displaying login page.


### 3. Templates
The templates folder holds HTML files used by Django to render pages to the user's browser.
Each template corresponds to a specific view function and includes references to other
templates via the {% extends %} tag at the top of the page. The application has the following templates:

- ``index.html``
- ``layout.html``
- ``learned.html``
- ``login.html``
- ``new_flashcard.html``
- ``register.html``
- ``review.html``
- ``stats.html``
- ``study.html``

### 4. Urls
Has all URLs mapped to their corresponding view functions. 

### 5. Media
This section describes any media files included in the project, such as images (user pictures and flashcards images).

### 6. Static
This section describes static assets, such as CSS stylesheets and JavaScript files. 

## Running the application
Make sure you have Python and Git installed on your computer. Then follow these steps:

1. Clone the repository into your local machine using Git. Open terminal and type:
``git clone https://github.com/SofiaBracho/flashcards.git``
2. Go to the project directory: 
``cd flashcards``
3. Migrate Django models:
``python manage.py makemigrations``
``python manage.py migrate``
4. Run the local server:
``python manage.py runserver``
5. Open http://localhost:8000 in your web browser. You should see the homepage
with "Log in" and "Register" button.
