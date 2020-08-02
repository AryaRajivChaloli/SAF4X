<?php

    extract($_GET);

    $command = escapeshellcmd('python solution.py "'.$sentence.'"');
    $output = explode(" ", shell_exec($command));
    $sentiment = $output[0];
    $negscore = $output[1];
    $neuscore = $output[2];
    $posscore = $output[3];
    $compound = $output[4];

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
    header("negscore:$negscore");
    header("neuscore:$neuscore");
    header("posscore:$posscore");
    header("compound:$compound");
    echo $data;

?>