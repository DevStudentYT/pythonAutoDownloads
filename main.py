import os
import shutil

path = r'C:/Users/Nando/Downloads'
music_dst_path = path + r"/Music"
image_dst_path = path + r"/Image"
docs_dst_path = path + r"/Documents"
exec_dst_path = path + r"/Execs"
weird_dst_path = path + r"/ArchivosRaros"

for pathDir in os.listdir(path):
    print(pathDir)
    index = pathDir.find(".")
    lastIndex = len(pathDir) - 1
    extension = pathDir[index::].lower()

    # Mover imagenes
    if extension == ".png" or extension == ".jpg" or extension == ".gif" or extension == ".jpeg":
        # Movimiento de la variable pathDir hacia la carpeta Imagenes
        shutil.move(path + "/" + pathDir, image_dst_path, copy_function=shutil.copy2)
    if extension == ".mp3" or extension == ".mp4" or extension == ".wav" :
        # Movimiento de la variable pathDir hacia la carpeta Musica
        shutil.move(path + "/" + pathDir, music_dst_path, copy_function=shutil.copy2)
    if extension == ".doc" or extension == ".csv" or extension == ".pdf" or extension == ".zip" or extension ==".xlsx":
        # Movimiento de la variable pathDir hacia la carpeta Documentos
        shutil.move(path + "/" + pathDir, docs_dst_path, copy_function=shutil.copy2)
    if extension == ".exe":
        # Movimiento de la variable pathDir hacia la carpeta ejecutable
        shutil.move(path + "/" + pathDir, exec_dst_path, copy_function=shutil.copy2)
    else:
        if not (path == "Music" or path == "Image" or path == "Documents" or path == "Execs"):
            shutil.move(path + "/" + pathDir, weird_dst_path, copy_function=shutil.copy2)
    print(extension, "\n")
