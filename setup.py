import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
	"packages": [
		"pygame",
		"Button",
		"Location",
		"Menu",
		"RPS",
		"RPS_Music",
		"Risk",
		"Risk_Game_State_Display",
		"Risk_Player",
		"constants"
	],
	"include_files": [
		"assets/"
	]
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "RiskPaperScissors",
        version = "0.1",
        description = "Risk Paper Scissors!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)])