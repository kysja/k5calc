import tkinter as tk
import keyboard
from slylib import CalcLexer, CalcParser
from configparser import ConfigParser


def enter(event):
    val = entry.get()
    
    if val.replace(".", "", 1).isdigit():
        entry.select_range(0,tk.END)
    else:
        lexer = CalcLexer()
        parser = CalcParser()
        res = round(parser.parse(lexer.tokenize(val)),12)
        res = int(res) if res == int(res) else res
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
        history.insert(0, val + "=" + str(res))
        if len(history) > 15: history.pop(15)
        historydisplay()

def historydisplay():
    for i in range(0,len(histlabels)):  
        if histlabels[i]: histlabels[i].destroy() # Clear previous history
    if len(history)>1: histbtn.grid(row=3, column=4, padx=5, pady=(0,15), sticky="w") # Display history button

    # History - Last line or all
    forlength = len(history) if historyvisible else 1 
    for i in range(0,forlength): 
        histlabels.insert(i, tk.Label(win, font=config['font_history'], bg="#698ad1", fg="#eeeeee", justify="right"))
        histlabels[i].grid(row=(3+i), column=2, padx=20, pady=(0,15), sticky="e")
        histlabels[i]['text'] = history[i]
        histlabels[i].bind('<Button-1>', lambda x, a=history[i]: history2entry(a))


def historytoggle():
    global historyvisible
    historyvisible = False if historyvisible else True
    historydisplay()

def history2entry(val):
    val = val.split("=")[0]
    entry.delete(0, tk.END)
    entry.insert(tk.END, val)




def winhideshow():
    if win.state() == 'normal':
        win.withdraw()
    else:
        win.deiconify()
        win.focus_force()
        entry.focus_set()

def dragwin(event):
    x = win.winfo_pointerx() - win._offsetx
    y = win.winfo_pointery() - win._offsety
    win.geometry('+{x}+{y}'.format(x=x,y=y))

def clickwin(event):
    geom = win.geometry().split('+')
    win._offsetx = win.winfo_pointerx() - int(geom[1])
    win._offsety = win.winfo_pointery() - int(geom[2])




cp = ConfigParser()
cp.read('config.ini')
config = {}
config['hotkey']  = cp.get('settings', 'hotkey')
config['bgcolor'] = cp.get('settings', 'bgcolor')
config['font_history'] = cp.get('settings', 'font_history')
config['font_main'] = cp.get('settings', 'font_main')



win = tk.Tk()
win.title("K5calc - Simple Calculator")
win.iconbitmap('images/k5calc.ico')
win.resizable(0,0)
win.configure(background=config['bgcolor'])
win.overrideredirect(1)
win.wm_attributes('-topmost', True)
# win.wm_attributes('-transparentcolor', '#3764ab')
win.attributes('-toolwindow', True)
win.bind('<Escape>', lambda x: winhideshow())
keyboard.add_hotkey(config['hotkey'], winhideshow)


logoimg = tk.PhotoImage(file="images/logo.png")
logo = tk.Label(win, image = logoimg, background=config['bgcolor'])
logo.grid(row=2, column=1, padx=(20,5), pady=20, sticky="w")
logo.bind('<Button-1>',clickwin)
logo.bind('<B1-Motion>',dragwin)


entry = tk.Entry(win, width=30, font = config['font_main'], bg="#ffffff", justify="right", bd=7, relief="flat")
entry.grid(row=2, column=2, padx=(5,20), pady=20, sticky="w")
entry.focus_set()
entry.bind('<Return>', enter)


historyvisible = False
history = []
histlabels = []

histbtn = tk.Button(win, text="History", command=historytoggle, relief="flat")
histbtnimg = tk.PhotoImage(file="images/history.png")
histbtn.config(image=histbtnimg)

minbtn = tk.Button(win, text="Minimize", command=winhideshow, relief="flat")
minimg = tk.PhotoImage(file="images/min.png")
minbtn.config(image=minimg)
minbtn.grid(row=2, column=4, padx=5, pady=20, sticky="w")

closebtn = tk.Button(win, text="Close", command=lambda: win.destroy(), relief="flat")
closebtnimg = tk.PhotoImage(file="images/close.png")
closebtn.config(image=closebtnimg)
closebtn.grid(row=2, column=5, padx=(5,20), pady=20, sticky="w")


win.mainloop()





