import os
from PyPDF2 import PdfMerger

# Directorio que contiene los archivos PDF
directorio_pdf = "pdfs"

# Obtener la lista de archivos PDF en el directorio y ordenar alfabéticamente
archivos_pdf = sorted([archivo for archivo in os.listdir(directorio_pdf) if archivo.endswith(".pdf")])

# Crear el objeto PdfFileMerger
merger = PdfMerger()

# Recorrer los archivos PDF y agregarlos al objeto PdfFileMerger
for archivo_pdf in archivos_pdf:
    ruta_pdf = os.path.join(directorio_pdf, archivo_pdf)
    merger.append(ruta_pdf)

# Guardar el archivo PDF combinado
pdf_combinado = os.path.join(directorio_pdf, "pdf_combinado.pdf")
merger.write(pdf_combinado)

# Cerrar el objeto PdfFileMerger
merger.close()
