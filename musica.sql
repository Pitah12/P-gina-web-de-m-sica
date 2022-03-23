/*Crea una base de datos "soundme" con una tabla llamada "usuarios"
    * con los campos "id" autoincrement, "nombre", "apellido", "email", "password"
*/
CREATE DATABASE soundme;
use soundme;
CREATE TABLE usuarios (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

/*Insert del usuario admin*/
INSERT INTO usuarios (nombre, apellido, email, password) VALUES ('admin', 'admin', 'admin@gmail.com', 'asir21');