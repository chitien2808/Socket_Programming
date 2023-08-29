from tkinter import *
from tkinter import scrolledtext
from tkinter import font
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter import Toplevel, Label, Button, PhotoImage
from PIL import Image, ImageTk
from tkinter.scrolledtext import ScrolledText
import queue
import time

import os
import time
try:
    from . import communicate
    from .define import *
    from .app import App
except:
    import communicate
    from define import *
    from app import App


mainclient = None
fontWord = None


class MyStruct:
    def __init__(self, string1, string2, string3):
        self.string1 = string1
        self.string2 = string2
        self.string3 = string3

class info():
    def __init__(self,ID,Name,Thread):
        self.ID = ID
        self.Name = Name
        self.Thread = Thread

pcs_list = []


   

def click_button(s, saveKey = False):
    communicate.command = s
    if saveKey:
        communicate.start_id = communicate.kill_id = s

def change_frame(frame):
    style2 = ttk.Style()
    style2.configure('Custom.TFrame', background= COLOUR_BACKGROUND)
    frame.configure(style='Custom.TFrame')
  

def open_folder(root,textbox1,scrolledbox):
    file_path = filedialog.askopenfilename()
    textbox1.delete(0, tk.END)
    textbox1.insert(0, file_path)
    with open(file_path, 'r') as file:
        content = file.read()
        scrolledbox.delete('1.0', tk.END)  # Xóa nội dung hiện tại trong vùng văn bản có cuộn
        scrolledbox.insert(tk.END, content)  # Chèn nội dung file vào vùng văn bản có cuộn
    
    
    


def notice4(root,s):
    my_not4 = Toplevel(root)
    my_not4.geometry("250x250")
    my_not4.configure(bg = COLOUR_BACKGROUND)
    my_not4.title('')
    s = s.split(' ')
    l1 = Label(my_not4,text =  'Đã diệt ' + s[1],bg = COLOUR_BACKGROUND,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER).grid(column=1, row = 1, padx = 50, pady = 70)

def notice5(root,s):
    my_not5 = Toplevel(root)
    my_not5.geometry("250x250")
    my_not5.configure(bg = COLOUR_BACKGROUND)
    my_not5.title('')
    s = s.split(' ')
    l1 = Label(my_not5,text = 'Không tồn tại ' + s[1],bg = COLOUR_BACKGROUND,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER).grid(column=1, row = 1, padx = 50, pady = 70)

# Điều kiện của Start

def notice6(root,s):
    my_not6 = Toplevel(root)
    my_not6.geometry("250x250")
    my_not6.configure(bg = COLOUR_BACKGROUND)
    my_not6.title('')
    print(s)
    s = s.split(' ')
    print(s)
    l1 = Label(my_not6,text = 'Đã bật ' + s[1],bg = COLOUR_BACKGROUND,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER).grid(column=1, row = 1, padx = 50, pady = 70)


def kill(s, root, self, filename = "processData.txt"):
    if communicate.status == "kill_ok": 
       delete(self)
       time.sleep(1)
       if filename == "processData.txt":click_button("listprocess")
       if filename == "apprunningData.txt":click_button("listrunningapp")
       notice4(root,s)
    else:
       notice5(root,s)


    
           
           
def start(s, root, self, filename = "processData.txt"):
    # click_button(s)
    if communicate.status == "open_ok":
        delete(self)
        time.sleep(1)
        if filename == "processData.txt":click_button("listprocess")
        if filename == "apprunningData.txt":
           click_button("listrunningapp")
        notice6(root,s)
    else:
        notice5(root,s)
    
def kill_window(s,root,self, filename = "processData.txt"):
    my_kll = Toplevel(root)
    my_kll.geometry("280x60")
    my_kll.configure(bg = COLOUR_BACKGROUND)
    my_kll.title('Kill')
    txt = Entry(my_kll,width=30)
    txt.place(x=1, y=10)
    txt.focus()
    communicate.root_kill = root 
    communicate.self_kill = self
    # Button(my_kll, text="Kill",width=8,command = lambda: kill(s+" "+txt.get(),my_kll,self, filename)).place(x=200, y=10)
    Button(my_kll, text="Kill",width=8,command = lambda: click_button(s + " " + txt.get(), True)).place(x=200, y=10)

    
    
def start_window(s,root,self, filename = "processData.txt"):
    my_sta = Toplevel(root)
    my_sta.geometry("280x60")
    my_sta.configure(bg = COLOUR_BACKGROUND)
    my_sta.title('Start')
    txt = Entry(my_sta,width=30)
    txt.place(x=1, y=10)
    txt.focus()
    communicate.root_start = root 
    communicate.self_start = self
    # Button(my_sta, text = "Start", width = 8,command = lambda: start(s+" "+txt.get(),my_sta,self, filename)).place(x = 200, y = 10)
    Button(my_sta, text = "Start", width = 8,command = lambda: click_button(s + " " + txt.get(), True)).place(x = 200, y = 10)

def do_kill(s,root,self, filename = "processData.txt"):
    kill_window(s,root,self, filename)
    

def do_start(s,root,self, filename = "processData.txt"):
    start_window(s,root,self, filename)


def delete(self):
    # click_button(s)
    for i in self.my_tree.get_children():
        self.my_tree.delete(i)
    
    
def insertText(self, fileDataName = "processData.txt"):
    # click_button(s)
    delete(self)
    script_dir = os.path.dirname(__file__)
    img_path = os.path.join(script_dir, "tempData\\" + fileDataName)
    self.my_tree.delete()
    with open(img_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            values = line.strip().split(',')
            if len(values) == 3:
                my_struct = MyStruct(values[0], values[1], values[2])
                self.my_tree.insert("", 'end', values= (values[0], values[1], values[2]))
                
def send_content(s):
    click_button(s)
    
    
def displayImage(my_scr):
    script_dir = os.path.dirname(__file__)
    img_path = os.path.join(script_dir, "tempData/tempImage.png")

    # Open and resize the image using Pillow
    new_width = 495
    new_height = 455
    with Image.open(img_path) as img:
        img = img.resize((new_width, new_height))

    # Convert PIL image to PhotoImage
    img_tk = ImageTk.PhotoImage(img)

    label = Label(my_scr, image=img_tk, width=new_width, height=new_height)
    label.image = img_tk  # this is to prevent garbage collection of the img_tk object
    label.place(relx=0.08, rely=0.1)

#Khi nào merge được connection sẽ dùng để check kết nối   
def notice1():
    my_not1 = Toplevel(mainClient)
    my_not1.geometry("250x250")
    my_not1.configure(bg = COLOUR_BACKGROUND)
    my_not1.title('')
    l1 = Label(my_not1,text = 'Chưa kết nối đến server',bg = COLOUR_BACKGROUND,fg = '#272829',activeforeground = COLOUR_AFTER).grid(column=1, row = 1, padx = 50, pady = 70)


    
def notice2():
    my_not2 = Toplevel(mainClient)
    my_not2.geometry("250x250")
    my_not2.configure(bg = COLOUR_BACKGROUND)
    my_not2.title('')
    l1 = Label(my_not2,text = 'Lỗi kết nối đến server',bg = COLOUR_BACKGROUND,fg = '#272829',activeforeground = COLOUR_AFTER).grid(column=1, row = 1, padx = 50, pady = 70)



def notice3():
    my_not3 = Toplevel(mainClient)
    my_not3.geometry("250x250")
    my_not3.configure(bg = COLOUR_BACKGROUND)
    my_not3.title('')
    l1 = Label(my_not3,text = 'Kết nối đến server thành công',bg = COLOUR_BACKGROUND,fg = '#272829',activeforeground = COLOUR_AFTER).grid(column=1, row = 1, padx = 50, pady = 70)    

def notice7():
    my_not7 = Toplevel(mainClient)
    my_not7.geometry("250x250")
    my_not7.configure(bg = COLOUR_BACKGROUND)
    my_not7.title('')
    l1 = Label(my_not7,text = 'Ngắt kết nối thành công ',bg = COLOUR_BACKGROUND,fg = '#272829',activeforeground = COLOUR_AFTER).grid(column=1, row = 1, padx = 50, pady = 70)


def scr_window():
    if communicate.status_connection == 0:
       notice1()
       return
    my_scr = Toplevel(mainClient)
    my_scr.geometry("700x550")
    my_scr.configure(bg = COLOUR_BACKGROUND)
    my_scr.title('Server Screen')
    my_scr.resizable(False, False)
    my_scr.grab_set()
    communicate.src_screen = my_scr

    label = Label(my_scr, bg = "#FFFFFF", width=65, height=30) #width = img_width/3.5, height = img_height/3.2)
    # label.image = img
    label.place(relx = 0.1, rely = 0.1 )

    script_dir = os.path.dirname(__file__)
    img_path = os.path.join(script_dir, "tempData/tempImage.png")
    img = PhotoImage(file = img_path)

    img_width = img.width()
    img_height = img.height()

    # img_width = 500
    # img_height = 400

    buton1 = Button(my_scr,text = 'Chụp',bg = COLOUR_BUTTON,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER, font = fontWord, width = 8, height = 16, command = lambda: click_button("screenshot"))
    buton2 = Button(my_scr,text = 'Lưu',bg = COLOUR_BUTTON,fg = COLOUR_FONT,activeforeground = COLOUR_AFTER, font = fontWord,width = 8, height = 8, command = lambda: click_button("saveimage"))
    buton1.place(x = 600, y = 65 )
    buton2.place(x = 600, y = 380 )

def send_keyLogger (txt):  
    # click_button(s)
    #if communicate.status_connection == 0:
    #    notice1()
    #    return
    # notice3()
    script_dir = os.path.dirname(__file__)
    text_path = os.path.join(script_dir, "tempData/keylogger.txt")
    
    txt.pack()
    try:
        with open(text_path, 'r') as file:
            content = file.read()
            
        # Clear the existing content from the Listbox
        txt.delete("1.0", tk.END)
        
        # Insert the new content into the Listbox
        txt.insert(tk.END, content)
    except FileNotFoundError:
        print("Keylogger file not found.")

def delete_Keystroke(txt):
    script_dir = os.path.dirname(__file__)
    filePath = os.path.join(script_dir, "tempData/keylogger.txt")
    with open(filePath, "w") as fi:
        pass 
    txt.delete("1.0", tk.END)

def kst_window():
    if communicate.status_connection == 0:
       notice1()
       return
    script_dir = os.path.dirname(__file__)
    filePath = os.path.join(script_dir, "tempData/keylogger.txt")
    with open(filePath, "w") as fi:
        pass 
    my_kst = Toplevel(mainClient)
    my_kst.geometry("750x500")
    my_kst.configure(bg = COLOUR_BACKGROUND)
    my_kst.title('Keystroke')
    my_kst.resizable(False, False)
    my_kst.grab_set()
    frame1 = ttk.Frame(my_kst)
    change_frame(frame1)
    frame1.pack(side="top", pady=20)
    button1 = ttk.Button(frame1, text="Hook", width=20, command=lambda: click_button("hook"))
    button2 = ttk.Button(frame1, text="Unhook", width=20, command=lambda: click_button("unhook"))
    # button3 = ttk.Button(frame1, text="In phím", width=20, command=lambda: send_keyLogger("sendkeylogger", txt))
    button3 = ttk.Button(frame1, text="In phím", width=20, command=lambda: click_button("sendkeylogger"))
    button4 = ttk.Button(frame1, text="Xóa", width=20, command=lambda: delete_Keystroke(txt))
    button_list = [button1, button2, button3, button4]
    for i in range(len(button_list)):
        button_list[i].pack(side="left", padx=15)
    frame2 = ttk.Frame(my_kst)
    frame2.pack(side="top",pady=15)
    txt = ScrolledText(frame2,width=100,height=25)
    communicate.keylogger_txt = txt
    txt.pack()

def pcs_window():
    if communicate.status_connection == 0:
       notice1()
       return
    my_pcs = Toplevel(mainClient)
    my_pcs.geometry("750x500")
    my_pcs.configure(bg = COLOUR_BACKGROUND)
    my_pcs.title('process')
    my_pcs.resizable(False, False)
    my_pcs.grab_set()
    frame1 = ttk.Frame(my_pcs)
    change_frame(frame1)
    frame1.pack(side="top", pady=20)
    frame2 = ttk.Frame(my_pcs)
    communicate.frameProcess = frame2
    frame2.pack(side="top")
    # Tạo listbox và đặt chúng ngang hàng nhau trong scrolledtext của frame 2
    cols = ("ID Process", "Name Process", "Count Thread")
    frame2.my_tree = ttk.Treeview(frame2, column = cols, height= 10, selectmode = "browse", show = 'headings')
    frame2.my_tree.column("#1", anchor= tk.CENTER, stretch= 'no', width= 175)
    frame2.my_tree.heading("#1", text="Id Process")
    frame2.my_tree.column("#2", anchor= tk.CENTER, stretch= 'no', width = 175)
    frame2.my_tree.heading("#2", text="Name Process")
    frame2.my_tree.column("#3", anchor= tk.CENTER, stretch= 'no', width = 175)
    frame2.my_tree.heading("#3", text="Count Thread")
    tree_scroll = ttk.Scrollbar(frame2, orient= "vertical")
    tree_scroll.configure(command= frame2.my_tree.yview)
    frame2.my_tree.configure(yscrollcommand= tree_scroll.set)
    #position
    frame2.my_tree.place(x = 24, y = 130)
    tree_scroll.place(x = 552, y= 130, height= 226)
    frame2.my_tree.pack(side=tk.LEFT, fill=tk.Y)
    tree_scroll.pack(side=tk.LEFT, fill=tk.Y)
    frame2.arrayInfo = []
    style1 = ttk.Style()
    style1.configure('TButton', background= COLOUR_BUTTON)
    button1 = ttk.Button(frame1, text="Kill", width=20, style='TButton', command = lambda: do_kill("killprocess",my_pcs,frame2))
    button2 = ttk.Button(frame1, text="Xem", width=20, style='TButton', command = lambda: click_button("listprocess"))
    button2.configure(style='TButton')
    button3 = ttk.Button(frame1, text="Xóa", width=20, style='TButton', command = lambda: delete(frame2))
    button3.configure(style='TButton')
    button_list = [button1, button2, button3]
    for i in range(len(button_list)):
        button_list[i].pack(side="left", padx=15)

    if not my_pcs.winfo_exists():
         frame2.arrayInfo = []
    # Chạy chương trình
    my_pcs.mainloop()



def app_window():
    if communicate.status_connection == 0:
       notice1()
       return
    my_app = Toplevel(mainClient)
    my_app.geometry("750x500")
    my_app.configure(bg = COLOUR_BACKGROUND)
    my_app.title('listApp')
    my_app.resizable(False, False)
    my_app.grab_set()
    frame1 = ttk.Frame(my_app)
    change_frame(frame1)
    frame1.pack(side="top", pady=20)
    frame2 = ttk.Frame(my_app)
    communicate.frameRunningApp = frame2
    frame2.pack(side="top")
    cols = ("Id Application", "Name Application", "Count Thread")
    frame2.my_tree = ttk.Treeview(frame2, column = cols, height= 10, selectmode = "browse", show = 'headings')
    frame2.my_tree.column("#1", anchor= tk.CENTER, stretch= 'no', width= 175)
    frame2.my_tree.heading("#1", text="ID Application")
    frame2.my_tree.column("#2", anchor= tk.CENTER, stretch= 'no', width = 175)
    frame2.my_tree.heading("#2", text="Name Application")
    frame2.my_tree.column("#3", anchor= tk.CENTER, stretch= 'no', width = 175)
    frame2.my_tree.heading("#3", text="Count Thread")
    tree_scroll = ttk.Scrollbar(frame2, orient= "vertical")
    tree_scroll.configure(command= frame2.my_tree.yview)
    frame2.my_tree.configure(yscrollcommand= tree_scroll.set)
    #position
    frame2.my_tree.place(x = 24, y = 130)
    tree_scroll.place(x = 552, y= 130, height= 226)
    frame2.my_tree.pack(side=tk.LEFT, fill=tk.Y)
    tree_scroll.pack(side=tk.LEFT, fill=tk.Y)
    frame2.arrayInfo = []
    style1 = ttk.Style()
    style1.configure('TButton', background= COLOUR_BUTTON)
    button1 = ttk.Button(frame1, text="Kill", width=20, style='TButton', command = lambda: do_kill("killrunningapp",my_app,frame2, "apprunningData.txt"))
    button2 = ttk.Button(frame1, text="Xem", width=20, style='TButton', command = lambda: click_button("listrunningapp"))
    button2.configure(style='TButton')
    button3 = ttk.Button(frame1, text="Xóa", width=20, style='TButton', command = lambda: delete(frame2))
    button3.configure(style='TButton')
    button4 = ttk.Button(frame1, text="Start", width=20, style='TButton', command = lambda: do_start("openapp",my_app,frame2, "apprunningData.txt"))
    button4.configure(style='TButton')
    button_list = [button1, button2, button3, button4]
    for i in range(len(button_list)):
        button_list[i].pack(side="left", padx=15)
    if not my_app.winfo_exists():
         frame2.arrayInfo = []    
    # Chạy chương trình
    my_app.mainloop()

def on_combobox_choose(combobox,choices1):
        selected_choice = combobox.get()
        if selected_choice == choices1[0]:
            click_button("Get Value")
        elif selected_choice == choices1[1]:
            click_button("Creat Key")
        elif selected_choice == choices1[2]:
            click_button("Delete Value")
        elif selected_choice == choices1[3]:
            click_button("Create Key")
        elif selected_choice == choices1[4]:
            click_button("Delete Key")
            

def on_combobox_type(combobox,choices2):
    selected_choice = combobox.get()
    if selected_choice == choices2[0]:
       click_button("String")
    elif selected_choice == choices2[1]:
         click_button("Binary")
    elif selected_choice == choices2[2]:
         click_button("DWORD")
    elif selected_choice == choices2[3]:
         click_button("QWORD")
    elif selected_choice == choices2[4]:
         click_button("Multi String")
    elif selected_choice == choices2[5]:     
         click_button("Expandable String")   
 
def rgt_window():
    if communicate.status_connection == 0:
       notice1()
       return
    my_rgt = Toplevel(mainClient)
    my_rgt.geometry("550x590")
    my_rgt.configure(bg = COLOUR_BACKGROUND)
    my_rgt.title('Registry')
    my_rgt.resizable(False, False) 
    # Tạo frame 1
    frame1 = ttk.Frame(my_rgt)
    frame1.pack(side="top", pady=5)
    change_frame(frame1)
    # Tạo frame 2
    frame2 = ttk.Frame(my_rgt)
    frame2.pack(side="top",pady= 5)
    change_frame(frame2)
    txt = scrolledtext.ScrolledText(frame2,height = 8)
    textbox_path = ttk.Entry(frame1)
    button_browser = ttk.Button(frame1, text="Browser",command = lambda: open_folder(my_rgt,textbox_path,txt))
    button_browser.pack(side="right", padx=10, pady=10)
    textbox_path.pack(side="right", padx=10, pady=10)
    textbox_path.configure(width = 50) 
    txt.pack(side="left")
    txt.configure(width = 38)
    but = ttk.Style()
    but.configure('TButton', height=80)
    button_send_content = ttk.Button(frame2, text="Gửi nội dung",command = lambda: click_button("Gửi nội dung"))
    button_send_content.configure(style = 'TButton')
    button_send_content.pack(side="left", padx=0, pady=5)
  

    # Tạo frame 3
    frame3 = ttk.Frame(my_rgt)
    frame3.pack(side="top")
    change_frame(frame3)
    style = ttk.Style()
    style.configure('TLabel', background= COLOUR_BACKGROUND)
    label_text = ttk.Label(frame3, text="Sửa Giá Trị Trực Tiếp --------------------------------------------------------------",style = 'TLabel')
    label_text.pack(padx=2, pady=15)
    

    # Tạo frame 4

    frame4 = ttk.Frame(my_rgt)
    frame4.pack(side="top",pady=5)
    change_frame(frame4)
    # Tạo combobox
    combobox = tk.StringVar(frame4)
    combobox.set("Chọn tác vụ")  # Giá trị mặc định
        
    # Tạo danh sách các lựa chọn
    choices1 = ["Get Value      ", "Creat Key      ", "Delete Value      ","Create Key      ","Delete Key      "]

    

    # Hàm xử lý khi người dùng thay đổi giá trị của combobox


    # Tạo combobox và gắn sự kiện cho nó
    combobox_widget = tk.OptionMenu(frame4 , combobox, *choices1, command=on_combobox_choose(combobox,choices1))
    combobox_widget.configure(width = 63) 
    combobox_widget.pack(pady=10)

    # Tạo Frame 5
    frame5 = ttk.Frame(my_rgt)
    frame5.pack(side="top", pady=5)
    change_frame(frame5)
    # Thêm Textbox vào Frame
    textbox1 = ttk.Entry(frame5)
    textbox1.pack(padx=10, pady=10)
    textbox1.configure(width = 68) 

    # Tạo Frame 6
    frame6 = ttk.Frame(my_rgt)
    frame6.pack(side="top", pady=5)
    change_frame(frame6)
    # Thêm Textbox vào Frame 2 (cách đều nhau)
    textbox2 = ttk.Entry(frame6)
    textbox3 = ttk.Entry(frame6)
    combobox = tk.StringVar(frame6)
    textbox2.pack(side="left", padx=10)
    textbox3.pack(side="left", padx=10)
    combobox.set("Chọn tác vụ")  # Giá trị mặc định

    # Tạo danh sách các lựa chọn
    choices2 = ["String      ", "Binary    ", "DWORD      ","QWORD     ","Multi String  ","Expandable String  "]

    # Tạo combobox và gắn sự kiện cho nó
    combobox_widget = tk.OptionMenu(frame6 , combobox, *choices2, command=on_combobox_type(combobox,choices2))
    combobox_widget.configure(width = 14) 
    combobox_widget.pack(side="left", padx=10)


    # Tạo Frame 7
    frame7 = ttk.Frame(my_rgt)
    frame7.pack(side="top", pady=5)
    change_frame(frame7)    
    listbox = tk.Listbox(frame7)
    listbox.configure(width = 69, height = 8) 
    listbox.pack()

    # Frame 8
    frame8 = ttk.Frame(my_rgt)
    frame8.pack(side="top", pady=5)
    change_frame(frame8) 
    style1 = ttk.Style()
    style1.configure('TButton', background= COLOUR_BUTTON)
    button1 = ttk.Button(frame8, text="Gửi", width=25,command = lambda: click_button('Gửi'))
    button1.configure(style='TButton')
    button2 = ttk.Button(frame8, text="Xóa", width=25,command = lambda: click_button('Xóa'))
    button2.configure(style='TButton')
    button_list = [button1, button2]
    for i in range(len(button_list)):
        button_list[i].pack(side="left", padx=20)
    

def get_ip(entryBox):
    if (communicate.status_connection != 0) : return
    ip = entryBox.get()
    communicate.ipHost = ip
    communicate.status_connection = 1
    while communicate.status_connection == 1 : pass
    if communicate.status_connection == 2 :
       notice3()   
    else:
       notice2() 

def check_valid_ip(ip):
    return True
    # Check if the IP contains only digits and dots
    return all(c.isdigit() or c == '.' for c in ip) 

def validate_input(char):
    return True
    # Allow only numbers and dots (for IP address)
    if char.isdigit() or char == '.':
        return True
    else:
        return False

def disconnect_work (s):
    if communicate.status_connection == 2 : 
        click_button(s)
        notice7()
    else : 
        notice1()
        return



def draw ():
    frame1 = ttk.Frame(mainClient)
    frame1.pack(side="top",pady=5)
    entryBox = Entry(frame1, bg = "#E9F4EE", fg = "#000000", font = fontWord, justify = LEFT, bd = 15, width = 77) #validate = "key", validatecommand=(mainClient.register(validate_input), "%S")
    entryBox.pack(side="left", padx=10)
    buttonConnect = Button(frame1, text = "Connect", font = fontWord, width = 21, bg = COLOUR_BUTTON, fg = COLOUR_FONT, padx = 50, pady = 15, command=lambda: get_ip(entryBox))
    buttonConnect.pack(side="left", padx=10)
    change_frame(frame1)
    frame2 = ttk.Frame(mainClient)
    frame2.pack(side="left",pady=5)
    change_frame(frame2)
    buttonProcess = Button(frame2, text = "Process Running", font = fontWord, width = 30,height =50, bg = COLOUR_BUTTON, fg = COLOUR_FONT,command = lambda: pcs_window())
    buttonProcess.pack(side="left", padx=10)
    frame3 = ttk.Frame(mainClient)
    frame3.pack(side="left",padx=5)
    change_frame(frame3)
    frame4 = ttk.Frame(frame3)
    frame4.pack(side="top",pady=5)
    change_frame(frame4)
    buttonApp = Button(frame4, text = "App Running", font = fontWord, width = 36, height =7, bg = COLOUR_BUTTON, fg = COLOUR_FONT, command = lambda: app_window())
    buttonApp.pack(side="top",pady=2)
    frame5 = ttk.Frame(frame3)
    frame5.pack(side="top",pady=5)
    change_frame(frame5)
    buttonTurnOff = Button(frame5, text = "Turn-Off\n\nComputer", font = fontWord, width = 15, height =1, bg = COLOUR_BUTTON, fg = COLOUR_FONT, command = lambda: click_button("shutdown"), padx = 10, pady = 33)
    buttonTurnOff.pack(side="left",pady=5)
    buttonCap = Button(frame5, text = "Print\n\nScreen", font = fontWord, width = 15, height =1, bg = COLOUR_BUTTON, fg = COLOUR_FONT,command = lambda: scr_window(), padx = 10, pady = 33)
    buttonCap.pack(side="left",pady=5)
    frame6 = ttk.Frame(frame3)
    frame6.pack(side="top",pady=5)
    change_frame(frame6)
    buttonRegistry = Button(frame6, text = "Disconnect Server", font = fontWord, width = 31, height =7, bg = COLOUR_BUTTON, fg = COLOUR_FONT, command = lambda: disconnect_work("disconnect"), padx = 20, pady = 33)
    buttonRegistry.pack(side="top",pady=2)
    frame7 = ttk.Frame(mainClient)
    frame7.pack(side="left",padx=5)
    change_frame(frame7)
    frame8 = ttk.Frame(frame7)
    frame8.pack(side="top",pady=5)
    change_frame(frame8)
    buttonKeyStroke = Button(frame8, text = "Keystroke", font = fontWord, width = 20, height =3, bg = COLOUR_BUTTON, fg = COLOUR_FONT,command = lambda: kst_window(), padx = 50, pady = 95)
    buttonKeyStroke.pack(side="top",padx=5)
    frame9 = ttk.Frame(frame7)
    frame9.pack(side="top",pady=5)
    change_frame(frame9)    
    buttonExit = Button(frame9, text = "Exit", font = fontWord, width = 20, height =7,bg = COLOUR_BUTTON, fg = COLOUR_FONT, padx = 50, pady = 33, command = on_closing)
    buttonExit.pack(side="top",padx=5)
    mainClient.mainloop()


def on_closing():
    # This function will be executed when the close button is clicked
    communicate.command = "QUIT"
    # You can add any custom cleanup operations or other logic here

    # Close the window
    mainClient.quit()  # Quit the mainloop
    mainClient.destroy()

def check_queue():
    global mainClient
    if communicate.status_connection != 2: 
        mainClient.after(100, check_queue)
        return
    while not communicate.queue_to_main.empty():
        command = communicate.queue_to_main.get()
        if command == "displayimage":
            displayImage(communicate.src_screen)
        elif command == "displaykeylogger":
            send_keyLogger(communicate.keylogger_txt)
        elif command == "displayprocess":
            insertText(communicate.frameProcess)
        elif command == "displayrunningapp":
            insertText(communicate.frameRunningApp, "apprunningData.txt")
        elif command == "kill_ok_process" or command == "kill_err_process":
            kill(communicate.kill_id, communicate.root_kill, communicate.self_kill)
        # elif command == "open_ok_process" or command == "open_err_process":
        #     start(communicate.start_id, communicate.root_start, communicate.self_start)
        elif command == "kill_ok_app" or command == "kill_err_app":
            kill(communicate.kill_id, communicate.root_kill, communicate.self_kill, "apprunningData.txt")
        elif command == "open_ok_app" or command == "open_err_app":
            start(communicate.start_id, communicate.root_start, communicate.self_start, "apprunningData.txt")

    # Schedule the check_queue to run again after 100ms
    mainClient.after(100, check_queue)

def run_GUI():
    global mainClient, fontWord
    mainClient = Tk() 
    app = App(mainClient)
    fontWord = font.Font(family = "Times New Roman", size = 10)
    mainClient.protocol("WM_DELETE_WINDOW", on_closing)
    communicate.queue_to_main = queue.Queue()
    mainClient.after(100, check_queue)
    draw()
    # def is_mainClient_open():
    # print(is_mainClient_open())
    

if __name__ == '__main__':
    run_GUI()
