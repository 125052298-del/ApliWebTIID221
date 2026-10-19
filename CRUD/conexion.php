<?php
/* Creamos una función llamada conectar */
function conectar() {
    /* Información del servidor */
    $host = "localhost";
    $user = "root";
    $pass = "";

    /* Base de datos */
    $db = "alumnos";

    /* Nos conectamos a la base de datos con mysqli_connect() */
    $con = mysqli_connect($host, $user, $pass, $db);

    /* Verificamos si hubo error de conexión */
    if (!$con) {
        die("Conexión fallida: " . mysqli_connect_error());
    }

    return $con;
}
?>