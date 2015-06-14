# phys7224
grade system for nonlinear dynamics course. 
Since this is a public repository. I only include a 
sample homework page, and the database of all answers
is not uploaded.

## prerequite

### PHPMailer

PHPMailer is a very popular 3rd part library for PHP to 
send emails. Here it is used to simplify our work.
We use *composer* to install PHPMailer. Install *composer* :
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

In the command line, type 
```
php composer.phar install
```