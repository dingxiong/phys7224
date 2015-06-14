# phys7224
grade system for nonlinear dynamics course. 
Since this is a public repository. I only include a 
sample homework page, and the database of all answers
is not uploaded.

## Components

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

