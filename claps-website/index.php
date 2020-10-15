<?php
$fd = fopen("claps.json", 'r');
$claps = fread($fd,1024);
fclose($fd);
echo $claps;
?>