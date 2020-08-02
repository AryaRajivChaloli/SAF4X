<?php

    extract($_GET);

    $command = escapeshellcmd('python exec.py "'.$sentence.'"');
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
            #echo "neutral";
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