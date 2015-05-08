<!DOCTYPE html>
<html>
<body>
 
<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "phys7224";
$tsubmit = "hw16_submit";
$tkey = "hw16_key";
$tgrade = "hw16_grades";
    
// connect to the mySQL database
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
// echo "Connected successfully";

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
        //print_r($points);

        // write the grade
        $sql = "select * from $tgrade where email='".$row['email']."'";
        echo $sql, "<br>";
        $student = $conn->query($sql);
        if($student->num_rows == 0){
            // create the student entry for this student
            $tmp = array('email' => "'".$row['email']."'", 
                         'num_submit' => 1, 'points' => $total);
            $new_entry = array_merge($tmp, $points);
            $columns = implode(", ", array_keys($new_entry));
            $new_row = implode(", ", array_values($new_entry));
            $sql = "insert into $tgrade ($columns) values ($new_row)";
            if($conn->query($sql) == FALSE){
                echo "error:" . $sql . "<br>" . $conn->error;
            }
        }
        elseif($student->num_rows == 1){
            // just update his/her grade
            $sql = "update $tgrade set points=$total where email=$row[email] ";
            $conn->query($sql);
            foreach($points as $key => $value){
                $sql = "update $tgrade set $key=$value where email=$row[email] "; 
                $conn->query($sql);
            }
        }
        else {
            // find more than one => error
            echo "Error: two identical emails are found in the grade table.", "<br>";
        }  
        
    }
}

	
$conn->close();

// tkey : the key table
// key  : the problem is about to grade
// value : student's answer
// Note: the answer should be set up first.
function grade_one_entry($conn, $tkey, $key, $value){
    // only return the first answer
    $sql = "select * from $tkey where question = '".$key."' limit 1";
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



</body>
</html>
