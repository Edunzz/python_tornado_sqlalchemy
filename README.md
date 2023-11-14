# Guía de Configuración y Ejecución de Aplicación Python con Tornado y MySQL

## Descripción de la Arquitectura

Esta aplicación utiliza Python con el framework Tornado para manejar solicitudes HTTP y comunicarse con una base de datos MySQL. La base de datos se ejecuta en un contenedor Docker, proporcionando un entorno de base de datos consistente y fácil de configurar. El código de la aplicación y la configuración de la base de datos están alojados en GitHub, permitiendo una fácil distribución y despliegue.

La estructura del proyecto es la siguiente:

-   `/app/app.py`: Contiene el código fuente de la aplicación Python con Tornado.
-   `/mysql/docker-compose.yaml`: Define la configuración del contenedor Docker para MySQL.

## Pre-requisitos

Asegúrate de tener instalado lo siguiente en tu entorno Windows:

-   Git
-   Python 3.x
-   pip (Administrador de paquetes de Python)
-   Docker Desktop para Windows

## Paso 1: Clonar el Repositorio

Clona el repositorio desde GitHub para obtener el código de la aplicación y la configuración de Docker. Abre una terminal y ejecuta:

`git clone https://github.com/Edunzz/python_tornado_sqlalchemy.git
cd python_tornado_sqlalchemy` 

## Paso 2: Instalación de Bibliotecas Python

Instala las bibliotecas necesarias para Python utilizando pip. En la terminal, ejecuta:

`pip install tornado sqlalchemy pymysql` 

## Paso 3: Definición de Variables de Entorno

Para configurar las variables de entorno necesarias para la aplicación, puedes utilizar la consola de comandos (CMD) en Windows. Es importante que uses la misma instancia de CMD para configurar las variables y para ejecutar tu aplicación, ya que las variables de entorno establecidas en CMD son específicas de esa sesión.

3.1.  **Abrir CMD en la Ruta Correcta:**
    
    -   Presiona `Win + R`, escribe `cmd` y presiona `Enter`.
    -   Navega a la carpeta donde clonaste el repositorio utilizando el comando `cd`. Por ejemplo:
                
        `cd ruta\a\python_tornado_sqlalchemy` 
        
3.2.  **Establecer Variables de Entorno:**
    
    -   En la ventana de CMD, establece las variables de entorno utilizando el comando `set`. Por ejemplo:
                
        `set DBHOST=la_ip_de_tu_contenedor
        set DBPORT=3306` 
        
    -   Reemplaza `la_ip_de_tu_contenedor` con la dirección IP real de tu contenedor Docker MySQL.
3.3.  **Verificar Variables de Entorno:**
    
    -   Puedes verificar que las variables se hayan establecido correctamente con:
                
        `echo %DBHOST%
        echo %DBPORT%` 
        
    -   Deberías ver los valores que acabas de establecer.
3.4.  **Mantener Abierta la Consola de Comandos:**
    
    -   Mantén abierta esta ventana de CMD para ejecutar tu aplicación Python. Si cierras esta ventana o abres una nueva, tendrás que volver a establecer las variables de entorno.

## Paso 4: Levantar el Contenedor Docker MySQL

En la terminal, navega a la carpeta `/mysql` y ejecuta:

`docker-compose up -d` 

Esto levantará el contenedor de MySQL según la configuración definida en `docker-compose.yaml`.

## Paso 5: Obtener la IP del Contenedor Docker

Para obtener la dirección IP del contenedor, utiliza:

`docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nombre_contenedor` 

Reemplaza `nombre_contenedor` con el nombre real de tu contenedor MySQL.

## Paso 6: Ejecutar la Aplicación Python

Navega a la carpeta `/app` y ejecuta el script `app.py`:

`python app.py` 

## Conclusión

Al seguir estos pasos, tendrás tu aplicación Python con Tornado corriendo y conectándose a una base de datos MySQL en un contenedor Docker en Windows.
