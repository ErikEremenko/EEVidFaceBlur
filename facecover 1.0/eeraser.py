import os, glob
from colorama import Fore, Back, Style 



def erase_command():
    shure = input()
    for filename in glob.glob("./face*"):


        if shure == 'yyy':  
            os.remove(filename)
            print(Fore.GREEN + 'file deleted')
            

        else:
            print(Fore.RED + 'operation aborted')
