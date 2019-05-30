<?php

$enlace = mysql_connect("localhost", "root", "asdf1234");
mysql_select_db("pruebas", $enlace);

$resultado = mysql_query("select count(*),edad from usuarios group by edad", $enlace);
$número_filas = mysql_num_rows($resultado);

echo "$número_filas Filas\n";

?>