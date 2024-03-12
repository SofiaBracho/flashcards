<div align="center">
  <h1 align="center">Flashcards App</h1>
</div>
<br/>



<div align="center">

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-javascript](https://img.shields.io/badge/Made%20with-JavaScript-1f425f.svg)](https://www.javascript.com)
<br/>
<br/>
<a href="https://www.linkedin.com/in/sofiabrach0/">
![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=fff&style=for-the-badge)
</a>
<a href="https://github.com/SofiaBracho">
![GitHub Badge](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=for-the-badge)
</a>
</div>


This Django App allows users to create and study flashcards, track their progress, and review learned words. It includes features such as proficiency tracking, statistics, and user authentication.


## ⚙️ Key Features
- **Flashcard Creation**: Users can create new flashcards with words in their target language, translation in their native language, and images.

- **Proficiency Tracking**: Users can set their proficiency level for each flashcard, indicating whether they need practice or have learned the word.

- **Check learned words**: Users can check all learned words in case they need to remember them and know their count.

- **Statistics**: The app calculates and displays user statistics, including the total number of cards, cards that need practice, learned cards, the percentage of learned cards, and the last time studied.

- **Study and Review**: Users can study new flashcards and review cards that need practice.

- **User Authentication**: Users can register, log in, and log out of the application.


## 🖥️ Demo

![Flashcards Demo GIF](https://github.com/SofiaBracho/flashcards/blob/master/media/demo.gif)

<a href="https://youtu.be/9urd2xRv_1Q">**Full demo on Youtube**</a>

## 🗄️ Models

The `models.py` file defines the database models for the application: 
- **User**: represents a user account with attributes such as: 
  - Username
  - Email,
  - Password
  - Profile picture
- **Flashcard**: represents a card. 
  - Target language word
  - Native language translation
  - Reference image.
- **Proficiency**: Represents a level of mastery for a specific flashcard word. It is related to the Flashcard and User model using ForeignKeys, with a unique_together attribute between user and flashcard fields to avoid duplication.
- **Stats**: Represents statistics about a user's performance on studying or practicing flashcards. 
  - Cards studied count
  - Learned flashcards count
  - Flashcards that need more practice count 
  - Last time studied

## 🖇️ Views
The `views.py` file contains all the views functions which handle incoming requests.

- **New Flashcard**: Receives a POST request to create a new flashcard object and save it in the database.

![New flashcard view](https://github.com/SofiaBracho/flashcards/blob/master/media/new.PNG)

- **Set Proficiency**: Receives a POST request from a fetch call and updates an user proficiency of certaing word/flashcard. 
- **Update Stats**: Update user stats into the database and calculate percent of words learned. Is called when a flashcard proficiency is updated.
- **Index**: Renders index template.

![Index view](https://github.com/SofiaBracho/flashcards/blob/master/media/home.PNG)

- **Study**: Gets max 10 flashcards for a study deck and shows one per page using Django paginator. 

![Study view](https://github.com/SofiaBracho/flashcards/blob/master/media/study.PNG)

- **Review**: Gets max 10 flashcards that needs more practice for a review deck and shows one per page using Django paginator.  

![Review view](https://github.com/SofiaBracho/flashcards/blob/master/media/review.PNG)

- **Learned**: Gets all learned flashcards ordered by last studied date time, using Paginator shows 5 per page.

![Learned view](https://github.com/SofiaBracho/flashcards/blob/master/media/learned.PNG)

- **Profile**: Gets user stats and renders stats template.

![Profile view](https://github.com/SofiaBracho/flashcards/blob/master/media/profile.PNG)

- **Login**: Handles user login by checking if provided credentials match those stored in the database and redirects accordingly. If not logged in, renders login page with error message (if any).

![Login view](https://github.com/SofiaBracho/flashcards/blob/master/media/login.PNG)

- **Logout**: Logs out current user by removing session data and displaying login page.


## 🛠️ Getting Started

### Prerequisites

Here's what you need to be able to run this App:

- Node.js
- MySQLI
- Python
- Django

### 1. Clone the repository

```shell
git clone https://github.com/SofiaBracho/flashcards.git
cd flashcards
```

### 2. Migrate database models

```shell
python manage.py makemigrations
python manage.py migrate
```

### 3. Run the dev server

```shell
python manage.py runserver
```

### 4. Open the App in your local host

```shell
http://localhost:8000
```

### 5. Register and login

Create your user account in the `/register` route, then login into the form in the `/login` route.


## 🔀 Contributing

Flashcards is an open-source project and anyone from the community can contribute to it.

If you'd like to contribute, fork the repository and make changes as you'd like. Pull requests are welcome.

### 👥 Author
**Sofia Bracho**

<a href="https://github.com/SofiaBracho">
  <img src="https://github.com/SofiaBracho/flashcards/blob/master/media/author.png" styles="width:75px;" alt="Author"/>
</a>
