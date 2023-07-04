# Unir archivos PDF

Este script de Python te permite unir varios archivos PDF en un solo archivo PDF.

## Requisitos

- Python 3.x
- PyPDF2 (instalable a través de `pip install PyPDF2`)

## Uso

1. Asegúrate de tener los archivos PDF que deseas unir en la carpeta `pdfs`.
2. Ejecuta el script `unir_pdf.py`.
3. El script buscará todos los archivos PDF en la carpeta `pdfs` y los unirá en un solo archivo llamado `pdf_combinado.pdf`.
4. El archivo PDF combinado se guardará en la carpeta `pdfs`.

Ten en cuenta que los archivos PDF se unirán en orden alfabético por nombre de archivo.

## Personalización

Si deseas personalizar el comportamiento del script, puedes modificar los siguientes parámetros:

- `directorio_pdf`: puedes cambiar el nombre de la carpeta donde se encuentran los archivos PDF. Asegúrate de que el nombre coincida con el nombre de la carpeta en tu sistema.
- `pdf_combinado`: puedes cambiar el nombre del archivo PDF combinado.

## Notas

- Asegúrate de tener instalada la biblioteca `PyPDF2` ejecutando `pip install PyPDF2`.
- Los archivos PDF deben estar en el formato correcto y no estar dañados para que el script funcione correctamente.
- Antes de ejecutar el script en un entorno de producción, se recomienda realizar pruebas y asegurarse de que los archivos y las rutas sean correctos.

¡Disfruta de la unión de tus archivos PDF con este script! Si tienes alguna pregunta o sugerencia, no dudes en contactarme.
