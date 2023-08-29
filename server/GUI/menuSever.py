from tkinter import *
from tkinter import font
try:
    from .define import *
    from . import config
except:
    from define import *
    import config

menuSever = Tk()

fontWord = font.Font(family = "Times New Roman", size = 10)

def open_server():
    config.openServer = True

def menuSeverSetup ():
    menuSever.geometry("200x150")
    menuSever.title('Sever')
    menuSever['background'] = COLOUR_BACKGROUND
    menuSever.resizable(False, False)
    buttonOpen = Button(menuSever, text = 'Open Sever', command=open_server,bg = COLOUR_BUTTON, fg = COLOUR_FONT, font = fontWord, activeforeground = COLOUR_AFTER, width = 10, padx = 10, pady = 15)
    buttonOpen.place(relx = 0.5, rely = 0.5, anchor = CENTER) 

def on_closing():
    global menuSever
    config.openServer = False
    menuSever.quit()  # Quit the mainloop
    menuSever.destroy()

def runServerGUI():
    menuSeverSetup()
    menuSever.protocol("WM_DELETE_WINDOW", on_closing)
    menuSever.mainloop()
