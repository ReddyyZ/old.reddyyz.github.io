<?php
$article = $_GET['article'];
if (!isset($article)){ exit(1); }

$fd = fopen("claps.json", "r");
$claps = fread($fd,1024);
fclose($fd);

$claps = json_decode($claps);
var_dump($claps);

$claps->$article = $claps->$article + 1;
$fd = fopen("claps.json", "w");
fwrite($fd, json_encode($claps));
fclose($fd);
?>