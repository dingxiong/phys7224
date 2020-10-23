# !!WARNING!!
This repo is outdated. The latest code is hosted in Heroku.
Please log into Heroku to checkout the repo.

Heroku  
username: phys7224@gmail.com 
password: ask Prof. Predrag


# phys7224 online course grader system
This grader is written under `python-django` platform.

Basically, homework htmls are saved as django templates and grader is only a function
in the view class. Also we use the default `sqlite` database.

We put the course folder under Prof. Predrag's home folder.
In this way,
we obtain maximal flexibility and simplicity such that my adviser can
modify the web page content and access database. 

# prerequisite 
In order to deploy `django` in `Apache`, we need to do two things:

1. install python package `django`, `virtualenv`.  

   `pip install django virtualenv`
2. install `mod-swgi` Apache module. In Ubuntu, `sudo apt-get install libapache2-mod-wsgi`

3. modify the Apache configuration file to indicate the right path to the homework
   folder and grand write permission to user group `www-data` to that folder.
   In Ubuntu, this file lives under /etc/apache2/sites-available/.
   File `000-default.conf` in this repository shows a sample Apache configuration.

**Note :**

1. During the setup, we need to restart Apache server a few times.

2. We will create a virtual python environment to serve the web pages, or worst, install a local
   version of python if the default version is not advanced enough.

# safety problem
I am not familiar with this problem. But, as you can see from the sample
`000-defult.conf` file, we are trying to grand permission to a folder under
a user's home folder ( probably Prof. Predrag's home folder).

I am not sure whether this will cause vulnerability of system files.

## the steps I followed to set it up in my laptop (just to record the steps).
```
$ sudo apt-get install apache2 libapache2-mod-wsgi
$ mkdir hws && cd hws
$ virtual venv && source venv/bin/activate
$ pip install django
$ django-admin.py startproject hws && python manage.py startapp grader
$ 
```
* add grader into INSTALLED_APPS in hws/settings.py
* add grader.urls into hws/urls.py and change the corresponding urls pattern in grader/urls.py
* create a folder htmls under top directory and add its path to TEMPLATES in hws/settings.py.
* create a folder static under top directory to serve figs and css files. Remember to add the path to STATICFILES_DIRS in hws/settings.py.
* create models and corresponding forms

  **Note:**
  1. specify float field as `null=True` and `blank=True`.
  2. specify char field as `blank=True`.
  3. each form field, except email, should be specified as `required=False`
* write the initialization file to fill out all the answer tables
* run `python manage.py collectstatic` to collect all static files to the static_root folder
* create superuser  
  ```
  python manage.py createsuperuser
  ```
* change the perssion of database files and related folders  
  ```
  sudo chown www-data hws 
  sudo chown www-data db.sqlite3
  sudo chmod 664 db.sqlite3
  ```

## steps to deploy it on Heroku
[Tutorial](https://devcenter.heroku.com/articles/getting-started-with-django)

### detatiled steps
1. create a Heroku account,  install Heroku toolbelt, python-virtualenv.
2. create django project and virtual environment.
3. install a few packages inside this virtual environment.
   ```
   pip install django-toolbelt, pillow, django-mathjax
   ```
4. edit `Procfile` and `requirement.txt`
5. change `setting.py` and `wsgi.py`
6. commit code and add remote heroku by `heroku create`. Then push code to heroku:
   `push heroku master`. (note must push to master branch)
7. migrate database. `heroku run python migrate syncdb`.

Last, change the `debug mode` to `False`

**Note:**

* mathjax js is not loaded in heroku but well behaved locally. I do not know why. Fortunately,
  `django-mathjax` works.

## how to change the email style ?

## remaining problems


## Components


### MathJax
In each homework html header, put
```
<!-- import mathjax.js -->
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
```
in order to use MathJax.



