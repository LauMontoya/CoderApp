# CoderApp
Curso CoderHouse
# README - Código de Ejemplo Django

Este es un proyecto de ejemplo que utiliza el framework Django para crear una aplicación web básica. A continuación, se describen las diferentes vistas y funciones implementadas en este código:

## Archivo views.py

### Función `saludo(request)`
Esta función maneja la solicitud para la vista `saludo`. Cuando un usuario accede a la URL correspondiente a esta vista, se devuelve una respuesta HTTP que contiene el mensaje "SALUDOS".

### Función `segundo(request)`
Esta función maneja la solicitud para la vista `segundo`. Cuando un usuario accede a la URL correspondiente a esta vista, se devuelve una respuesta HTTP que contiene el mensaje "ESTA ES LA SEGUNDA VISTA".

### Función `diadehoy(request)`
Esta función maneja la solicitud para la vista `diadehoy`. Cuando un usuario accede a la URL correspondiente a esta vista, se obtiene la fecha y hora actual y se genera una respuesta HTTP que muestra esta información en formato de texto.

### Función `minombreEs(self, nombre)`
Esta función toma un parámetro `nombre` y genera una respuesta HTTP que muestra el mensaje "Mi nombre es:" seguido del valor proporcionado para `nombre`.

### Función `probandotemplate(self)`
Esta función muestra cómo utilizar plantillas en Django. Carga un archivo HTML de la ubicación especificada, reemplaza variables dentro de la plantilla con los valores correspondientes y devuelve una respuesta HTTP que muestra el contenido resultante de la plantilla renderizada.

## Uso
Para utilizar este código de ejemplo:

1. Asegúrate de tener Django instalado en tu entorno de desarrollo.

2. Crea un proyecto Django y una aplicación en tu entorno.

3. Copia y pega el contenido del archivo `views.py` en el archivo correspondiente de tu aplicación Django.

4. Configura las URL de tu proyecto para que coincidan con las vistas definidas en `views.py`.

5. Ejecuta el servidor de desarrollo de Django.

6. Accede a las diferentes URLs para probar cada una de las vistas y ver las respuestas generadas.

