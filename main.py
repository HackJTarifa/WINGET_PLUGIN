import subprocess
import win32com.client as wincl
import sys

sys.path.append(r'C:\\Users\\JTarifa\\AppData\\Roaming\\Python\\Python37\\site-packages')

import pyautogui

import ctypes

def check_admin_permissions():
    is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    return is_admin

if __name__ == "__main__":
    if check_admin_permissions():
        print("El script se está ejecutando con permisos de administrador.")
    else:
        print("El script se está ejecutando sin permisos de administrador.")


def run_winget(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        print(f'Error executing command: {e}')
        return None


shell = wincl.Dispatch("WScript.Shell")
shell.Run("cmd.exe /K winget install --id=ShareX.ShareX -e")

# Instalar la aplicación ShareX
app_id = 'ShareX.ShareX'
command = f'winget install --id={app_id} -e'
comando = 'winget install --id=ShareX.ShareX -e'
proceso = subprocess.Popen(comando, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
proceso.wait()
# output = run_winget(command)
# if output:
#    print(output)


# injectar comando a la ventana cmd, espera un segundo
pyautogui.sleep(1)
pyautogui.typewrite("winget list")
pyautogui.press("enter")

pyautogui.sleep(3
                )
pyautogui.typewrite("cls")
pyautogui.press("enter")

