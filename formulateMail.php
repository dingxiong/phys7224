<?php

function getCourseInfo($courseNo){
    switch($courseNo){
	case 1:
	    return array("name" => "Nonlinear Dynamics 1: Geometry of Chaos",
		"link" => "http://chaosbook.org/course1/Syllabus.html"
	    );

	case 2:
	    return array("name" => "Nonlinear dynamics 2: Chaos rules",
		"link" => "http://chaosbook.org/course1/index2.html"
	    );
    }
}

function getWeekInfo($weekNo){
    switch($weekNo){
	case 1:
	    return array("name" => "week 1", "link" => "http://www.chaosbook.org/course1/Course1w1.html");
	    
	case 2:
	    return array("name" => "week 2", "link" => "http://www.chaosbook.org/course1/Course1w2.html");

	case 3:
	    return array("name" => "week 3", "link" => "http://www.chaosbook.org/course1/Course1w3.html");
	    
	case 4:
	    return array("name" => "week 4", "link" => "http://www.chaosbook.org/course1/Course1w4.html");

	case 5:
	    return array("name" => "week 5", "link" => "http://www.chaosbook.org/course1/Course1w5.html");
	    
	case 6:
	    return array("name" => "week 6", "link" => "http://www.chaosbook.org/course1/Course1w6.html");

	case 7:
	    return array("name" => "week 7", "link" => "http://www.chaosbook.org/course1/Course1w7.html");
	    
	case 8:
	    return array("name" => "week 8", "link" => "http://www.chaosbook.org/course1/Course1w8.html");
	    
	case 9:
	    return array("name" => "week 9", "link" => "http://www.chaosbook.org/course1/Course2w9.html");
	    
	case 10:
	    return array("name" => "week 10", "link" => "http://www.chaosbook.org/course1/Course2w10.html");
	    
	case 11:
	    return array("name" => "week 11", "link" => "http://www.chaosbook.org/course1/Course2w11.html");
	    
	case 12:
	    return array("name" => "week 12", "link" => "http://www.chaosbook.org/course1/Course2w12.html");
	    
	case 13:
	    return array("name" => "week 13", "link" => "http://www.chaosbook.org/course1/Course2w13.html");

	case 14:
	    return array("name" => "week 13", "link" => "http://www.chaosbook.org/course1/Course2w14.html");

	case 15:
	    return array("name" => "week 13", "link" => "http://www.chaosbook.org/course1/Course2w15.html");

	case 16:
	    return array("name" => "week 13", "link" => "http://www.chaosbook.org/course1/Course2w16.html");

	default:
	    echo "<br> The week No. is wrong ! <br>";
	    break;
    }

}


function getHomeworkInfo($hwNo){
    switch($hwNo){
	case 1:
	    return array("name" => "homework 1", "link" => "http://www.chaosbook.org/course1/homework1.html");
	    
	case 2:
	    return array("name" => "homework 2", "link" => "http://www.chaosbook.org/course1/homework2.html");

	case 3:
	    return array("name" => "homework 3", "link" => "http://www.chaosbook.org/course1/homework3.html");
	    
	case 4:
	    return array("name" => "homework 4", "link" => "http://www.chaosbook.org/course1/homework4.html");

	case 5:
	    return array("name" => "homework 5", "link" => "http://www.chaosbook.org/course1/homework5.html");
	    
	case 6:
	    return array("name" => "homework 6", "link" => "http://www.chaosbook.org/course1/homework6.html");

	case 7:
	    return array("name" => "homework 7", "link" => "http://www.chaosbook.org/course1/homework7.html");
	    
	case 8:
	    return array("name" => "homework 8", "link" => "http://www.chaosbook.org/course1/homework8.html");
	    
	case 9:
	    return array("name" => "homework 9", "link" => "http://www.chaosbook.org/course1/homework9.html");
	    
	case 10:
	    return array("name" => "homework 10", "link" => "http://www.chaosbook.org/course1/homework10.html");
	    
	case 11:
	    return array("name" => "homework 11", "link" => "http://www.chaosbook.org/course1/homework11.html");
	    
	case 12:
	    return array("name" => "homework 12", "link" => "http://www.chaosbook.org/course1/homework12.html");
	    
	case 13:
	    return array("name" => "homework 13", "link" => "http://www.chaosbook.org/course1/homework13.html");

	case 14:
	    return array("name" => "homework 13", "link" => "http://www.chaosbook.org/course1/homework14.html");

	case 15:
	    return array("name" => "homework 13", "link" => "http://www.chaosbook.org/course1/homework15.html");

	case 16:
	    return array("name" => "homework 13", "link" => "http://www.chaosbook.org/course1/homework16.html");

	default:
	    echo "<br> The homework No. is wrong ! <br>";
	    break;

    }
}

// function used use to formulate the body of the email
function formualteMailContent($courseNo, $weekNo, $hwNo){
    $courseInfo = getCourseInfo($courseNo);
    $weekInfo = getWeekInfo($weekNo);
    $homeworkInfo = getHomeworkInfo($hwNo);
    
    $message = '
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <title>Nonlinear Dynamics 1: Geometry of Chaos - homework 1 grades</title>
    <style>

    div.head {
        height:15%;
        border:5px;
        color: #0CF;
        background: rgba(200, 200, 200, 0.6);
        text-align:left;
        margin-left: 10px;
    }  
    span.tab{
        padding: 0 10%; /* Or desired space*/
    }

    span.vtab{
        padding: 10% 0; /* Or desired space*/
    }

    span.link{
        font-family:"Lucida Console";
    }

    span.center{
        text-align:center;
    }   

    table { 
        background: rgba(255, 255, 255, 0.6);
    }
    .gradeFont {
        font-size: 24px;
        font-weight: bold;
        text-decoration: none;
    }
    .hwLink {
        font-size: 24px;
        font-weight: bold;
        text-decoration: underline;
    }
    </style>
    </head>
    
    <body style="font-family: Arial, Helvetica, sans-serif; width: 700px;" background="ChaosGrade_files/cloud_bg.jpg">
    <div align="right"><small>This email contains your grade for homework ${hwNo}. Do not reply to this email. </small></div>

    <img src="ChaosGrade_files/ChaosBookLogo.jpg" style="width:700px;height:200px;">
    <div class="head">

    <h1><a href="$courseInfo["link"]" class="head"> $courseInfo["name"] </a></h1>
    <span class="vtab"></span>
    <span class="link">
    <a href="http://www.chaosbook.org/course1/Course1w1.html" class="hwLink">week 1</a>
    <span class="tab"></span>
    <a href="http://www.chaosbook.org/course1/homework1.html" class="hwLink">homework 1</a>
    </span>
    </div>
    <!--End-->

         <table align="left" style="border:1px solid black"><tbody><tr><td>Your grade: 
    <div class="gradeFont"><b>12 / 16 (75.00%) </b></div></td></tr></tbody></table>

    <p>
    <br>
    <!--<a href = "http://www.prism.gatech.edu/~kshah84/table.html"> Link</a>-->
  
  
                </p>
    <h4>&nbsp;</h4>
    <h4>Summary of your submissions:</h4>
    <table style="border:1px solid black" align="left">
    <tbody><tr>
    <td>Your e-mail</td>
    <td>predrag@gatech.edu</td>
    </tr>

    <tr>
    <td>Submission time</td>
    <td>Wed Dec 31 2014 06:20:34 GMT-0800 (PST) </td>
    </tr>
    </tbody></table> 
    <p>&nbsp;</p>
    <p><br>
                  
    </p>
    <table style="width:700">
    <tbody><tr>
    <td width="578"></td>
    <td width="58" align="center"><b>point(s)</b></td><td width="48"></td>
    </tr>
    </tbody></table>

    <table style="width:700">
    <tbody>
    <tr style="border:1px solid #33CC33">
    <td>
    <table>
    <tbody><tr>
    <td><b>Equilibria of the Roessler flow <br>(ChaosBook.org version14.5.7, exercise 2.8 a)</b></td>
    </tr>
    <tr>
    <td>Your Answer: <b>  2 </b></td>
    </tr>
                       
    </tbody></table>
    </td>
    <td width="57" align="center" class="gradeFont"> 1 </td>
    <td width="47" bgcolor="#66FF33" align="center" style="border:1px solid #33CC33"><img src="ChaosGrade_files/right.jpg" style="width:47px;height:47px;"></td>
    </tr></tbody></table>
    <table style="width:700">
    <tbody><tr>
    <td>
    <table style="background: rgba(255, 255, 255, 0);">
    <tbody><tr>
    <td><b>Equilibria of the Roessler flow <br>(ChaosBook.org version14.5.7, exercise 2.8 b)</b></td>
    </tr>
    <tr>
    <td>Your Answer: <b> 0.007 -0.0351 0.0351  </b></td>
    </tr></tbody></table>
    </td>
    <td width="57" align="center" class="gradeFont">  3 </td>
    <td width="47" bgcolor="#66FF33" align="center" style="border:1px solid #33CC33"><img src="ChaosGrade_files/right.jpg" style="width:47px;height:47px;"></td>
    </tr>
    </tbody></table>
	<table style="width:700">
    <tbody><tr>
    <td>
    <table style="background: rgba(255, 255, 255, 0);">
    <tbody><tr>
    <td><b>Runge-Kutta integration</b></td>
    </tr>
    <tr>
    <td>Your Answer: <b>  -0.84 </b></td>
    </tr></tbody></table>
    </td>
    <td width="57" align="center" class="gradeFont">  3 </td>
    <td width="47" bgcolor="#66FF33" align="center" style="border:1px solid #33CC33">
    <img src="ChaosGrade_files/right.jpg" style="width:47px;height:47px;"></td>
    </tr>
    </tbody></table><table style="width:700">
                                <tbody><tr>
    <td>
    <table style="background: rgba(255, 255, 255, 0);">
    <tbody><tr>
    <td><b>Integrating Roessler system</b> </td>
    </tr>
    <tr>
    <td>Your Answer: <b>0.007 -0.0351 0.0351  </b></td>
    </tr>
    </tbody></table>
    </td>
    <td width="57" align="center" class="gradeFont"> 0 </td>
    <td width="47" bgcolor="#FF3333" align="center" style="border:1px solid #33CC33">
    <img src="ChaosGrade_files/wrong.jpg" style="width:47px;height:47px;"></td>
    </tr>
    </tbody></table>
    <table style="width:700">
    <tbody><tr>
    <td>
    <table style="background: rgba(255, 255, 255, 0);">
    <tbody><tr>
    <td><b>Poincare sections and return maps of the Reissler system:</b></td>
    </tr>
    <tr>
    <td>Your Answer: <b>  8.38 </b></td>
    </tr></tbody></table>
    </td>
    <td width="57" align="center" class="gradeFont">  1 </td>
    <td width="47" bgcolor="#66FF33" align="center" style="border:1px solid #33CC33"><img src="ChaosGrade_files/right.jpg" style="width:47px;height:47px;"></td>
    </tr>
    </tbody></table>
    

    </body>
    </html>
';
    return $message;
}


?>
