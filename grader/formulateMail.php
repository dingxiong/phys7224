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
	    return array("name" => "week 14", "link" => "http://www.chaosbook.org/course1/Course2w14.html");

	case 15:
	    return array("name" => "week 15", "link" => "http://www.chaosbook.org/course1/Course2w15.html");

	case 16:
	    return array("name" => "week 16", "link" => "http://www.chaosbook.org/course1/Course2w16.html");

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
	    return array("name" => "homework 14", "link" => "http://www.chaosbook.org/course1/homework14.html");

	case 15:
	    return array("name" => "homework 15", "link" => "http://www.chaosbook.org/course1/homework15.html");

	case 16:
	    return array("name" => "homework 16", "link" => "http://www.chaosbook.org/course1/homework16.html");

	default:
	    echo "<br> The homework No. is wrong ! <br>";
	    break;

    }
}

function formulateGradeTable($conn, $grade, $keyTable, $userAnswerAndEmail){
    $list = '';
    $tmp = $conn->query("select id, title, points from $keyTable ");
    while($answer = $tmp->fetch_assoc()){
	$id = $answer['id'];
	$title = $answer['title'];
	$points= $grade[$id];
	if($points == $answer['points']){
	    $color = '#06ac06';
	} else {
	    $color = '#FF3333';
	}

	$item = <<<EOD
<div style="color: black; background-color: {$color} ; border-radius: 15px; margin-bottom: 1cm; width: 700px; overflow:hidden;">
<div style="padding: 15px; width: 60%; float:left">
<p><b style="font-size:20px"> {$title} </b></p>
<p> Your answer: {$userAnswerAndEmail[$id]} </p>
</div>
<div style="padding: 15px; width: 20%; float:right">
<p><b> {$points} out of {$answer['points']} point(s) </b></p>
</div>
</div>
EOD;
	$list .= $item;
	echo $item;
    }
    
    return $list;

}

// function used use to formulate the body of the email
function formualteMailContent($conn, $courseNo, $weekNo, $hwNo, 
    $grade, $keyTable, $userAnswerAndEmail){
    
    $gradeBlock = formulateGradeTable($conn, $grade, $keyTable, $userAnswerAndEmail);
    $courseInfo = getCourseInfo($courseNo);
    $weekInfo = getWeekInfo($weekNo);
    $homeworkInfo = getHomeworkInfo($hwNo);
    
    $percent = percentFormat($grade['percent']);
    
    /* Important: EOD is the marker of start and end of this message. 
     * There should be no blanck space before the end marker */
    $message = <<<EOD
<html>
<head>
</head>
    
<body style="font-family: Arial, Helvetica, sans-serif; width: 700px;" background="cid:cloud">
<div align="right"><small>This email contains your grade for homework ${hwNo}. Do not reply to this email. </small></div>

<img src="cid:logo" style="width:700px;height:50px">
<div>

<h1 style="text-align: center">
<a href="{$courseInfo['link']}" > {$courseInfo['name']} </a>
</h1>

<h2 style="text-align: center">
<a href="{$weekInfo['link']}"> {$weekInfo['name']}</a>
<span style="padding: 0 50px 0 0;"></span>
<a href="{$homeworkInfo['link']}" > {$homeworkInfo['name']}</a>
</h2>
</div>

<h1>Your grade: {$grade['sum']} / {$grade['max']} ( {$percent} ) </h1> 

<h4>Summary of your submissions:</h4>
<div  style="color: black;  margin-bottom: 10px; width: 500px; overflow:hidden;">
<div style="width:60%; float:left">
<p>Your e-mail</p>
<p>Submission time</p>
</div>
<div style="width:30%; float=right">
<p>{$grade['email']}</p>
<p>{$grade['time']} </p>
</div>
</div>

$gradeBlock

</body>
</html>
EOD;
    return $message;

}

function percentFormat($x){
    $y = round($x * 100);
    return (string)$y . '%';
}

?>
