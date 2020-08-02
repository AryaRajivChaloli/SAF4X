<?php
    move_uploaded_file($_FILES["sentences"]["tmp_name"], "uploads/test.csv");

    $command = escapeshellcmd('python exec-batch.py');
    $accuracy = trim(shell_exec($command))."%";

    header("Location: http://localhost/SIH/SIH_Final/Ver4.X/csvip.php?accuracy=$accuracy");
    exit();
?>
