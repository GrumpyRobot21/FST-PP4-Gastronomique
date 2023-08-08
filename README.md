# Gastronomique -Restaurant Booking System

## Introduction
This is my fourth project. This project is a restaurant (Gastronomique) booking system, allowing users to make a reservation. This application uses the following languages: Django, Python, HTML, CSS and JavaScript.

This project demonstrates CRUD functionality (Create, Read, Update, Delete). The user is able to create, read, update and delete their reservation as well as create a profile and login/logout of the site.

A live website can be found [here](https:///).

![website preview](<img src="assets/images/headerbar.png"?raw=true alt=" picture of the navigation bar"></p>)

# Table of Contents

-   [1. UX](#ux)
    -   [1.1. Strategy](#strategy)
        -   [Project Goals](#project-goals)
            -   [User Goals:](#user-goals)
            -   [User Expectations:](#user-expectations)
            -   [Trends of Modern Websites](#trends-of-modern-websites)
            -   [Strategy Table](#strategy-table)
    -   [1.2. Structure](#structure)
    -   [1.3. Skeleton](#skeleton)
    -   [1.4. Surface](#surface)
-   [2. Features](#features)
-   [3. Technologies Used](#technologies-used)
-   [4. Testing](#testing)
-   [5. Development Cycle](#development-cycle)
-   [6. Deployment](#deployment)
-   [7. End Product](#end-product)
-   [8. Known Bugs](#known-bugs)
-   [9. Credits](#credits)

<a name="ux"></a>

# 1. UX

[Go to the top](#table-of-contents)

A simple online booking system makes ging to a restaurant a stress free and enjoyable experience.

This project provides diners with a simplea and easy way to creat a user profile, make a reservation, update a reservation and delete a reservation.

<a name="strategy"></a>

## 1.1. Strategy

[Go to the top](#table-of-contents)

### Goals
The project goals are to allow the user to be able to sign up, sign in/out, create a user profile and create/update/delete a reservation easily via this application.

### User Goals:
First Time Visitor.
-   As a first-time visitor, I want to make a reservation at my preferred date and time.
-   As a first-time visitor, I want to view the menu for the restaurant.
-   As a first-time visitor, I want to be able to easily contact the restaurant.
-   As a first time visitor, I want to be able to easily create a user account to access my private reservation information.

Returning Visitor Goals
-   As a Returning visitor, I want to be able to log in and out of my user account.
-   As a Returning Visitor, I want to update my reservation.
-   As a Returning Visitor, I want to cancel my reservation.

Frequent User Goals
-   As a Frequent User, I want to see if the menu has been changed and view the gallery.

### User Expectations:
The application should provide a simple user interface, with clear and concise site navigation.

-   The menu is easy to locate and easy to read.
-   The site is easy to navigate.
-   The website is fully responsive.
-   There is a clear way to contact the restaurant.

### User Stories
Throughout the project I used the GitHub projects board to log all user stories as my project management tool. This helped me keep focus on the necesarry tasks as I would move them to the "in progress lane" as I'm working on the story. I would then move them to the "done" lane once the story has been completed.

![user_story_board](documentation_assets/images/project_board.png)

### Strategy Table
Opportunity/Problem/Feature| Importance| Viability/Feasibility
------------ | -------------------------|---------
Display a Menu | 5 | 5
Account signup | 5 | 5
User profile | 1 | 4
Responsive design | 5 | 5
Contact form | 5 | 5
Ability to create a booking | 5 | 5
Ability to update a booking | 5 | 5
Ability to cancel a booking | 5 | 5
Multiple table occupancies | 1 |4
Avoid double bookings | 1 | 5

Total | 38 | 48

## Scope
I was not able to include all of the features from the above table. As a result the project has been designed in it's first incarnation as a minimum viable product. Please find below the design parameters and ideas to include in a future phase.

### Minimum viable product - Basic functionality
- Display a menu
- Allow users to register for an account
- Allow users to log in and out of their account
- Responsive design
- Contact form
- Ability to create a reservation
- Ability to update a reservation
- Ability to cancel a reservation

### Future functionality to add
- Multiple table occupancies
- Avoid double bookings
- Contact form model, so messages are saved to the database
- Email confirmation when a message has been received.
- Account email verification
- Allow users to create and edit a personal profile

<a name="structure"></a>

## 1.2. Structure

[Go to the top](#table-of-contents)

A key component is to have responsive design in this project as most users access applications on multiple device types (mobile, tablet, laptop/PC). This application has been designed to be:

- Responsive on all device sizes
- Easily navigated through clear labelling and uncluttered design
- All elements share a consistent style including font size, font family, colour schemes etc.

### Database Model

Final database structure:

```python
class Reservations(models.Model):
    """Reservations model definitions"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()

    def __str__(self):
        return self.name
```

<a name="skeleton"></a>

## 1.3. Skeleton

[Go to the top](#table-of-contents)

### Wire-frames

Home Page:
![home_page](docs/wireframes/home.png)

Conatct Page:
![contact_page](docs/wireframes/contact_page.png)

Thank you for message Page:
![thanks_message_page](docs/wireframes/thanks_message_page.png)

Registration Page:
![register_page](docs/wireframes/register_page.png)

Login Page:
![login_page](docs/wireframes/login_page.png)

Reservation created successfully Page:
![res_success_page](docs/wireframes/res_success_page.png)

My Reservations page:
![myres_page](docs/wireframes/myres_page.png)

Make a Reservation Page:
![make_a_res_page](docs/wireframes/make_a_res_page.png)

Update a reservation page:
![update_res_page](dos/wireframes/update_res_page.png)

Delete a reservation:
![delete_res_page](docs/wireframes/delete_res_page.png)

Logout Page:
![logout_page](docs/wireframes/logout_page.png)


<a name="surface"></a>

## 1.4. Surface

[Go to the top](#table-of-contents)

### Colours

I used the following colors in my design to keep the overall layout simple and cler: #339966, #fff, #00ced1, #000000 .

### Typography

I decided to use Indie Flower as my font of choice with sans serif as my backup font for browsers that might not support Be Vietnam Pro.

The link to the font can be found [here](https://fonts.google.com/specimen/Indie+Flower/about).

<a name="features"></a>

# 2. Features

[Go to the top](#table-of-contents)

### All Pages
- The navigation bar is at the top of all the pages. The navigation bar is dynamic so that depending whether or not the user is logged in, the options will change.
- If the user is not logged in the navigation bar will look like this:
![user_logged_out](documentation_assets/images/navbar_not_logged_in.png)
- If the user is logged in the navigation bar will look like this:
![user_logged_in](documentation_assets/images/navbar_logged_in.png)
- The footer is placed at the bottom of each page.
- The restaurant name is placed at the top of all pages. It performs no additional function due to the inclusion of a home button in the navigation links. It dissappears on mobile screes to accomodate the navbar links.

### Registration Page
- A simple signup form that requires the user to enter a unique username, email address and password. The password must be entered again for confirmation, this must match the already entered password above.
- If the user enters an email address that has already been registered, the user is prompted by an error message.
- If the user enters a password that is not secure, the user will be prompted by a message.
- If the user enters both passwords that do not match, the user is prompted by a message.
- Once the user has successfully signed up, they will be directed to the make a reservation page.

### Login Page
- A login form that requires the user to enter their email address and password that they used when signing up to the site.

### Logout Page
- When clicking logout from the navigation bar, the user is redirected to the home page.

### Home Page
- A simple but elegant banner to give the user a sense of the restaurant with an image and about us text.
-A menu with a nav link in the navbar to take user straigh to this infomration. There is a back to top of page link for the user once they have read the menu.
- A gallery section with enticing picture of the restaurant food offereings. There is a back to top of page link for the user once they have read the menu.

### Contact Page
- This perovides users with the ability to contact the restaurant voa a contact form. This will provide error messages when incorrect data is entered and has a message sent confirmation screen once the message has been submitted by the user.

### Reservations Page
- This allows the user to create a reservation on their preferred date and time. If oncirrect data is entered they will receive an error message. They are directed to a reservation confirmation page once their reservation has been successfully submitted and are then asked to navigate to the reservation list page.

### My Reservations Page
- Thsi provides the user with a list of their confirmed reservations. It provides them with the option to delete their reservation or update their reservation. 

### Delete Reservation
-This page confirms that the user wishes to truly delete their reservation or cancel that decision. Two buttons are provided. Idf deleted the user is taken back to their reservation list which will now not display the deleted reservation. If there sre no reservations left it will display a no reservations found message.

### Update reservation
- The user is taken to their reservation detaisl where they can change any part of the stored data. Once completed they are taken back to their reservation list page and they will see the confirmed changes made to their reservation.

<a name="technologies-used"></a>

## 3. Technologies Used

[Go to the top](#table-of-contents)

-   [HTML5](https://en.wikipedia.org/wiki/HTML) (Programming Language)
    
-   [CSS3](https://en.wikipedia.org/wiki/CSS) (Programming Language)
    
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript) (Programming language)
    
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    
-   [PostgreSQL](https://www.postgresql.org/) Database
    
-   [Gitpod](https://www.gitpod.io/) Cod environment
    
-   [Chrome](https://www.google.com/intl/en_uk/chrome/) Debugging
    
-   [Figma](https://www.figma.com/) Wireframes
       
-   [Google Fonts](https://fonts.google.com/)
    
-   [GitHub](https://github.com/) Repository
   

<a name="testing"></a>

# 4. Testing

[Go to the top](#table-of-contents)

### Google Developer Tools
Developer tools enabled me to establish which parts of my code were not working and to try options out before settling on my chosen solution. 

I checked the accessibility of the page using lighthouse.
![google_lighthouse](documentation_assets/images/google_lighthouse.png)

### Responsive Tools
I used [Am I Responsive](http://ami.responsivedesign.is) to make sure that all my pages are responsive to all devices.

### W3C Validator Tools
#### HTML:
I used [W3C Markup](https://validator.w3.org/#validate_by_input+with_options) to check for any errors within the HTML pages.
#### CSS:
I used [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) to check for any errors within my CSS stylesheet.

I had no errors in my CSS file:
![css_validation](docs/images/css_validation.png)

### JavaScript:
I used [JS Hint](https://jshint.com/) to check for any errors within my JavaScript script tags. 

I had no errors in my JavaScript files:
![javascript_validation](docs/images/javascript_validation.png)

### Python:
I used [PEP8 online](http://pep8online.com/) to check for any errors within my Python files. The validator showed multiple "line too long" errors. This was rectified by adding each statement as a new line.

There were also "line too long" errors within my settings.py file but I have chosen to ignore these as this is a very important file and despite trying to rectify these errors I was unsuccessful.

## Manual Testing
I have tested my site on Safari and google chrome on multiple devices.

These include:
-   Dell Inspiron 15 Laptop
-   Samsung Galaxy S20 FE


Please find below my testing process for all pages via mobile and web:

### Navigation Bar

All Pages:
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Home page | When clicking the "home" link in the navigation bar, the browser redirects me to the home page. The active styling will turn the menu text turquoise when hovered over. | PASS
Menu section | When clicking the "menu" link in the navigation bar, the browser redirects me to the menu section. The active styling will turn the menu text turquoise when hovered over. | PASS
Gallery section | When clicking the "Gallery" link in the navigation bar, the browser redirects me to the interactive gallery section. The active styling will turn the menu text turquoise when hovered over. | PASS
Contact page | When clicking the "contact" link in the navigation bar, the browser redirects me to the contact page. The active styling will turn the menu text turquoise when hovered over. | PASS
Message sent confirmation | When clicking the "submit" button in the contact page, the browser redirects me to the message sent confirmation page. The active styling will turn the menu text turquoise when hovered over.| PASS
Login page | When clicking the "Login" link in the navigation bar, the browser redirects me to the Login page. The active styling will turn the menu text turquoise when hovered over.| PASS
Registration page | When clicking the "Regiatration" link in the navigation bar, the browser redirects me to the user registration page. The active styling will turn the menu text turquoise when hovered over. | PASS
Reservations page | When clicking the "Reservations" link in the navigation bar, the browser redirects me to the make a reservation page. The active styling will turn the menu text turquoise when hovered over.| PASS
My reservations page | When clicking the "My Reservations" link in the navigation bar, the browser redirects me to the reservation list page. The active styling will turn the menu text turquoise when hovered over.| PASS
Logout link | When clicking the "Logou" link in the navigation bar, the browser redirects me to the Home page. The active styling will turn the menu text turquoise when hovered over.| PASS
Reservation confirmation | When clicking the "submit" button in the reservations page, the browser redirects me to the reservation booking successful page. The active styling will turn the menu text turquoise when hovered over.| PASS

### Home page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS

![index_google_lighthouse](documentation_assets/images/index_google_lighthouse.png)

### Menu page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Book now button | When clicking the book now button on the page, the browser redirects to the booking page. | PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS

![menu_google_lighthouse](documentation_assets/images/menu_google_lighthouse.png)

### Contact page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Book now button | When clicking the book now button on the page, the browser redirects to the booking page. | PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Contact Form | Checked the form submits only when all fields are filled out. | PASS

![contact_google_lighthouse](documentation_assets/images/contact_google_lighthouse.png)

### Booking page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Book now button | When clicking the book now button on the page, the browser redirects to the booking page. | PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Booking Form | Checked the form submits only when all required fields are filled out. | PASS
If not signed in | Checked to see if the user has not signed in the booking form should not show and a message displays prompting the user to signup/sign-in first. | PASS

![booking_google_lighthouse](documentation_assets/images/booking_google_lighthouse.png)

### Edit booking page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Edit Booking Form | Checked the form submits only when all required fields are filled out. | PASS
Form validation | Checked that the telephone number input only allows number input and not any text | PASS

![edit_booking_google_lighthouse](documentation_assets/images/edit_booking_google_lighthouse.png)

### Manage booking page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Edit booking button | Checked that the button redirects to the edit booking page with the correct booking instance. | PASS
Cancel booking button | Checked that the button redirects to the cancel booking page with the correct booking instance. | PASS

![manage_booking_google_lighthouse](documentation_assets/images/manage_booking_google_lighthouse.png)

### Create profile page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Create profile form | Checked the form submits only when all required fields are filled out. | PASS
If the profile has not been created | Checked to see if the user has created a profile, if not it will redirect the user to the create profile page | PASS
Form validation | Checked that the telephone number input only allows number input and not any text | PASS

![create_profile_validation](documentation_assets/images/create_profile_input_validation.png)
![create_profile_google_lighthouse](documentation_assets/images/create_profile_google_lighthouse.png)


### Edit profile page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Edit profile form | Checked the form submits only when all required fields are filled out. | PASS
Form validation | Checked that the telephone number input only allows number input and not any text | PASS
If the profile has not been created | Checked to see if the user has created a profile, if not it will redirect the user to the create profile page | PASS

![edit_profile_google_lighthouse](documentation_assets/images/edit_profile_google_lighthouse.png)

### Register page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Register form | Checked the form submits only when all required fields are filled out. | PASS
Sign in link | Checked the sign-in link redirects to the sign-in page. | PASS

![signup_google_lighthouse](documentation_assets/images/sign_up_google_lighthouse.png)

### Sign in page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Sign in form | Checked the form submits only when all required fields are filled out. | PASS
Signup link | Checked the signup link redirects to the signup page. | PASS

![sign_in_google_lighthouse](documentation_assets/images/sign_in_google_lighthouse.png)

<a name="development-cycle"></a>

# 5. Development Cycle

[Go to the top](#table-of-contents)

## Project Checklist
- Install Django and the supporting libraries
    -  Install Django and Gunicorn. Gunicorn is the server I am using to run Django on Heroku.
    - Install support libraries including psycopg2, this is used to connect the PostgreSQL database
    - Install Cloudinary libraries, this is a host provider service that stores images
    - Create the requirements.txt file. This includes the project's dependencies allowing us to run the project in Heroku.

- Create a new, blank Django Project
    - Create a new project
    - Create the app
    - Add restaurant_booking to the installed apps in settings.py
    - Migrate all new changes to the database
    - Run the server to test

- Setup project to use Cloudinary and PostgreSQL
    - Create new Heroku app
        - Sign into Heroku
        - Select New
        - Select create new app
        - Enter a relevant app name
        - Select appropriate region
        - Select the create app button

    - Attach PostgreSQL database
        - In Heroku go to resources
        - Search for Postgres in the add-ons box
        - Select Heroku Postgres
        - Submit order form

    - Prepare the environment and settings.py file
        - Create env.py file
        - Add DATABASE_URL with the Postgres URL from Heroku
        - Add SECRET_KEY with a randomly generated key
        - Add SECRET_KEY and generated key to the config vars in Heroku
        - Add if statement to settings.py to prevent the production server from erroring
        - Replace insecure key with the environment variable for the SECRET_KEY
        - Add Heroku database as the back end
        - Migrate changes to new database

    - Get static media files stored on Cloudinary
        - Create a Cloudinary account
        - From the dashboard, copy the API Environment variable
        - In the settings.py file create a new environment variable for CLOUDINARY_URL
        - Add the CLOUDINARY_URL variable to Heroku
        - Add a temporary config var for DISABLE_COLLECTSTATIC
        - In settings.py add Cloudinary as an installed app
        - Add static and media file variables
        - Add templates directory
        - Change DIR's key to point to TEMPALTES_DIR
        - Add Heroku hostname to allowed hosts
        - Create directories for media, static and templates in the project workspace
        - Create a Procfile

- Deploy new empty project to Heroku
![initial_heroku_deployment](documentation_assets/images/initial_deployment_successful.png)

<a name="deployment"></a>

# 6. Deployment

[Go to the top](#table-of-contents)

I used the terminal to deploy my project locally. To do this I had to:
1. Create a repository on GitHub.
2. Clone the repository on your chosen source code editor (GitPod in my case) using the clone link.
3. Open the terminal within GitPod
4. Enter "python3 manage.py runserver into the terminal.
5. Go to local host address on my web browser.
6. All locally saved changes will show up here.

For the final deployment to Heroku, I had to:
1. Uncomment the PostgreSQL databse from my settings.py file.
2. Set debug = False in my settings.py file.
3. Commit and push all files to GitHub
3. In Heroku, remove the DISABLE_COLLECTSTATIC config var.
4. In the deploy tab, go to the manual deploy sections and click deploy branch.

I had an issue with the deployed site and the CSS was not showing on my screen.
This was rectified by restarting all dynos in Heroku.

<a name="end-product"></a>

# 7. End Product

[Go to the top](#table-of-contents)

Home Page:
![home_page_desktop_preview](documentation_assets/images/homepage_desktop_preview.png)

![home_page_mobile_preview](documentation_assets/images/homepage_mobile_preview.png)

Menu Page:
![menu_desktop_preview](documentation_assets/images/menu_desktop_preview.png)

![menu_mobile_preview](documentation_assets/images/menu_mobile_preview.png)

Contact Page:
![contact_desktop_preview](documentation_assets/images/contact_deskop_preview.png)

![contact_mobile_preview](documentation_assets/images/contact_mobile_preview.png)

Book Now Page:
![booking_desktop_preview](documentation_assets/images/booking_desktop_preview.png)

![booking_mobile_preview](documentation_assets/images/booking_mobile_preview.png)

Manage Booking Page:
![manage_booking_desktop_preview](documentation_assets/images/manage_booking_desktop_preview.png)

![manage_booking_mobile_preview](documentation_assets/images/manage_booking_mobile_preview.png)

Edit Booking Page:
![edit_booking_desktop_preview](documentation_assets/images/edit_booking_desktop_preview.png)

![edit_booking_mobile_preview](documentation_assets/images/edit_booking_mobile_preview.png)

Edit Profile Page:
![edit_profile_desktop_preview](documentation_assets/images/edit_profile_desktop_preview.png)

![edit_profile_mobile_preview](documentation_assets/images/edit_profile_mobile_preview.png)

Register Page:
![register_desktop_preview](documentation_assets/images/register_desktop_preview.png)

![register_mobile_preview](documentation_assets/images/register_mobile_preview.png)

Sign In Page:
![sign_in_desktop_preview](documentation_assets/images/sign_in_desktop_preview.png)

![sign_in_mobile_preview](documentation_assets/images/sign_in_mobile_preview.png)

Sign Out Page:
![sign_out_desktop_preview](documentation_assets/images/sign_out_desktop_preview.png)

![sign_out_mobile_preview](documentation_assets/images/sign_out_mobile_preview.png)

<a name="known-bugs"></a>

# 8. Known Bugs

[Go to the top](#table-of-contents)

- Some items in the navigation bar don't have a is active red background to show the user they are on the selected page.

- Some forms for this project is built by using the django-crispy-forms libraries therefore, some of the fields do not contain all the validation rules as I cannot target the individual inputs. For example on the edit profile form, I have add the validation rule so that the user can only enter a number, however I couldnt not figure out a way to add a min and max length value.

<a name="credits"></a>

# 9. Credits

[Go to the top](#table-of-contents)

### Code
-   The navigation bar came from [Bootstrap](https://getbootstrap.com/docs/5.0/components/navbar).

- The JavaScript code to set the online booking form to default to the current date came from [Stack Overflow](https://stackoverflow.com/questions/6982692/how-to-set-input-type-dates-default-value-to-today).

- The JavaScript code to disable any previous dates on the online booking form came from [Demo2s](https://www.demo2s.com/javascript/javascript-input-date-input-type-date-disable-dates-before-today.html).

### Content
-   The restaurant logo came from [Adobe Creative Cloud Express logo maker](https://www.adobe.com/express/create/logo).

-   The dragon image from the home page came from [PNGItem](https://www.pngitem.com/middle/wRmbRx_red-dragon-png-red-chinese-dragon-png-transparent/).

-   The banner image from the home page came from [PNGItem](https://pngtree.com/freebackground/chinese-food-pasta-simple-white-banner_1059420.html).

-   The Chinese food image on the menu page came from [Google Images](tinyurl.com/68hzut9u).

-   The Chinese food image on the menu page came from [Google Maps](https://www.maps.ie/create-google-map/).

### Project Acknowledgements
- Code Institue Tutor Support - For directing me to the correct solutions for any bugs.

- My Mentor - For his constructive criticism and always pushing me to go further to develop my skills.