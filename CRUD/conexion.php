<?php
/* Creamos una funcion llamada conectar */
function conectar() {
    /* informacion del servidor */
    $host = "localhost";
    $user = "root";
    $pass = "";

    /* Base de datos */
    $db = "aw221";

    /* Nos conectamos a la base de datos con mysqli_connect() */
    $con = mysqli_connect($host, $user, $pass, $db);

    return $con;
}
?>