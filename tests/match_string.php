<?php
echo "Welcome to XSS Fun<br> ";
if (isset($_GET['pay'])){
	echo $_GET['pay'];
}
?>
