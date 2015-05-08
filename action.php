<!DOCTYPE html>
<html>
<body>
 
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "phys7224";
    $tname = "hw16_submit";
    
    // prepare the answer array
    $answer = array();
    foreach($_POST as $key => $value){
        $value = test_input($_POST[$key]); // for security reason
        if($key != "submit"){
            if($key == "email")
                $answer[$key] =  "'$value'";
            else 
                $answer[$key] = $value;
        }
    }
    $current_time = date("Y-m-d h:i:s");
    $answer['time'] = "'$current_time'";
    $answer['hasGraded'] = 0 ;
    // print_r($answer);

    // connect to MySQL server
    $conn = mysqli_connect($servername, $username, $password, $dbname);
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }
    // echo "Connected successfully";

    // insert the new submit
    $columns = implode(", ", array_keys($answer));
    $new_row  = implode(", ", array_values($answer));
    $sql = "insert into $tname ($columns) values ($new_row)";
    // echo $sql, "<br>";
    if($conn->query($sql) == FALSE){
        echo "error:" . $sql . "<br>" . $conn->error;
    }
    
    echo "Your submission is successfully. ", "<br>";

    $conn->close();             // close the connection
    
}

function test_input($data){
    $data = htmlspecialchars(stripslashes(trim($data)));
    return $data;
}
?>



</body>
</html>
