<?php
/* Incluir el archivo de conexión */
include("conexion.php");

/* Crear la conexión */
$con = conectar();

/* Consultar los datos de la tabla alumnos */
$sql = "SELECT * FROM alumnos";
$query = mysqli_query($con, $sql);
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TABLA DE ALUMNOS</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        h1 {
            text-align: center;
        }

        /* Hace que la tabla ocupe todo el ancho disponible */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        /* Estilo para dar borde y espacio a las celdas */
        th, td {
            border: 1px solid #000;
            padding: 12px;
            text-align: center;
            height: 30px; 
        }

        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>

    <h1>TABLA DE ALUMNOS</h1>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Matrícula</th>
                <th>Nombre</th>
                <th>Apellido Paterno</th>
                <th>Apellido Materno</th>
                <th>Edad</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            <?php
            while ($row = mysqli_fetch_assoc($query)){
            ?>
            <tr>
                <td><?php echo $row['id']; ?></td>
                <td><?php echo $row['matricula']; ?></td>
                <td><?php echo $row['nombre']; ?></td>
                <td><?php echo $row['apellido_p']; ?></td>
                <td><?php echo $row['apellido_m']; ?></td>
                <td><?php echo $row['edad']; ?></td>
                <td>
                    <!-- Enlaces dinámicos para eliminar y editar -->
                    <a href="delete.php?id=<?php echo $row['id']; ?>">Eliminar</a>
                    <br>
                    <a href="editar.php?id=<?php echo $row['id']; ?>">Editar</a>
                </td>
            </tr>
            <?php 
            } 
            ?>
        </tbody>
    </table>

    <h1>Formulario</h1>
    <form action="insertar.php" method="POST">
        <input type="text" class="form-control" name="matricula" placeholder="Matrícula"><br><br>
        <input type="text" class="form-control" name="nombre" placeholder="Nombre"><br><br>
        <input type="text" class="form-control" name="apellido_p" placeholder="Apellido Paterno"><br><br>
        <input type="text" class="form-control" name="apellido_m" placeholder="Apellido Materno"><br><br>
        <input type="text" class="form-control" name="edad" placeholder="Edad"><br><br>

        <input type="submit" value="Enviar">
    </form>
</body>
</html>