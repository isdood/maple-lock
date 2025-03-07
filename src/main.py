import os
import platform
import subprocess
import time

def detect_usb_insertion():
    if platform.system() == "Linux":
        return detect_usb_insertion_linux()
    elif platform.system() == "Windows":
        return detect_usb_insertion_windows()
    elif platform.system() == "Darwin":
        return detect_usb_insertion_macos()
    elif platform.system() == "Android":
        return detect_usb_insertion_android()
    else:
        raise NotImplementedError("Unsupported platform")

def detect_usb_insertion_linux():
    while True:
        result = subprocess.run(['lsblk', '-o', 'NAME,TRAN'], stdout=subprocess.PIPE)
        devices = result.stdout.decode('utf-8').split('\n')
        for device in devices:
            if 'usb' in device:
                return True
        time.sleep(1)

def detect_usb_insertion_windows():
    while True:
        result = subprocess.run(['wmic', 'logicaldisk', 'get', 'description'], stdout=subprocess.PIPE)
        devices = result.stdout.decode('utf-8').split('\n')
        for device in devices:
            if 'Removable Disk' in device:
                return True
        time.sleep(1)

def detect_usb_insertion_macos():
    while True:
        result = subprocess.run(['diskutil', 'list'], stdout=subprocess.PIPE)
        devices = result.stdout.decode('utf-8').split('\n')
        for device in devices:
            if 'external' in device:
                return True
        time.sleep(1)

def detect_usb_insertion_android():
    while True:
        result = subprocess.run(['ls', '/storage'], stdout=subprocess.PIPE)
        devices = result.stdout.decode('utf-8').split('\n')
        for device in devices:
            if 'usb' in device:
                return True
        time.sleep(1)

def launch_interface():
    if platform.system() == "Linux":
        os.system("python3 src/interface.py")
    elif platform.system() == "Windows":
        os.system("python src/interface.py")
    elif platform.system() == "Darwin":
        os.system("python3 src/interface.py")
    elif platform.system() == "Android":
        os.system("python3 src/interface.py")
    else:
        raise NotImplementedError("Unsupported platform")

if __name__ == "__main__":
    if detect_usb_insertion():
        launch_interface()
