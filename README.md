# Biblioteca Personal (MariaDB + SQLAlchemy) 📚🐬

Gestor de libros migrado a una arquitectura ORM moderna, utilizando **MariaDB** como motor de base de datos y **SQLAlchemy** para el manejo de datos en Python.

## ⚙️ Prerrequisitos

1.  **Python 3.8+**
2.  **Servidor MariaDB** (o MySQL) instalado y ejecutándose.

## 🛠️ Instalación de MariaDB

### Windows
1. Descarga el instalador MSI desde [mariadb.org](https://mariadb.org/download/).
2. Durante la instalación, **establece una contraseña para el usuario 'root'** y recuérdala.
3. Asegúrate de instalar "HeidiSQL" (incluido) para visualizar tu base de datos fácilmente.

### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install mariadb-server
sudo mysql_secure_installation
