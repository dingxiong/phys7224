<?php

/**
 * @brief put user's submission into database
 *
 * param[in] conn         connection to the database
 * param[in] submitData   user's submission answer, should be _POST variable
 */
function submit($conn, $submitData){
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
    $current_time = date("Y-m-d h:i:s");
    $answer['time'] = "'$current_time'";
    $answer['hasGraded'] = 0 ;
    // print_r($answer);
    
    // insert the new submit
    $columns = implode(", ", array_keys($answer));
    $new_row  = implode(", ", array_values($answer));
    $sql = "insert into $tsubmit ($columns) values ($new_row)";
    // echo $sql, "<br>";
    if($conn->query($sql) == FALSE){
	echo "error:" . $sql . "<br>" . $conn->error;
    }
    
    echo "Your submission is successfully. ", "<br>";

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

?> 

