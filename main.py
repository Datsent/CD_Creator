import ctypes
import glob
import os
import shutil
import time
from tkinter import *
from tkinter import messagebox

from Utils.Utils import *


def eject_disk():
    messagebox.showinfo('information', 'הצריבה הסתיימה ')
    time.sleep(3)
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)


ws = Tk()

# top_box = Toplevel(ws)
ws.title('CD-Creator')
ws.geometry('300x200')
width = 300
height = 150
x = int(ws.winfo_screenwidth() / 2 - width / 2)
y = int(ws.winfo_screenheight() / 2 - height / 2)
ws.geometry("+{}+{}".format(x, y))
ws.config(bg='#5FB691')


def format_cd(driver):
    os.system(f'cmd /c "format {driver}: /y"')


def copy_file(src, des):
    shutil.copy2(src, des)


def msg1():
    messagebox.showinfo('information', 'Hi! You got a prompt.')
    messagebox.showerror('error', 'Something went wrong!')
    messagebox.showwarning('warning', 'accept T&C')
    messagebox.askquestion('Ask Question', 'Do you want to continue?')
    messagebox.askokcancel('Ok Cancel', 'Are You sure?')
    messagebox.askyesno('Yes|No', 'Do you want to proceed?')
    messagebox.askretrycancel('retry', 'Failed! want to try again?')


def find_file(sn, wo):
    for folder in glob.glob(f'{DSC_PATH}\\*{wo}*\\CD*'):
        print(folder)
        if glob.glob(f'{DSC_PATH}\\*{wo}*\\CD*\\*{sn}*'):
            for file in glob.glob(f'{DSC_PATH}\\*{wo}*\\CD*\\*{sn}*'):
                print('Coping...')
                print(file)
                copy_file(file, f'{CD_LETTER}:\\')
        else:
            messagebox.showinfo('information', f' {sn} אין קבצים עבור מעגל:')


def find_sn():
    file1 = open(FILE, 'r')
    Lines = file1.readlines()
    print(Lines[0].strip())
    if glob.glob(f'{DSC_PATH}\\*{Lines[0].strip()}*\\CD*'):
        for line in Lines[1:]:
            # print(f"{line.strip()}")
            # print(Lines[0].strip())
            find_file(line.strip(), Lines[0].strip())
    else:
        messagebox.showinfo('information', f' {Lines[0].strip()} אין קבצים עבור פק"ע:')


def main():
    path = f'{CD_LETTER}:\\'
    format_cd(CD_LETTER)
    isExist = os.path.exists(path)
    print(isExist)
    while not os.path.exists(path):
        if messagebox.askquestion('Ask Question', 'No Disk, want try again?') == 'yes':
            format_cd(CD_LETTER)
        else:
            quit()
    find_sn()
    print('waiting...')
    print('ejecting...')
    eject_disk()


if __name__ == '__main__':
    main()
