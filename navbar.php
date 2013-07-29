<?php
$parts = Explode('/', $_SERVER["SCRIPT_NAME"]);
$currentFile = $parts[count($parts) - 1];
?>
<div style="margin-left: auto; margin-right: auto; padding: 0px; width: 960px;">
<?php if ($currentFile != "index.php") { ?>

<?php 
if ($currentFile == "about.php") {
	echo "<span style=\"color: #00CC00\"><strong>About</strong></span>";
} else {
	echo "<a href=\"../personal/about.php\">About</a>";
}
/*echo "&nbsp;::&nbsp;";
if ($currentFile == "zhongwen.php") {
	echo "<span style=\"color: #00CC00\"><strong>中文</strong></span>";
} else {
	echo "<a href=\"../personal/zhongwen.php\">中文</a>";
}*/
echo "&nbsp;||&nbsp;";
if ($currentFile == "skills.php") {
	echo "<span style=\"color: #00CC00\"><strong>Skills</strong></span>";
} else {
	echo "<a href=\"../professional/skills.php\">Skills</a>";
}
echo "&nbsp;::&nbsp;";
if ($currentFile == "work.php") {
	echo "<span style=\"color: #00CC00\"><strong>Work History</strong></span>";
} else {
	echo "<a href=\"../professional/work.php\">Work History</a>";
}
echo "&nbsp;::&nbsp;";
if ($currentFile == "education.php") {
	echo "<span style=\"color: #00CC00\"><strong>Education</strong></span>";
} else {
	echo "<a href=\"../professional/education.php\">Education</a>";
}
echo "&nbsp;::&nbsp;";
if ($currentFile == "contact.php") {
	echo "<span style=\"color: #00CC00\"><strong>Contact</strong></span>";
} else {
	echo "<a href=\"../professional/contact.php\">Contact</a>";
}
?>

<br />
<?php } 
if ($currentFile == "index.php") {
	echo "<a style=\"color: #FFFFFF\" href=\"personal/about.php\"><strong>John Dietrick</strong></a> :: Beijing";
} else {
	echo "<a style=\"color: #FFFFFF\" href=\"../\"><strong>John Dietrick</strong></a> :: Beijing";
}?>
</div>
