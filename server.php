<?php

extract($_GET);

$myfile = fopen("uploads/test.txt", "w");
fwrite($myfile, $sentence);
fclose($myfile);

$command = escapeshellcmd('python3 exec.py');
$output = explode(" ", shell_exec($command));
$sentiment = $output[0];
$polarity = $output[1];

switch ($sentiment) {
case 1 :
{
	$file = fopen("1.jpg", "rb");
	$data = fread($file, filesize("1.jpg"));
	$sent = "POSITIVE";
	break; 
}
case -1 :
{
	$file = fopen("-1.jpg", "rb");
	$data = fread($file, filesize("-1.jpg"));
	$sent = "NEGATIVE";
	break; 
}
default :
{
	$file = fopen("0.jpg", "rb");
	$data = fread($file, filesize("0.jpg"));
	$sent = "NEUTRAL";
	break; 
}
}

header("sentiment:$sent");
header("polarity:$polarity");
echo $data;

?>
