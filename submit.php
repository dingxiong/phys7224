<?php

/**
 * @brief put user's submission into database
 *
 * param[in] conn         connection to the database
 * param[in] submitData   user's submission answer, should be _POST variable
 */
function submit($conn, $userAnswer, $submitTable){
    
    $current_time = date("Y-m-d h:i:s");
    $userAnswer['time'] = "'$current_time'";
    $userAnswer['hasGraded'] = 0 ;
    // print_r($userAnswer);
    
    // insert the new submit
    $columns = implode(", ", array_keys($userAnswer));
    $new_row  = implode(", ", array_values($userAnswer));
    $sql = "insert into $submitTable ($columns) values ($new_row)";
    // echo $sql, "<br>";
    if($conn->query($sql) == FALSE){
	echo "error:" . $sql . "<br>" . $conn->error;
    }
    
    echo "Your submission is successfully. ", "<br>";

}


/**
 * @brief extract user's submission.
 *
 * @param[in] sumbitData    should be _POST
 */
function extractSubmit($submitData){
    // prepare the answer array
    $answer = array();
    foreach($submitData as $key => $value){
	$value = test_input($submitData[$key]); // for security reason
	if($key != "submit"){
	    if($key == "email") // email need to be stored in string 
		$answer[$key] =  "'$value'";
	    else 
		$answer[$key] = $value;
	}
    }
    return $answer;
}

/**
 * @brief trim the data form submission for security consideration
 *
 * @param[in] data      data collected from html form
 */
function test_input($data){
    $data = htmlspecialchars(stripslashes(trim($data)));
    return $data;
}

/**
 * @brief extract answer and email from user's submission.
 *
 * @param[in] sumbitData    result of function extractSubmit
 */
function extractAnswerAndEamil($submitData){
    // print_r( $submitData);
    $result = array();
    foreach($submitData as $key => $value){
	if(preg_match("/^q[0-9]+$/" , $key) or $key == 'email'){
	    $result[$key] = $value;
	}
    }
    // print_r( $result);
    return $result;
}



function findTableNames($hwNo){
    switch ($hwNo){
    	case 'homework1':
	    return array("key" => "hw1_key", "submit" => "hw1_submit", "grades" => "hw1_grades");
	    
    	case 'homework2':
	    return array("key" => "hw2_key", "submit" => "hw2_submit", "grades" => "hw2_grades");
	    
    	case 'homework3':
	    return array("key" => "hw3_key", "submit" => "hw3_submit", "grades" => "hw3_grades");
	    
    	case 'homework4':
	    return array("key" => "hw4_key", "submit" => "hw4_submit", "grades" => "hw4_grades");
	    
    	case 'homework5':
	    return array("key" => "hw5_key", "submit" => "hw5_submit", "grades" => "hw5_grades");
	    
    	case 'homework6':
	    return array("key" => "hw6_key", "submit" => "hw6_submit", "grades" => "hw6_grades");
	    
    	case 'homework7':
	    return array("key" => "hw7_key", "submit" => "hw7_submit", "grades" => "hw7_grades");
	    
    	case 'homework8':
	    return array("key" => "hw8_key", "submit" => "hw8_submit", "grades" => "hw8_grades");
	    
    	case 'homework9':
	    return array("key" => "hw9_key", "submit" => "hw9_submit", "grades" => "hw9_grades");
	    
    	case 'homework10':
	    return array("key" => "hw10_key", "submit" => "hw10_submit", "grades" => "hw10_grades");
	    
    	case 'homework11':
	    return array("key" => "hw11_key", "submit" => "hw11_submit", "grades" => "hw11_grades");
	    
    	case 'homework12':
	    return array("key" => "hw12_key", "submit" => "hw12_submit", "grades" => "hw12_grades");
	    
    	case 'homework13':
	    return array("key" => "hw13_key", "submit" => "hw13_submit", "grades" => "hw13_grades");
	    
    	case 'homework14':
	    return array("key" => "hw14_key", "submit" => "hw14_submit", "grades" => "hw14_grades");
	    
    	case 'homework15':
	    return array("key" => "hw15_key", "submit" => "hw15_submit", "grades" => "hw15_grades");

    	case 'homework16':
	    return array("key" => "hw16_key", "submit" => "hw16_submit", "grades" => "hw16_grades");
	    
	default:
	    echo " <br> homeworkd identityfier is wrong ! <br>";
	    break;
    }
}

?> 

