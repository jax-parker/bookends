# **Bookends - Project Portfolio 4**

[Bookends](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691077259/screenshots_xjqlvb.png)

Bookends is a fictitious website that provides ideas for any book clubs next best read. Designed 'mobile first' the site provides users with a book list with the book cover, title, author, genre, description and reviews that any site user can add once they have signed up/in. Once signed in the user can edit or delete their entries and see a list of books that they have added.

You can view the live site here - <a href="https://django-bookends.herokuapp.com/" target="_blank">Bookends </a>

# User Experience (UX)
## Site Aims
* To provide the user with a website that allows them to view books, descriptions and reviews
* To easily find books that may appeal to the members of their book club
* To allow users that have signed up to create, update, edit or delete their book entries
* To provide the admin user with the ability to delete users
* To provide a clear and appropriate response to any user inputs or actions

## Agile Methodology
The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board, which can be seen here -

Through the use of the Kanban board in the projects view in Github, the project was divided into a few different sections:
[Kanban board github](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690981983/kanban-board_vr0jps.png)

A User Story template was created then Github issues were used to create User Stories for the project.  

### User Stories

**User Story: Account Registration**
* As a Site User I can register an account so that I can view books or add a review

**User Story: LogIn/LogOut/SignUp**
* As a Returning Site User I can log in, view books in detail, create my own book listing and review and log out.

**User Story: View Book List**
* As a Site User I can view a list of books so that I can see the book cover, title and description.

**User Story: Book Detail**
* As a Site User I can click on a book in the list view so I can read more details and the review.

**User Story: Create A Review**
* As a Site User I can create a book review so that other members can see my reviews.

**User Story: Manage Book Reviews**
* As a Site User I can create, read, update & delete books so that I can manage my book content

**User Story: Search For Books**
* As a Site User I can search for books using key words so that I don't have to scroll through the books to get to the one I want

## Design Wireframes

### Low fidelity mobile wireframes
* [Home Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076598/wireframe-mb-home_honamm.png)
* [Book List Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076598/wireframe-mb-listview_oiec9x.png)
* [Book Detail Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076597/wireframe-mb-detailview_nifvye.png)
* [Add A Review Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076597/wireframe-mb-addreview_j87s9j.png)
* [Your Books Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076598/wireframe-mb-yourbooks_bk5gyq.png)
* [Log In Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076598/wireframe-mb-signin_jhfkne.png)
* [Sign Up Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076598/wireframe-mb-signup_mgs3f8.png)
* [Log Out Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076598/wireframe-mb-signout_dgvhal.png)
* [Search Not Found Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076598/wireframe-mb-nonefound_nzvrpw.png)

### Low fidelity pc wireframes
* [Home Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076597/wireframe-pc-home_gmbzap.png)
* [Book List Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076597/wireframe-pc-listview_qcwfjz.png)
* [Book Detail Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076597/wireframe-pc-detailview_zfobqz.png)
* [Add A Review Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076597/wireframe-pc-addreview_tahjxq.png)
* [Your Books Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076597/wireframe-pc-yourbooks_omj3hq.png)
* [Log In Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076597/wireframe-pc-signin_dpdqcx.png)
* [Sign Up Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076597/wireframe-pc-signup_xyrdiy.png)
* [Log Out Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076597/wireframe-pc-signout_ni0dus.png)
* [Search Not Found Page](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691076597/wireframe-pc-nonefound_aav7ff.png)

## Entity Relationship Diagram
#### Database layout using Exclaidraw
![Database Schema](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691077013/database-schema_lezbhx.png)

## Code Schema
#### Code workflow using Exclaidraw
![Code Schema](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691077024/code-schema_ppijwv.png)

## Site Structure
From the home page, Bookends website has three pages visible in the navigation bar plus the search bar; Home, Sign Up and Login. Once signed in the nav bar then
has Book List, Add A Review, Your Books and Logout. This ensures that only users that have signed in are authorised to see the book list, add a review and the book list they have
added.

## Design Choices

### Logo
I used a website called [Looka](https://looka.com/logo-maker) to design the logo. It gives you a choice of colours, fonts and icons that you can choose which would be best for your design. 

### Colour Scheme
The colour scheme was based around the logo I chose. Looka.com then provided me with a colour palette to use within my project.
![Colour Palette](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691077103/color-palette_gdjauy.png)
### Typography
I chose two fonts from Google Fonts for this project, but both from the same family. Roboto Slab and Roboto (weight:300). Both are contrasting but clear to read.
# Features
## Navigation
The site navigation is done through the navigation bar at the top of each page and does not change in style through out the users navigation of the webisite. 
There is a search bar which will search through the list of books' titles, authors, description or any word in the review. The nave bar shrinks to a Bootstrap toggle on smaller screens and opens to a dropdown when clicked on. Each link is active so will be underlined when the user is on the specific page.

![Navbar Mobile](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691004625/navbar-mobile_xiaw5o.png)
![Navbar PC](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690997395/navbar_bqmo5s.png)

## Home Screen
The Home Screen is visible when the website is opened. Along with the navbar and the footer, the main section contains a message to explain what the webstie is about
and displays 3 example book covers. These can be clicked on to see an example of the book detail but the user only has access to these three. They will need to sign up to have
access to the whole library of books and reviews.

![Home Page Mobile](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984229/home-mbview_qiao1x.png)
![Home Page PC](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984230/pcview-home_w5moih.png)

## Sign Up Screen
The sign up page is accessed from either the navigation bar or a link on the log in page for any user who may have clicked login by mistake.
It uses django-allauth and crispy forms to provide the styling and the settings for user authentication. (Username, Email(optional) and Password)

![Sign Up Page Mobile](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984229/mbview-signup_jusatd.png)
![Sign Up Page PC](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984230/pcview-signup_kruiu8.png)
## Login Screen
The login page is accessed from either the navigation bar or a link on the sign in page for any user who may have clicked signup by mistake.
It uses django-allauth and crispy forms to provide the styling and the settings for user authentication.  (Username, Password)

![Login Page Mobile](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984228/mbview-signin_lhmrpu.png)
![Login Page PC](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984229/pcview-signin_wlllfu.png)

## Book List Screen
When a user is logged in they can view all the book covers and and the first part of the description. To view the book in more detail in see the 
review they simply click on the book.

![Book List Screen Mobile](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984228/mbview-booklist_iifrmy.png)
![Book List Screen PC](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984229/pcview-booklist_ewr6jv.png)

## Book Detail Screen
When a user is logged in they can click any book in the list to view the books title, posted by & date, author, book type, full description and review.
If it is a book that they have posted they can edit the book listing or delete it. If they click delete a confirm deletion page will show with a button
for them to confirm.

![Book Detail Screen Mobile](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984229/mbview-bookdetail_xkesu9.png)
![Book Detail Screen PC](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984229/pcview-bookdetails_b3csg4.png)
![Delete Book Confirmation Mobile](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691003992/mbview-confdelete_dqi6ez.png)
![Delete Book Confirmation PC](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691003992/pcview-confdelete_jsevhg.png)
## Add A Review Screen
When a user is logged in they click on Add A Review and fill in the form to add thier own book and review it.

![Add A Review Mobile](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984228/mbview-addreview_jkm7br.png)
![Add A Review PC](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984229/pcview-addreview_hysper.png)
## Your Books Screen
When a user is logged in they can view a list of all the books they have added to the website. They can then use the search bar to find their book listing.

![Your Books Screen Mobile](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984229/mbview-yourbooks_gui3eb.png)
![Your Books Screen PC](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984230/pcview-yourbooks_vgl6ow.png)
## Logout Screen
The logout screen can be accessed from the navbar only when the user is logged in. The log out page has a confirmation button to check the user wishes to sign out.
It uses django all-auth and crispy forms to provide the styling and the settings for user confirmation. 

![Sign Out Confirm Mobile](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690984228/mbview-signout_ildkwl.png)
![Sign Out Confirm PC](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691004998/pcview-logout_u8bduj.png)
## Search Bar (not found) screen
When a user types into the search bar but nothing is found a page to say there was no result is displayed and a button to take the user back to the book list. 

![No Search Mobile](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690997641/mbview-nosearch_hnb5mr.png)
![No Search PC](https://res.cloudinary.com/dwvsz0fug/image/upload/v1690995797/pcview-nosearch_en780f.png)

## Footer
The footer contains social icons which link to the websites social media sites.

![Footer](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691005624/Footer_jsruj9.png)

# Technologies Used

* HTML - Used to structure all the templates on the site
* CSS - to provide extra styling to the site
* Python - To provide the functionality to the site. Packages used in the project can be found in requirements.txt
* Django - Python framework used in the project
* Heroku - Used to deploy the site publicly
* ElephantSQL - Used for the database during development and deployment
* Bootstrap5 -  used for providing layouts and styling the html in the templates
* Balsamiq - Used to create wireframes for the project
* Cloudinary - Used to host Static files for the site
* Excalidraw - Used to create the Entity Relationship Diagram and Code Schema
* Looka.com - Used to create the Bookends Logo
* Black - intalled black in terminal and ran to ensure PEP8 compliant in files
* Breakpoint - used breakpoint() to step through code in terminal and check each step is working to help debug
* URL Encode Online - to encode my url to add to the validation checkers to add links to testing section

[Back to top](<#contents>)

# Testing
## Validation
### Html Validation
Html validation was done with [https://validator.w3.org/nu/](https://validator.w3.org/nu/).
On website page, right click, view page source, copy code and paste into validator. Repeat for each page.
Results 
* [Home](https://validator.w3.org/nu/?doc=https%3A%2F%2F8000-jaxparker-bookends-r6l7rti2x81.ws-eu102.gitpod.io)
* [Book List](https://validator.w3.org/nu/?doc=https%3A%2F%2F8000-jaxparker-bookends-r6l7rti2x81.ws-eu102.gitpod.io%2Fbooks%2F)
* [Book Detail](https://validator.w3.org/nu/?doc=https://8000-jaxparker-bookends-r6l7rti2x81.ws-eu102.gitpod.io/books/9/)

### CSS Validation

The stylesheet was validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)
![CSS Validator Check](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691070801/css-validator_q9mxyn.png)
Errors: None

### Python Validation

Python code that I have written was validated using [Code institues Python validator](https://pep8ci.herokuapp.com/#)
No errors were found:
* [main/settings.py](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691074311/test-home-settings.py_jodfa5.png)
* [main/urls.py](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691074311/test-main-urls.py_b7sogd.png)
* [main/urls.py](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691074311/test-main-urls.py_b7sogd.png)
* [home/views.py](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691074311/test-home-views.py_cgffnk.png)
* [home/urls.py](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691074312/test-home-urls.py_qv8hww.png)
* [books/views.py](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691074311/test-books-views.py_zjs9bi.png)
* [books/urls.py](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691074311/test-books-urls.py_yevtdr.png)
* [books/models.py](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691074311/test-books-models.py_xurycf.png)
* [books/forms.py](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691074311/test-books-forms.py_ijc43m.png)
* [books/admin.py](https://res.cloudinary.com/dwvsz0fug/image/upload/v1691074311/test-books-admin.py_wtflbb.png)

### Lighthouse Testing
* [Home Page]()
* [Book List Page]()
* [Book Detail Page]()
* [Home Page]()

## Manual Testing

In addition to the other tests, I have conducted a manual check list for myself to carry out to make sure that everything is working as intended.

| Status | **Navigation Bar - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the navbar logo loads the home page
| &check; | The navbar shows home, signup and login tabs
| &check; | Clicking the home tab on the navbar loads the home page
| &check; | Clicking the sign up tab on the navbar loads the signup page
| &check; | Clicking the login tab on the navbar loads the login page
| &check; | Clicking the home tab on the navbar loads the home page

| Status | **Navigation Bar - User Logged In**
|:-------:|:--------|
| &check; | The navbar shows the home, book list, add a review, your books and log out tabs
| &check; | Clicking the home tab loads the home page
| &check; | Clicking the book list tab loads the book list page
| &check; | Clicking the add a review tab loads the add a review page
| &check; | Clicking the your books tab loads the your books page
| &check; | Clicking the logout tab loads the logout page

| Status | **Footer - User Logged In/out**
|:-------:|:--------|
| &check; | Clicking the LinkedIn icon opens its home page in a new window
| &check; | Clicking the Instagram icon opens its home page in a new window
| &check; | Clicking the Twitter icon opens its home page in a new window
| &check; | Clicking the YouTube icon opens its home page in a new window
| &check; | Clicking the Facebook icon opens its home page in a new window

| Status | **Home Page - User Logged In/out**
|:-------:|:--------|
| &check; | Info message shows with 3 books in main section
| &check; | Clicking on any of the 3 books takes you to the book detail

| Status | **Book List Page - User Logged In**
|:-------:|:--------|
| &check; | List of books images appear with title and start of description below each
| &check; | Title and description change colour and pointer changes to hand on hover
| &check; | Clicking on any book takes you to the book detail

| Status | **Book Detail Page - User Logged In**
|:-------:|:--------|
| &check; | Book cover appears on left
| &check; | Title, user, post date and time, author, book type, description and review to right
| &check; | If book opened belongs to user the edit and delete buttons appear
| &check; | Clicking on edit button takes user to edit a review page, allows them to edit and finish editing button returns to book list page
| &check; | Clicking on delete takes user to confirm book deletion page with confirm button removing book from list returning to book list page

| Status | **Add A Review/Book Page - User Logged In**
|:-------:|:--------|
| &check; | Form appears centrally with entries book, author, description, review, image, image description, genre inputs
| &check; | Book review allows user to use formatting for their review
| &check; | Genre dropdown box shows all genres created in admin
| &check; | Submit button adds book to book list and returns user to book list page showing new book at front

| Status | **Your Books Page - User Logged In**
|:-------:|:--------|
| &check; | Your Books title and list of books added by that user. Different users were created to test

| Status | **Log In Page**
|:-------:|:--------|
| &check; | Message to check if user has a log in - sign up link takes user to sign up page
| &check; | Form appears with username and password input boxes and sign in button 
| &check; | Sign in button take user to book list page

| Status | **Sign Up Page**
|:-------:|:--------|
| &check; | Message to check if user has an account - log in link takes user to log in page
| &check; | Form appears with username, email(optional) and password input boxes and sign up button 
| &check; | Sign up button take user to home page

| Status | **Log Out Page**
|:-------:|:--------|
| &check; | Confirmation of log out appears and sign out button signs user out and returns to home page

| Status | **Search Bar**
|:-------:|:--------|
| &check; | Searching for book title returns book
| &check; | Searching for author returns book
| &check; | Searching for book title returns book
| &check; | Searching for description word returns book(s)
| &check; | Searching for unfound word takes you sorry no books found page
| &check; | No books found page displays message and return to books list button takes you to book list

## Bugs
* I had made the mistake of pushing my repo to git hub before adding env.py to my gitignore file which stopped my env from 'greying' and becoming secret. Firstly I had to remove the cached version with git rm --cached env.py. I then had to delete the file and commit, then recreated it. I then had to generate new secrets as my old ones had been exposed in github, recreate a superuser and add books back in to user accounts.

* I originally only copied over the sign up, log in and out AllAuth files as I mistakenly thought this would be ok but this caused a 403 forbidden error in my code. Student Support explained that as allauth had a lot of things going on in the background it was advisable to copy all of the allauth files over even if you're not using them. I did this and this resolved the issue.

* Search that doesn't exist returned a TypeError message. So I added an {% empty %} in the books.html template and entered a message and button to return the user to the books list page.

* After running the git rm --cached env.py as stated above, this caused issues in gitpod, bringing through old workspaces which were resolved by deleting old workspaces but then I could not push to git as it wanted me to pull first as I'd unknowingly completed work in old workspaces. I ran git pull and got an error saying I had divergent branches. I then ran git config pull.rebase false to pull data from my repo, commit and push.


# Deployment

## Deployment to Heroku

### 1. Creating the Django Project
* If development if being done locally: Activate your virtual environment
* To ensure the virtual environment is not tracked by version control, add .venv to the .gitignore file.
* Install Django and gunicorn: `pip3 install django gunicorn`
* Install supporting database libraries dj_database_url and psycopg2 library: `pip install dj_database_url psycopg2`
* Install Cloudinary libraries to manage static files: `pip install dj-3-cloudinary-storage`
* Create file for requirements: `pip freeze --local > requirements.txt`
* Create project:`django-admin startproject project_name .`
* Create app: `python manage.py startapp app_name`
* Add app to list of `installed apps` in settings.py file: `'app_name'`
* Migrate changes: `python manage.py migrate`
* Test server works locally: `python manage.py runserver`

### 2. Create your Heroku app
* Navigate to the Heroku website
* Create a Heroku account by entering your email address and a password (or login if you have one already).
* Activate the account through the authentication email sent to your email account
* Click the **new button** on the top right corner of the screen and select create a new app from the dropdown menu.
* Enter a unique name for the application.
* Select the appropriate region for the application.
* Click create app
* In the Heroku dashboard click on the Resources tab
* Scroll down to Add-Ons, search for and select 'Heroku Postgres'
* In the Settings tab, scroll down to 'Reveal Config Vars' and copy the text in the box beside DATABASE_URL.

### 3. Set up Environment Variables
* In you IDE create a new env.py file in the top level directory
* Add env.py to the .gitignore file
* In env.py import the os library
* In env.py add `os.environ["DATABASE_URL"]` = "Paste in the text link copied above from Heroku DATABASE_URL"
* In env.py add `os.environ["SECRET_KEY"] = "Make up your own random secret key"
* In env.py add `os.environ["CLOUDINARY]` = "Paste in the API Environment Variable link from Cloudinary and remove the prefix"
* In Heroku Settings tab Config Vars enter the same secret key created in env.py by entering 'SECRET_KEY' in the box for 'KEY' and your randomly created secret key in the 'value' box.

### 4. Setting up settings.py

* In your Django 'settings.py' file type:

 ```
 from pathlib import Path
 import os
 import dj_database_url

 if os.path.isfile("env.py"):
  import env
 ```
* Remove the default insecure secret key in settings.py and replace with the link to the secret key variable in Heroku by typing: `SECRET_KEY = os.environ.get(SECRET_KEY)`
* Comment out the `DATABASES` section in settings.py and replace with:
```
DATABASES = {
  'default': 
  dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }`
```
* Create a Cloudinary account and from the 'Dashboard' in Cloudinary copy your url into the env.py file by typing: `os.environ["CLOUDINARY_URL"] = "cloudinary://<insert-your-url>"`
* In Heroku  add cloudinary url to 'config vars'
* In Heroku config vars add DISABLE_COLLECTSTATIC with value of '1' (note: this must be removed for final deployment)
* Add Cloudinary libraries to the installed apps section of settings.py file:
 ```
 'cloudinary_storage'
 'django.contrib.staticfiles''
 'cloudinary'
 ```
* Connect Cloudinary to the Django app in `settings.py`:
```
STATIC_URL = '/static'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'STATIC')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage'
* Link file to the templates directory in Heroku 
* Place under the BASE_DIR: TEMPLATES_DIR = os.path.join(BASE_DIR,
'templates')
```
* Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array: `'DIRS': [TEMPLATES_DIR]`
* Add Heroku Hostname to ALLOWED_HOSTS: ```ALLOWED_HOSTS =
['rhi-book-nook.herokuapp.com', 'localhost']```
*Create Procfile at the top level of the file structure and insert the following:
    ``` web: gunicorn PROJECT_NAME.wsgi ```

* Make an initial commit and push the code to the GitHub Repository.
    ```git add .```
    ```git commit -m "Initial deployment"```
    ```git push```

### 5. Heroku Deployment: 
* Click Deploy tab in Heroku
* In the 'Deployment method' section select 'Github' and click the 'connect to Github' button to confirm.
* In the 'search' box enter the Github repository name for the project
* Click search and then click connect to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository.

### 6. Final Deployment
In the IDE: 
* When development is complete change the debug setting to: `DEBUG = False` in `env.py` 
* In Heroku settings config vars change the DISABLE_COLLECTSTATIC value to 0
* Because DEBUG must be switched to True for development and False for production it is recommended that only manual deployment is used in Heroku. 
* To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

## To fork the repository on GitHub

A copy of the GitHub Repository can be made by forking the GitHub account. Changes can be made on this copy without affecting the original repository.

1. Log in to GitHub and locate the repository in question.
2. Locate the Fork button which can be found in the top corner, right-hand side of the page, inline with the repository name.
3. Click this button to create a copy of the original repository in your GitHub Account.

## To clone the repository on GitHub

1. Click on the code button which is underneath the main tab and repository name to the right.
2. In the 'Clone with HTTPS' section, click on the clipboard icon to copy the URL.
3. Open Git Bash in your IDE of choice.
4. Change the current working directory to where you want the cloned directory to be made.
5. Type git clone, and then paste the URL copied from GitHub.
6. Press enter and the clone of your repository will be created.

[Back to top](<#contents>)

# Credits
* [Looka.com](https://looka.com/)
* [Django Girls](https://tutorial.djangogirls.org/en/)
* [learndjango.com](https://learndjango.com/tutorials/)
* [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
* [Setting up a global .gitignore file](https://sebastiandedeyne.com/setting-up-a-global-gitignore-file/)
* [Uxwing for social icons](https://uxwing.com/)

[Back to top](<#contents>)

# Acknowledgements
This website was designed and developed in conjuction with the Full Stack Software Developer Diploma Course at Code Institute. Thank you to my mentor Ronan McClelland for his guidance and support throughout my project and to Student Support for their patience and knowledge.