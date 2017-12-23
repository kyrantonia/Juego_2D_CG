import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\Kyra\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Kyra\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"
from cx_Freeze import setup, Executable
setup(
    options={"build_exe": {
        'packages': ["os", "math", "pygame", "OpenGL","random","sys"],
        'include_files': ["texturas_opengl.py","pato2.jpg","musica.mp3", "rebote.ogg","cuac.ogg","CC3501Utils.py","disqualified.ogg","muros2.py","Objetos.py","pato.py","plataforma1.py","plataforma3.py","plataforma_2.py","texto.py","Variables.py"],  # SI USARON ARCHIVOS, VAN ACA
        'include_msvcr': True,
    }},
    executables=[Executable("Main.py", base="Win32GUI")]
)
