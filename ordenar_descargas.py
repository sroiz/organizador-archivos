import os
import shutil
import pathlib

categorias = {
    # Imágenes
    ".jpg": "Imagenes",
    ".jpeg": "Imagenes",
    ".png": "Imagenes",
    ".gif": "Imagenes",
    ".bmp": "Imagenes",
    ".svg": "Imagenes",
    ".webp": "Imagenes",
    ".ico": "Imagenes",
    ".tiff": "Imagenes",
    ".raw": "Imagenes",

    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",
    ".flac": "Audio",
    ".ogg": "Audio",
    ".wma": "Audio",
    ".m4a": "Audio",

    # Video
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",
    ".m4v": "Videos",

    # Documentos
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".doc": "Documentos",
    ".txt": "Documentos",
    ".odt": "Documentos",
    ".rtf": "Documentos",
    ".xlsx": "Documentos",
    ".xls": "Documentos",
    ".csv": "Documentos",
    ".ods": "Documentos",
    ".pptx": "Documentos",
    ".ppt": "Documentos",
    ".odp": "Documentos",

    ".zip": "Archivos",
    ".rar": "Archivos",
    ".7z": "Archivos",
    ".tar": "Archivos",
    ".gz": "Archivos",
    ".exe": "Archivos",
    ".msi": "Archivos",
    ".dmg": "Archivos",
    ".pkg": "Archivos",
    ".apk": "Archivos",
    ".py": "Programacion",
        
    ".js": "Programacion",
    ".html": "Programacion",
    ".css": "Programacion",
    ".json": "Programacion",
    ".xml": "Programacion",
    ".sql": "Programacion",
    ".ts": "Programacion",
    ".cpp": "Programacion",
    ".java": "Programacion",
    ".c": "Programacion",
    ".cs": "Programacion",
    ".php": "Programacion",
    ".rb": "Programacion",
    ".go": "Programacion",
    ".rs": "Programacion",
    ".kt": "Programacion",
    ".swift": "Programacion",
}

inicio=os.path.expanduser("~")
ruta_inicial=os.path.expanduser("~/Downloads")
carpeta_final= f"{inicio}/Desktop/orden"
os.makedirs(carpeta_final,exist_ok=True)

archivos=os.listdir(ruta_inicial)


cuenta=0
for index,archivo in enumerate(archivos):

    tipo_archivo=pathlib.Path(f"{ruta_inicial}/{archivo}").suffix.lower()
    categoria=categorias.get(tipo_archivo, "Otros")
    
    if os.path.isdir(f"{ruta_inicial}/{archivo}"):
        continue 
    
    os.makedirs(f"{carpeta_final}/{tipo_archivo}", exist_ok=True)
    shutil.move(f"{ruta_inicial}/{archivo}",f"{carpeta_final}/{tipo_archivo}")

    cuenta+=1

print("Número de archivos organizados:",cuenta)  

