<?php
include("conexion.php");

$con = conectar();

/* SI EL FORMULARIO FUE ENVIADO POR POST, ACTUALIZAMOS LOS DATOS */
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $id = $_POST['id'];
    $matricula = $_POST['matricula'];
    $nombre = $_POST['nombre'];
    $apellido_p = $_POST['apellido_p'];
    $apellido_m = $_POST['apellido_m'];
    $edad = $_POST['edad'];

    /* Sentencia SQL para actualizar el registro */
    $sql = "UPDATE alumnos SET matricula='$matricula', nombre='$nombre', apellido_p='$apellido_p', apellido_m='$apellido_m', edad='$edad' WHERE id='$id'";
    $query = mysqli_query($con, $sql);

    if ($query) {
        header("Location: alumnos.php");
        exit();
    } else {
        echo "Error al actualizar el registro: " . mysqli_error($con);
    }
}

/* SI SE ACCEDE POR GET (DESDE EL ENLACE), MOSTRAMOS EL FORMULARIO */
$id = $_GET['id'];
$sql = "SELECT * FROM alumnos WHERE id='$id'";
$query = mysqli_query($con, $sql);
$row = mysqli_fetch_assoc($query);
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar Alumno</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            text-align: center;
        }
        form {
            width: 300px;
            margin: 0 auto;
        }
        input[type="text"], input[type="submit"] {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
            box-sizing: border-box;
        }
    </style>
</head>
<body>

    <h1>EDITAR ALUMNO</h1>

    <!-- El action apunta al mismo archivo editar.php -->
    <form action="editar.php" method="POST">
        <!-- Campo oculto con el ID para saber qué registro actualizar -->
        <input type="hidden" name="id" value="<?php echo $row['id']; ?>">

        <label>Matrícula:</label>
        <input type="text" class="form-control" name="matricula" value="<?php echo $row['matricula']; ?>"><br><br>

        <label>Nombre:</label>
        <input type="text" class="form-control" name="nombre" value="<?php echo $row['nombre']; ?>"><br><br>

        <label>Apellido Paterno:</label>
        <input type="text" class="form-control" name="apellido_p" value="<?php echo $row['apellido_p']; ?>"><br><br>

        <label>Apellido Materno:</label>
        <input type="text" class="form-control" name="apellido_m" value="<?php echo $row['apellido_m']; ?>"><br><br>

        <label>Edad:</label>
        <input type="text" class="form-control" name="edad" value="<?php echo $row['edad']; ?>"><br><br>

        <input type="submit" value="Guardar Cambios">
    </form>

</body>
</html>