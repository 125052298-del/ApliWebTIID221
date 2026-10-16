<?php
/*Incluir info del archivo*/
include ("conexion.php");
/*Conexion por llamada a la funcion conectar()*/
$con= conectar();
/*Obtenemos la consulta y tendremos acceso a la bd*/
$sql = "SELECT * FROM alumnos";
$query = mysqli_query($con,$sql);
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

        /* Estilo para dar borde y espacio a los cuadros (celdas) */
        th, td {
            border: 1px solid #000;
            padding: 12px;
            text-align: center;
            height: 30px; 
        }


        th {
            background-color: #f2f2f2;
        }

        button {
            padding: 5px 10px;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <h1>TABLA DE ALUMNOS</h1>

    <table>
        <thead>
            <tr>
                <th>Matrícula</th>
                <th>Nombre</th>
                <th>Apellido Paterno</th>
                <th>Apellido Materno</th>
                <th>Edad</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
        
            <tr>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td>
                    <button>Editar</button>
                    <button>Eliminar</button>
                </td>
            </tr>
        </tbody>
    </table>

</body>
</html>