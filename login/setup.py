import sys
from cx_Freeze import  setup, Executable

# Dependencies (add more if needed)
build_exe_options = {"packages": ["your_packages"], "excludes": []}

# Executable
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="JSS",
    version="1.0",
    description="Application pour gérer le club sportif JSS Saoula",
    options={"build_exe": build_exe_options},
    executables=[Executable("login.py", base=base)]
)
