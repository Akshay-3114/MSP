# Music-Sharing-Portal

A music sharing portal where users can signup, login using their emails and upload music based on their preferred level of visibility of the uploaded content.

# List of Feature

- Home page: Describes website and link to login page </br>

- Register User: Sign up for new user account </br>

- Login User: Sign in with existing user account </br>

- Dashboard: It has 4 different types of albums </br>

	     1.) Private / Uniquely yours albums [including private & public both]  
	     2.) Received Albums
		- Albums which are shared by another users to you only will fall into this category
	     3.) Friends Albums
		- It contains Public Albums of users whom you follow
	     4.) Browse All
		- It contains all the public albums of all available users on the site 
	

	         Create new Albums and uploads song 
             View/Edit/Delete own albums 
             View albums shared by other users 
             View Friends' albums 
             View public albums of all users 
             Share/Unshare own albums 
             Search any albums with album title, artist, genre

- listen/search all songs with their album names </br>

- Follow/Unfollow Users </br>

- View my profile and analytics :- It is named as [user's] activity on my profile page. </br>
				   It shows the classification of your albums into 4 diff category and number of songs available in album.</br>
   
- Edit my profile </br>

- View profile of my followers</br>

- Custom error handler pages inside templates folder [it will be available to use when release mode is on]</br>

- Logout</br>

# How to run ?
	1.) Go to Music_Sharing_Site2 folder
	2.) Create new virtual env by running 'python -m venv env' or use existing venv inside project. [virtual env is recommended]
	3.) Come back to previous directory ,open terminal there and run 'pip install -r /requirements.txt' . It will install all the required packages.
	4.) apply migrations and finally python manage.py runserver

