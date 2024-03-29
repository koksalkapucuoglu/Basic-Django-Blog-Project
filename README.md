## Basic-Django-Blog
Basic Django blog is a beginner friendly blog application. 

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Installing
```
open terminal and type
git clone https://github.com/koksalkapucuoglu/Basic-Django-Blog-Project.git
```

#### or simply download using the url below
```
https://github.com/koksalkapucuoglu/Basic-Django-Blog-Project.git
```

## Requirements
```
Create a virtual environment and active it
and install requirements type:

pip install -r requirements.txt
```

### In this project i have used sqlite as a database, change db information in settings with your database information
## To migrate the database open terminal in project directory and type
```
python manage.py makemigrations
python manage.py migrate
```

## Static files collection
```
python manage.py collectstatic
```

## Creating Superuser
```
python manage.py createsuperuser
```


## To run the program in local server use the following command
```
python manage.py runserver
Then go to http://127.0.0.1:8000 in your browser
```

## Project Screenshots


### Home Page
![Home](https://github.com/koksalkapucuoglu/Basic-Django-Blog-Project/blob/master/basic_django_blog_ss/django_index.PNG)

### Login Page
![Login](https://github.com/koksalkapucuoglu/Basic-Django-Blog-Project/blob/master/basic_django_blog_ss/login%20fomr.PNG)

### Archieve Page
![Archieve](https://github.com/koksalkapucuoglu/Basic-Django-Blog-Project/blob/master/basic_django_blog_ss/archieve.PNG)

### Dashboard page
![Dashboard](https://github.com/koksalkapucuoglu/Basic-Django-Blog-Project/blob/master/basic_django_blog_ss/dashboard.PNG)

### Update Article page
![Update Articlet](https://github.com/koksalkapucuoglu/Basic-Django-Blog-Project/blob/master/basic_django_blog_ss/update.PNG)

### Search Article page
![ Search Article](https://github.com/koksalkapucuoglu/Basic-Django-Blog-Project/blob/master/basic_django_blog_ss/search.PNG)
