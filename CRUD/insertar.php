<?php
include("conexion.php");

/* Conexión por llamada a la función conectar() */
$con = conectar();  

$matricula = $_POST['matricula'];
$nombre = $_POST['nombre'];
$apellido_p = $_POST['apellido_p'];
$apellido_m = $_POST['apellido_m'];
$edad = $_POST['edad'];

/* Obtenemos la consulta utilizando los nombres reales de la BD */
$sql = "INSERT INTO alumnos (matricula, nombre, apellido_p, apellido_m, edad) 
VALUES ('$matricula', '$nombre', '$apellido_p', '$apellido_m', '$edad')";

/* Ejecutamos la consulta */
$query = mysqli_query($con, $sql);

/* Comprobar y direccionar */
if ($query) {
    header("Location: alumnos.php");
} else {
    echo "Error al insertar el registro: " . mysqli_error($con);
}
?>