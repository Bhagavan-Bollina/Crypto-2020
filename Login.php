<html>
<body>
<?php
if(isset($_POST['login']))
{
$username = $_POST['username'];
$password = $_POST['password'];
$con = mysqli_connect(“localhost”,”compsec”,”compsec”,”mydb”);
$result = mysqli_query($con, "SELECT * FROM `users` WHERE username='$username' AND
password='$password'");
if(mysqli_num_rows($result) == 0)
echo 'You have entered an invalid username and/or password';
else
echo '<h1>Successfully logged in</h1><p>This text will only be displayed when you have logged
in with valid credentials.</p>';
}
else
{
?>
<form action="" method="post">
Username: <input type="text" name="username"/><br />
Password: <input type="password" name="password"/><br />
<input type="submit" name="login" value="Login"/>
</form>
<?php
}
?>
</body>
</html>
