<!DOCTYPE html>
<html>
    <body>
	
	<?php
	
	require_once('submit.php');
	require_once('formulateMail.php');
	require_once('grade.php');

	if ($_SERVER["REQUEST_METHOD"] == "POST") {
	    
	    $servername = "localhost";
	    $username = "root";
	    $password = "";
	    $dbname = "phys7224";
	    
	    
	    $hwNo = "hw16";
	    $tsubmit = "hw16_submit";
	    $tkey = "hw16_key";
	    $tgrade = "hw16_grades";
	    
	    // connect to MySQL server
	    $conn = mysqli_connect($servername, $username, $password, $dbname);
	    if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	    }
	    // echo "Connected successfully";
	    
	    ////////////////////////////////////////////////////////////
	    //                 submit part                            //
	    ////////////////////////////////////////////////////////////
	    
	    submit($conn, $_POST);
	    
	    ////////////////////////////////////////////////////////////
	    //                 grade part                            //
	    ////////////////////////////////////////////////////////////
	    $sql = " select * from $tsubmit where hasGraded=0 ";    
	    $ungraded = $conn->query($sql);
	    if($ungraded->num_rows > 0){
		while($row = $ungraded->fetch_assoc()){
		    // calculate grades and store it in an array
		    $points = array();
		    foreach($row as $key => $value){
			if($key != 'time' and $key != 'email' and $key != 'hasGraded'){
			    $points[$key] = grade_one_entry($conn, $tkey, $key, $value);
			}
		    }
		    $total = array_sum($points);
		    $result = $conn->query("SELECT SUM(points) AS value_sum FROM $tkey"); 
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
		    $sql = "update $tsubmit set hasGraded=1 where email='"
			.$row['email']."' and time='".$row['time']."'";
		    // echo $sql;
		    $conn->query($sql);
		    
		    // mail the grade
		    mail_grade($conn, $hwNo, $row['email'], $new_entry, $tkey);
		    
		}
	    }        
	    echo "successfully graded. ", "<br>";

	    ////////////////////////////////////////////////////////////
	    $conn->close();             // close the connection

	    
	    
	}

	function extractSubmit($submitData){
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

	
	function mail_grade($conn, $hwNo, $email, $grade, $tkey){
	    $to = $email;
	    $subject = "Nonliear Dynamics Online Course : Your grade for $hwNo";
	    $txt = " Your grade: \r\n\r\n";
	    foreach($grade as $key => $value){
		$txt .= "$key"." : "."$value \r\n";
	    }
	    
	    $txt .= "\r\n ======================================= \r\n";
	    $txt .= "\r\n Assigned points for each problem : \r\n\r\n";
	    
	    $tmp = $conn->query("select question, points from $tkey");
	    while ($answer = $tmp->fetch_assoc()){
		foreach($answer as $key => $value){
		    $txt .= "$key" . " : " . "$value \r\n";
		}
	    }
	    
	    mail($to, $subject, $txt);          
	}
	
	?>
	
    </body>
</html>
