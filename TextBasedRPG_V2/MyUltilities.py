# ====IMPORTS==== #
import subprocess
import sys
import os
import ctypes

# ====OPEN CMD TERMINAL==== #
script_path = os.path.abspath(sys.argv[0])
if '--new-cmd' not in sys.argv:
    # "/k" for debugging , "/c" for instant exit
    cmd_command = f'start cmd /c "mode con: cols=100 lines=40 && python \"{script_path}\" --new-cmd"'
    subprocess.run(cmd_command, shell=True)
    sys.exit()

# ====SETUP FOR CURSOR==== #
std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
def SetCursorPos(x, y):
    position = (y << 16) | x
    ctypes.windll.kernel32.SetConsoleCursorPosition(std_out_handle, position)

class CONSOLE_CURSOR_INFO(ctypes.Structure):
    _fields_ = [("dwSize", ctypes.c_ulong),
                ("bVisible", ctypes.c_bool)]

def set_cursor_visibility(visible: bool):
    cursor_info = CONSOLE_CURSOR_INFO()
    cursor_info.dwSize = 1  # size of the cursor, 1-100
    cursor_info.bVisible = visible
    ctypes.windll.kernel32.SetConsoleCursorInfo(std_out_handle, ctypes.byref(cursor_info))
set_cursor_visibility(False) # Initialise cursor visibility to be false