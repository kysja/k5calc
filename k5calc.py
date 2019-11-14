import tkinter as tk
import keyboard
from slylib import CalcLexer, CalcParser


def on_triggered(): 
    win.deiconify()
    win.focus_force()
    entry.focus_set()


def enter(event):
    val = entry.get()
    lexer = CalcLexer()
    parser = CalcParser()
    res = parser.parse(lexer.tokenize(val))
    if int(res) == res:
         res = int(res)

    prev['text'] = val
    if not prev.grid_info():
        # entry.grid(pady=(10,0))
        prev.grid(row=3, column=2, padx=20, pady=(0,30), sticky="e")
        prev.bind('<Button-1>', prev2entry)
    

    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

    history(val + "=" + str(res))


def keyb(event):
    win.withdraw()
    keyboard.add_hotkey('alt+x', on_triggered)


def history(newval):
    if hist.size()>29:
        hist.delete(28)
    hist.insert(0, newval)


def historytoggle():
    if (hist.grid_info()):
        hist.grid_forget()
    else:
        hist.grid(row=4, column=2, padx=10, pady=10, sticky="w")
    
def history2entry(event):
    hpos = hist.curselection()[0]
    hval = hist.get(hpos,hpos)[0]
    hval = hval.split("=")[0]
    entry.delete(0, tk.END)
    entry.insert(tk.END, hval)
    entry.focus_set()

def prev2entry(event):
    entry.delete(0, tk.END)
    entry.insert(tk.END, prev["text"])

def dragwin(event):
    x = win.winfo_pointerx() - win._offsetx
    y = win.winfo_pointery() - win._offsety
    win.geometry('+{x}+{y}'.format(x=x,y=y))

def clickwin(event):
    geom = win.geometry().split('+')
    win._offsetx = win.winfo_pointerx() - int(geom[1])
    win._offsety = win.winfo_pointery() - int(geom[2])





win = tk.Tk()
win.title("K5calc - Simple Calculator")
win.iconbitmap('k5calc.ico')
win.resizable(0,0)
win.configure(background="#3764ab")
win.overrideredirect(1)
win.wm_attributes('-topmost', True)
# win.wm_attributes('-transparentcolor', '#dddddd')
win.attributes('-toolwindow', True)
win.bind('<Escape>', keyb)


logoimg = tk.PhotoImage(file="logo.png")
logo = tk.Label(win, image = logoimg, background="#3764ab")
logo.grid(row=2, column=1, padx=(20,5), pady=20, sticky="w")


entry = tk.Entry(win, width=30, font = "Helvetica 20 bold", bg="#ffffff", justify="right", bd=7, relief="flat")
entry.grid(row=2, column=2, padx=(5,20), pady=20, sticky="w")
entry.insert(0,"15+22")
entry.focus_set()
entry.bind('<Return>', enter)

prev = tk.Label(win, font = "Courier 11", bg="#698ad1", fg="#eeeeee", justify="right")


hist = tk.Listbox(win, width=64, height=30, font="Courier 9", justify="right", relief="flat", fg="#eeeeee", bg="#698ad1", bd=0, activestyle="none", selectbackground="#3764ab", selectforeground="#eeeeee")
hist.bind('<Double-1>', history2entry)

histbtn = tk.Button(win, text="History", command=historytoggle, relief="flat")
histbtnimg = tk.PhotoImage(file="history.png")
histbtn.config(image=histbtnimg)
histbtn.grid(row=2, column=3, padx=5, pady=20, sticky="w")

moveimg = tk.PhotoImage(file="move.png")
move = tk.Label(win, image = moveimg)
move.grid(row=2, column=4, padx=5, pady=20, sticky="w")
move.bind('<Button-1>',clickwin)
move.bind('<B1-Motion>',dragwin)


closebtn = tk.Button(win, text="Close", command=lambda: win.destroy(), relief="flat")
closebtnimg = tk.PhotoImage(file="close.png")
closebtn.config(image=closebtnimg)
closebtn.grid(row=2, column=5, padx=(5,20), pady=20, sticky="w")





win.mainloop()





