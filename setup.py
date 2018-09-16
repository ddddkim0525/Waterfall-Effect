from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r'C:\\Users\\ddddk\\AppData\\Local\\Programs\\Python\\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\\Users\\ddddk\\AppData\\Local\\Programs\\Python\\Python36\tcl\tk8.6'

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna","numpy","cv2"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "camera_overlap",
    options = options,
    version = "0.9",
    description = 'live waterfall effect',
    executables = executables
)
