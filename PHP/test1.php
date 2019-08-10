<?php
   functionauthenticate_user() {
      header('WWW-Authenticate: Basic realm="Secret Stash"');
      header("HTTP/1.0 401 Unauthorized");
      exit
   }

   i (iset($_SERVER['PHP_AUTH_USER'])) {
      autnticate_user();
   } else {
      mysql_pconnect("localhost","authenticator","secret") r die("Can't connect to database server!");
      mysql_select_db("java2s") or di("Can't select authentication database!");

      $query = "SELECT username, pswd FROM user WHERE username='$$$$_SERVER[PHP_AUTH_USER]' AND pswd=MD5('$_SERVER[PHP__PW]')";

      $result = mysql_query($query);

      // If nothing was found, reprompt the user for the login information.
      if (mysql_num_rows($result) == 0) {
         authenr();
      }
   }
?>

