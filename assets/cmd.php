<?php
$cmd = htmlspecialchars($_POST['cmd']);
file_put_contents('capture.txt', $cmd);
?>