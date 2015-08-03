# phys7224 online course grader
grade system for nonlinear dynamics course. 
Since this is a public repository. I only include a 
sample homework page, and the database of all answers
is not uploaded.

Basically, html forms are used to collect user submission. Each question has a
label : q1, q1, q3, ect. And there is `email` label used for email and a 
hidden input `hwNo` used to identify the homework number. Once user hits
`submit` button, file `grade/action.php` is triggered. User's submission
is inserted to table `hw*_sumbit`. Correct answer from table `hw*_key` is loaded to
grade ungraded submissions. The graded result is inserted to table `hw*_grades` and
emailed to user.

## steps
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
* write the initialization file to fill out all the answer tables
* run `python manage.py collectstatic` to collect all static files to the static_root folder
* create superuser 
  ```
  python manage.py createsuperuser
  ```
* change the perssion of database files and related folders 
  ```
  sudo chown www-data:www-data hws
  sudo chown www-data:www-data db.sqlite3
  ```
  
## how to change the email style ?
Email format is encoded in file `formulateMail.php`. It is a mix of html and
php. You can easily find the part that controls the style of email. Change it,
Email content will change for next submission.

## remaining problems
* Background image cannot be used in email html. Even you use it, email 
server will automatically filter it.

* PHPMailer seems not able to change the aspect ratio of inline images.

## Components

### MySQL to store submissions, grades and keys
Each homework has 3 tables: `hw*_submit`, `hw*_key` and `hw*_grades`, storing users' submission, 
correct answers, grades respectively. File `writeKeys.php` is used to initialize all these tables.

### PHPMailer

PHPMailer is a very popular 3rd part library for PHP to 
send emails. Here it is used to simplify our work.
We use `composer` to install PHPMailer. Install `composer` :
```
$ cd grader
$ curl -sS https://getcomposer.org/installer | php
```
In grader folder, you will find file `composer.phar`. Then create 
a file `composer.json` in folder `grader`, and put the following
into it:
```
{
	"require" : {
		"phpmailer/phpmailer": "~5.2"
	}
}
```

In folder `grader`, open a terminal and type 
```
php composer.phar install
```
PHPMailer now is installed in `vendor` folder

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

### Javascript to valid answer
Three functions are used to validate users' submission before injecting it into database
```
    <script type="text/javascript">
      
      function validateDecimal(input, qnum) {
	  var number = /^[-+]?[0-9]+\.[0-9]+$/;
	  if(input.value.match(number) ){
	      return true;
	  } else {
	      alert('please input a decimal number for question  ' + qnum);
	      return false;
	  }
      }

      function validateInt(input, qnum){
	  var number = /^[-+]?[0-9]+$/;  
	  if(input.value.match(number) ){
	      return true;
	  } else {
	       alert('please input a integer number for question  ' + qnum );
	      return false;
	  }
      }
      
      
      function validateEmail(input) {
	  var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
	  if ( re.test(input.value)){  
	      return true;  
	  } else {
	      alert("You have entered an invalid email address!");
	      return false;
	  }
      }  
      
      function validateSubmit(){
	  var q1 = validateDecimal(document.homework_form.q1, "q1");
	  var q2 = validateDecimal(document.homework_form.q2, "q2");
	  var q3 = validateDecimal(document.homework_form.q3, "q3");
	  var email = validateEmail(document.homework_form.email);

	  return q1 && q2 && q3 && email;
      }

    </script>
```
Change `validateSubmit` function accordingly for each homework.

