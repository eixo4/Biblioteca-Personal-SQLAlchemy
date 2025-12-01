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
````

### MacOS (Homebrew)

```bash
brew install mariadb
brew services start mariadb
```

## 🚀 Configuración del Proyecto

### 1\. Preparar la Base de Datos

Antes de ejecutar Python, debes crear la base de datos vacía. Entra a tu consola de MariaDB/MySQL:

```sql
-- Entra a la consola (te pedirá contraseña)
mysql -u root -p

-- Ejecuta este comando SQL:
CREATE DATABASE biblioteca_db;
```

### 2\. Instalar Librerías Python

En la carpeta del proyecto, ejecuta:

```bash
pip install -r requirements.txt
```

### 3\. Configurar Credenciales

Abre el archivo `database.py` y edita la sección de configuración con **tus datos**:

```python
DB_USER = 'root'
DB_PASS = 'TU_CONTRASEÑA_AQUI'  <-- ¡Importante!
DB_HOST = 'localhost'
DB_NAME = 'biblioteca_db'
```

## ▶️ Ejecución

```bash
python main.py
```
