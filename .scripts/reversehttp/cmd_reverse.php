<?php
$cmd = htmlspecialchars($_POST['cmd']);
file_put_contents('cmd.txt', $cmd);
?>