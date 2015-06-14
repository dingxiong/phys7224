<?php 

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "key";

$conn = mysqli_connect($servername, $username, $password, $dbname);

createSubmitTable($conn, "hw16_submit", array('q1', 'q2', 'q3', 'q4'));
createGradeTable($conn, "hw16_grades", array('q1', 'q2', 'q3', 'q4'));

////////////////////////////////////////////////////////////
// create  hw15 answer key
$keyTable = "hw15_key";
createKeyTable($conn, $keyTable);

$key = formKey('q1', 'Q16.1    Invariant subspace in Kuramoto-Sivashinsky system', 
    0.42, 0.43, 2);
writeKey($conn, $keyTable, $key);

$key = formKey('q2', 'Q16.2    Period-doubling bifurcation', 
    36.32, 36.33, 4);
writeKey($conn, $keyTable, $key);

$key = formKey('q3', 'Q16.3    Equilibria in anti-symmetric spaceQ16.2', 
    0.03, 0.031, 3);
writeKey($conn, $keyTable, $key);

$key = formKey('q4', 'Q16.4    Return map and cycle expansion', 
    0, 0, 0);
writeKey($conn, $keyTable, $key);

////////////////////////////////////////////////////////////
// create  hw16 answer key
$keyTable = "hw16_key";
createKeyTable($conn, $keyTable);

$key = formKey('q1', 'Q16.1    Invariant subspace in Kuramoto-Sivashinsky system', 
    0.42, 0.43, 2);
writeKey($conn, $keyTable, $key);

$key = formKey('q2', 'Q16.2    Period-doubling bifurcation', 
    36.32, 36.33, 4);
writeKey($conn, $keyTable, $key);

$key = formKey('q3', 'Q16.3    Equilibria in anti-symmetric space', 
    0.03, 0.031, 3);
writeKey($conn, $keyTable, $key);

$key = formKey('q4', 'Q16.4    Return map and cycle expansion', 
    0, 0, 0);
writeKey($conn, $keyTable, $key);

////////////////////////////////////////////////////////////
// close the collection 
$conn->close();             // close the connection


/**
 * @brief form the answer key
 *
 * @note id and title already has single quote around it, so when inserting
 *       into the table, do not need to add quote agian.
 */
function formKey($id, $title, $left_value, $right_value, $points){
    return array('id' => "'$id'",
	    'title' => "'$title'",
	    'left_value' => "$left_value",
	    'right_value' => "$right_value",
	    'points' => "$points"
    );
}

function writeKey($conn, $keyTable, $data){
    // prepare the keys and values to insert
    $cols = implode(", ", array_keys($data));
    $values = implode(", ", array_values($data));

    // remove the existing data
    $sql = "select * from $keyTable where id={$data['id']}";
    $tmp = $conn->query($sql);
    if($tmp->num_rows > 0){ 
	// if entry exist, then delete it first
	$conn->query(" delete from $keyTable where id={$data['id']} ");
    }

    // write data
    $sql = "insert into $keyTable ($cols) values ($values)";
    if($conn->query($sql) == FALSE){
	    echo "error:" . $sql . "<br>" . $conn->error;
    };    
}

function createKeyTable($conn, $keyTable){
    $result = $conn->query("show tables like '$keyTable'");
    if ($result->num_rows == 0){  // table does not exist
	$sql = "create table $keyTable (" .
            "id text, " .
	    "title text, " .
            "left_value double, " .
	    "right_value double, " .
	    "points double ".
	    ")";
	// echo $sql; 
    	if($conn->query($sql) == FALSE){
	    echo "error:" . $sql . "<br>" . $conn->error;
	};    
    }
}

function createSubmitTable($conn, $submitTable, $questions){
    $result = $conn->query("show tables like '$submitTable'");
    if ($result->num_rows == 0){  // table does not exist
	$sql = "create table $submitTable (" .
            "email text, " .
	    "time datetime, " .
	    "hasGraded integer ";
	foreach($questions as $key => $value){
	    $sql .= ", $value double ";
	}
        
	$sql .= ")" ;
	
	echo $sql;
    	if($conn->query($sql) == FALSE){
	    echo "error:" . $sql . "<br>" . $conn->error;
	};    
    }
}

function createGradeTable($conn, $gradeTable, $questions){
    $result = $conn->query("show tables like '$gradeTable'");
    if ($result->num_rows == 0){  // table does not exist
	$sql = "create table $gradeTable (" .
            "email text, " .
	    "time datetime, " .
	    "sum double, " .
	    "max double, " .
	    "percent double ";
	foreach($questions as $key => $value){
	    $sql .= ", $value double ";
	}
        
	$sql .= ")" ;
	
	echo $sql;
    	if($conn->query($sql) == FALSE){
	    echo "error:" . $sql . "<br>" . $conn->error;
	};    
    }
    
}


?>
