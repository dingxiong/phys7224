<?php
require './vendor/phpmailer/phpmailer/PHPMailerAutoload.php';
require_once('formulateMail.php');

/**
 * @brief grade the submission
 *
 * @param[in] conn            connection to the database
 * @param[in] submitTable     homework submission table
 */

function grade($conn, $keyTable, $submitTable, $gradesTable, $userAnswerAndEmail){
    // find all ungraded entry
    $sql = " select * from $submitTable where hasGraded=0 ";    
    $ungraded = $conn->query($sql);
    if($ungraded->num_rows > 0){
	while($row = $ungraded->fetch_assoc()){
	    // calculate grades and store it in an array
	    $userAnswer = extractAnswer($row);
	    $points = gradeOneUser($conn, $keyTable, $userAnswer);
	    
	    $sum = array_sum($points);
	    $max = calMaxPoints($conn, $keyTable);
	    //print_r($points);
	    
	    // write the grade
	    $newGrade= writeGrade($conn, $gradesTable, $row['email'], 
		$row['time'], $sum, $max, $points);
	    
	    // change the hasGraded status
	    $sql = "update $submitTable set hasGraded=1 where 
			    email= '{$row['email']}' and time= '{$row['time']}' ";
	    // echo $sql;
	    $conn->query($sql);
	    
	    // mail the grade
	    mail_grade($conn, $newGrade, $keyTable,  $userAnswerAndEmail);
	    
	}
    }        
    echo "successfully graded. ", "<br>";
}


function extractAnswer($submitEntry){
    // print_r( $submitEntry);
    $result = array();
    foreach($submitEntry as $key => $value){
	if( preg_match("/^q[0-9]+$/" , $key) ){
	    $result[$key] = $value;
	}
    }
    // print_r( $result);
    return $result;
}

/**
 * @param[in] conn                 connection to the database
 * @param[in] keyTable             the key table
 * @param[in] key                  the problem is about to grade
 * @param[in] value                student's answer
 *
 * @note     the answer should be set up first
 */
function gradeOneEntry($conn, $keyTable, $key, $value){
    // only return the first answer
    $sql = "select * from $keyTable where id =  '$key' limit 1";
    $result = $conn->query($sql);
    if($result->num_rows == 1){
	$answer = $result->fetch_assoc();
	if($value >= $answer['left_value'] and $value <= $answer['right_value']){
	    return $answer['points'];                   
	} else {
	    return 0;
	}
    }
    
    // error case
    return 0;
}

function gradeOneUser($conn, $keyTable, $userAnswer){
    $points = array();
    foreach($userAnswer as $key => $value){
	$points[$key] = gradeOneEntry($conn, $keyTable, $key, $value);
    }
    return $points;
}

function calMaxPoints($conn, $keyTable){
    $result = $conn->query("SELECT SUM(points) AS value_sum FROM $keyTable"); 
    $maxim = $result->fetch_assoc(); 
    $sum = $maxim['value_sum'];

    return $sum;
}

function writeGrade($conn, $gradesTable, $email, $time, $sum, $max, $points){
    // create the grade entry for this student
    $tmp = array('email' => " '$email' ", 
	'time' => " '$time' ",
	'sum' => $sum,
	'max' => $max, 
	'percent' => $sum / $max );
    $new_entry = array_merge($tmp, $points);
    $cols = implode(", ", array_keys($new_entry));
    $newRow = implode(", ", array_values($new_entry));
    $sql = "insert into $gradesTable ($cols) values ($newRow)";
    if($conn->query($sql) == FALSE){
	echo "error:" . $sql . "<br>" . $conn->error;
    }

    return $new_entry;
}

function filterNum($str){
    $int = filter_var($str, FILTER_SANITIZE_NUMBER_INT);
    return $int;
}


/**
 * @param[in] grade   an array containing one grade entry
 */
function mail_grade($conn, $grade, $keyTable,  $userAnswerAndEmail){

    $hwNo = filterNum($keyTable);
    $message = formualteMailContent($conn, ($hwNo > 8) + 1, $hwNo, $hwNo, 
	$grade, $keyTable, $userAnswerAndEmail);
    $to = str_replace("'", "", $grade['email']);

    $mail = new PHPMailer;

    $mail->SMTPOptions = array(
	'ssl' => array(
            'verify_peer' => false,
		'verify_peer_name' => false,
		'allow_self_signed' => true
	)
    );

    // $mail->SMTPDebug = 2;
    $mail->isSMTP();                
    $mail->Host = 'smtp.gmail.com'; 
    $mail->Port = 587;
    $mail->SMTPSecure = 'tls'; 
    $mail->SMTPAuth = true;              
    $mail->Username = 'phys7224@gmail.com'; 
    $mail->Password = '!phys7224';            
    $mail->setFrom('phys7224@gmail.com', 'ChaosBook');
    $mail->addAddress( "$to" );
    $mail->addReplyTo('phys7224@gmail.com', 'ChaosBook');
    $mail->isHTML(true);                                  

    $mail->Subject = 'Nonliear Dynamics Online Course : Your grade';
    $mail->Body    = $message;
    //$mail->AddEmbeddedImage("./ChaosGrade_files/right.jpg", "right", "right.jpg");
    //$mail->AddEmbeddedImage("./ChaosGrade_files/wrong.jpg", "wrong", "wrong.jpg");
    $mail->AddEmbeddedImage("./ChaosGrade_files/cloud_bg.jpg", "cloud", "cloud_bg.jpg");
    $mail->AddEmbeddedImage("./ChaosGrade_files/ChaosBookLogo.jpg", "logo", "ChaosBookLogo.jpg");

    if(!$mail->send()) {
	echo 'Message could not be sent.';
	echo 'Mailer Error: ' . $mail->ErrorInfo;
    } else {
	echo 'Message has been sent <br>';
    }

}

?>
