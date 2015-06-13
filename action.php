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
	    $dbname = "key";
	    
	    // connect to MySQL server
	    $conn = mysqli_connect($servername, $username, $password, $dbname);
	    if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	    }
	    // echo "Connected successfully";
	    
	    /* obtain submitted data */
	    $userSubmit = extractSubmit($_POST);
	    $userAnswerAndEmail = extractAnswerAndEmail($userSubmit);

	    /* point to the correct table */
	    $tableNames =  findTableNames($userSubmit['hwNo']);
	    $keyTable = $tableNames['key'];
	    $submitTable = $tableNames['submit'];
	    $gradesTable = $tableNames['grades'];
	    
	    /* sumbit the answer into database*/
	    submit($conn, $userAnswerAndEmail,  $submitTable);
	    
	    /* grade submission and send grade email */
	    grade($conn, $keyTable, $submitTable, $gradesTable);
	    
	    ////////////////////////////////////////////////////////////
	    $conn->close();             // close the connection
	    
	}
		
	?>
	
    </body>
</html>
