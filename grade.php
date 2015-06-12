<?php

/**
 * @brief grade the submission
 *
 * @param[in] conn            connection to the database
 * @param[in] submitTable     homework submission table
 */

function grade($conn, $submitTable){
    $sql = " select * from $submitTable where hasGraded=0 ";    
    $ungraded = $conn->query($sql);
    if($ungraded->num_rows > 0){
	while($row = $ungraded->fetch_assoc()){
	    // calculate grades and store it in an array
	    $points = array();
	    foreach($row as $key => $value){
		if($key != 'time' and $key != 'email' and $key != 'hasGraded'){
		    $points[$key] = gradeOneEntry($conn, $keyTable, $key, $value);
		}
	    }
	    $total = array_sum($points);
	    $result = $conn->query("SELECT SUM(points) AS value_sum FROM $keyTable"); 
	    $maxim = $result->fetch_assoc(); 
	    $sum = $maxim['value_sum'];
	    //print_r($points);
	    
	    // write the grade
	    // create the student entry for this student
	    $tmp = array('email' => "'".$row['email']."'", 
		'time' => "'".$row['time']."'",
		'points' => $total,
		'percent' => $total/$sum );
	    $new_entry = array_merge($tmp, $points);
	    $columns = implode(", ", array_keys($new_entry));
	    $new_row = implode(", ", array_values($new_entry));
	    $sql = "insert into $tgrade ($columns) values ($new_row)";
	    if($conn->query($sql) == FALSE){
		echo "error:" . $sql . "<br>" . $conn->error;
	    }
	    
	    // change the hasGraded status
	    $sql = "update $submitTable set hasGraded=1 where email='"
		.$row['email']."' and time='".$row['time']."'";
	    // echo $sql;
	    $conn->query($sql);
	    
	    // mail the grade
	    mail_grade($conn, $hwNo, $row['email'], $new_entry, $keyTable);
	    
	}
    }        
    echo "successfully graded. ", "<br>";
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
    $sql = "select * from $keyTable where question = '".$key."' limit 1";
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



?>
